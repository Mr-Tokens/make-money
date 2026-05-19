from __future__ import annotations

import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request

ROOT = Path(__file__).resolve().parents[1]
DELEGATION_DIR = ROOT / "delegation"
TASKS_DIR = Path(os.environ.get("DELEGATION_TASKS_DIR", str(DELEGATION_DIR / "tasks")))
PROMPTS_DIR = DELEGATION_DIR / "prompts"
PROVIDERS_PATH = DELEGATION_DIR / "providers.example.json"
ENV_PATH = ROOT / ".env"

TASK_TYPES = {"research", "summary", "risk-check", "writing"}
SOURCE_FILE_MAX_CHARS = 8_000
SOURCE_TOTAL_MAX_CHARS = 24_000
FORBIDDEN_SOURCE_DIRS = {".git", ".venv", ".worktrees", "node_modules", "secret", "venv"}
TOKEN_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"tp-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(Authorization:\s*Bearer\s+)[A-Za-z0-9._~+/=-]{8,}", re.IGNORECASE),
    re.compile(r"(api-key:\s*)[A-Za-z0-9._~+/=-]{8,}", re.IGNORECASE),
]


class DelegationError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str, limit: int = 48) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return (slug or "task")[:limit].strip("-") or "task"


def redact_secrets(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: redact_secrets(item) for key, item in value.items()}
    if isinstance(value, list):
        return [redact_secrets(item) for item in value]
    if not isinstance(value, str):
        return value

    redacted = value
    for pattern in TOKEN_PATTERNS:
        if pattern.pattern.startswith("("):
            redacted = pattern.sub(lambda match: match.group(1) + "[REDACTED_TOKEN]", redacted)
        else:
            redacted = pattern.sub("[REDACTED_TOKEN]", redacted)
    return redacted


def load_env_file(path: Path = ENV_PATH) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, raw_value = line.split("=", 1)
        value = raw_value.strip().strip('"').strip("'")
        values[key.strip()] = value
    return values


def merged_env(path: Path = ENV_PATH) -> dict[str, str]:
    values = dict(os.environ)
    values.update(load_env_file(path))
    return values


def load_providers(path: Path = PROVIDERS_PATH) -> dict[str, dict[str, Any]]:
    if not path.exists():
        raise DelegationError(f"Provider metadata file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_provider(
    name: str,
    providers: dict[str, dict[str, Any]],
    env: dict[str, str],
    require_key: bool,
) -> dict[str, str]:
    if name not in providers:
        raise DelegationError(f"Unknown provider: {name}")

    meta = providers[name]
    api_key = env.get(meta["api_key_env"], "")
    if require_key and not api_key:
        raise DelegationError(f"Missing API key env var: {meta['api_key_env']}")

    return {
        "name": name,
        "base_url": env.get(meta["base_url_env"], "") or meta["default_base_url"],
        "api_key": api_key,
        "model": env.get(meta["model_env"], "") or meta["default_model"],
        "token_limit_field": meta.get("token_limit_field", "max_tokens"),
    }


def read_prompt_text(prompt: str | None, prompt_file: str | None) -> str:
    if bool(prompt) == bool(prompt_file):
        raise DelegationError("Provide exactly one of --prompt or --prompt-file")
    if prompt_file:
        return Path(prompt_file).read_text(encoding="utf-8")
    return prompt or ""


def read_worker_template(task_type: str) -> str:
    if task_type not in TASK_TYPES:
        raise DelegationError(f"Unknown task type: {task_type}")
    return (PROMPTS_DIR / f"worker-{task_type}.md").read_text(encoding="utf-8")


def is_url_source(source: str) -> bool:
    return source.startswith(("http://", "https://"))


def resolve_source_file(source: str) -> Path:
    path = Path(source)
    candidate = path if path.is_absolute() else ROOT / path
    resolved = candidate.resolve()
    try:
        relative = resolved.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise DelegationError(f"Source must stay inside project root: {source}") from exc

    parts = {part.lower() for part in relative.parts}
    if parts & FORBIDDEN_SOURCE_DIRS:
        raise DelegationError(f"Source is not safe for worker prompts: {source}")

    name = relative.name.lower()
    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        raise DelegationError(f"Source is not safe for worker prompts: {source}")
    if not resolved.exists() or not resolved.is_file():
        raise DelegationError(f"Source file not found: {source}")
    return resolved


def read_source_excerpt(source: str) -> str:
    if is_url_source(source):
        return f"### {source}\nURL source. Fetch and summarize externally before expecting detailed worker review."

    path = resolve_source_file(source)
    text = path.read_text(encoding="utf-8", errors="replace")
    text = redact_secrets(text)
    truncated = len(text) > SOURCE_FILE_MAX_CHARS
    excerpt = text[:SOURCE_FILE_MAX_CHARS].rstrip()
    if truncated:
        excerpt += "\n...[truncated]"
    return f"### {source}\n```text\n{excerpt}\n```"


def build_source_excerpts(sources: list[str]) -> str:
    if not sources:
        return "- None"

    excerpts: list[str] = []
    used = 0
    for source in sources:
        excerpt = read_source_excerpt(source)
        remaining = SOURCE_TOTAL_MAX_CHARS - used
        if remaining <= 0:
            excerpts.append("...[source excerpt budget exhausted]")
            break
        if len(excerpt) > remaining:
            excerpt = excerpt[:remaining].rstrip() + "\n...[source excerpt budget exhausted]"
        excerpts.append(excerpt)
        used += len(excerpt)
    return "\n\n".join(excerpts)


def build_messages(task_type: str, prompt_text: str, sources: list[str]) -> list[dict[str, str]]:
    template = read_worker_template(task_type)
    source_block = "\n".join(f"- {source}" for source in sources) if sources else "- None"
    source_excerpts = build_source_excerpts(sources)
    user_prompt = (
        f"Task type: {task_type}\n\n"
        f"Sources:\n{source_block}\n\n"
        f"Source excerpts:\n{source_excerpts}\n\n"
        f"Task:\n{prompt_text}\n"
    )
    return [
        {"role": "system", "content": template},
        {"role": "user", "content": user_prompt},
    ]


def new_task_record(
    provider: dict[str, str],
    task_type: str,
    title: str,
    prompt_text: str,
    sources: list[str],
) -> dict[str, Any]:
    task_id = f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{slugify(title)}-{uuid.uuid4().hex[:8]}"
    return {
        "task_id": task_id,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "provider": provider["name"],
        "model": provider["model"],
        "task_type": task_type,
        "title": title,
        "input_prompt": redact_secrets(prompt_text),
        "sources": redact_secrets(sources),
        "status": "pending",
    }


def task_path(status: str, task_id: str) -> Path:
    return TASKS_DIR / status / f"{task_id}.json"


def write_task(record: dict[str, Any], status: str) -> Path:
    record = redact_secrets(record)
    record["status"] = status
    record["updated_at"] = utc_now()
    destination = task_path(status, record["task_id"])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return destination


def find_task(status: str, task_id: str) -> Path:
    path = task_path(status, task_id)
    if not path.exists():
        raise DelegationError(f"Task not found: {path}")
    return path


def load_task(status: str, task_id: str) -> dict[str, Any]:
    return json.loads(find_task(status, task_id).read_text(encoding="utf-8"))


def approve_task(task_id: str, reason: str) -> Path:
    record = load_task("completed", task_id)
    record["review"] = {"decision": "approved", "reason": reason, "reviewed_at": utc_now()}
    return write_task(record, "completed")


def reject_task(task_id: str, reason: str) -> Path:
    completed = find_task("completed", task_id)
    record = json.loads(completed.read_text(encoding="utf-8"))
    record["review"] = {"decision": "rejected", "reason": reason, "reviewed_at": utc_now()}
    rejected = write_task(record, "rejected")
    completed.unlink()
    return rejected


def call_chat_completion(
    provider: dict[str, str],
    messages: list[dict[str, str]],
    max_output_tokens: int,
    timeout: int,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": provider["model"],
        "messages": messages,
        "temperature": 0.2,
        provider["token_limit_field"]: max_output_tokens,
    }
    data = json.dumps(payload).encode("utf-8")
    url = provider["base_url"].rstrip("/") + "/chat/completions"
    req = request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {provider['api_key']}",
            "Content-Type": "application/json",
        },
    )
    try:
        with request.urlopen(req, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise DelegationError(f"Provider HTTP {exc.code}: {redact_secrets(detail)}") from exc
    except error.URLError as exc:
        raise DelegationError(f"Provider request failed: {exc.reason}") from exc

    return json.loads(body)


def extract_output_text(response: dict[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return json.dumps(response, ensure_ascii=False, indent=2)
    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content
    return json.dumps(content, ensure_ascii=False, indent=2)
