# Delegation Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a lightweight local Delegation Agent that can send bounded research tasks to MiniMax or Mimo, save auditable outputs, and require strategy-lead review before wiki writeback.

**Architecture:** Use Python standard library scripts with a shared helper module. Provider metadata is committed in `delegation/providers.example.json`; real credentials are loaded from ignored `.env`. Task records are JSON files moved through `delegation/tasks/pending`, `delegation/tasks/completed`, and `delegation/tasks/rejected`.

**Tech Stack:** Python 3 standard library (`argparse`, `json`, `pathlib`, `urllib.request`, `unittest`), Markdown docs, git.

---

## File Structure

- Create `scripts/delegation_lib.py`: shared task, provider, redaction, file, and HTTP helpers.
- Create `scripts/delegate_task.py`: CLI for dry-run and real worker calls.
- Create `scripts/review_task.py`: CLI for approving or rejecting completed worker outputs.
- Create `tests/test_delegation_lib.py`: unit tests for redaction, provider resolution, task creation, and review helpers.
- Create `delegation/README.md`: human usage guide and safety rules.
- Create `delegation/providers.example.json`: committed provider metadata without secrets.
- Create `delegation/prompts/worker-research.md`: research-worker contract.
- Create `delegation/prompts/worker-summary.md`: summary-worker contract.
- Create `delegation/prompts/worker-risk-check.md`: risk-check-worker contract.
- Create `delegation/tasks/pending/.gitkeep`, `delegation/tasks/completed/.gitkeep`, `delegation/tasks/rejected/.gitkeep`: keep task directories in git.
- Modify `.env.example`: include the non-high-speed MiniMax model only.

---

### Task 1: Test Secret Redaction And Provider Resolution

**Files:**
- Create: `tests/test_delegation_lib.py`
- Create later: `scripts/delegation_lib.py`

- [ ] **Step 1: Write failing tests for secret redaction and provider resolution**

Add this initial test file:

```python
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from delegation_lib import (
    load_env_file,
    load_providers,
    redact_secrets,
    resolve_provider,
)


class DelegationLibTests(unittest.TestCase):
    def test_redact_secrets_masks_known_token_shapes(self):
        text = (
            "minimax sk-test-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
            "mimo tp-test-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb "
            "bearer Authorization: Bearer secret-token-value"
        )

        redacted = redact_secrets(text)

        self.assertNotIn("sk-test-aaaaaaaa", redacted)
        self.assertNotIn("tp-test-bbbbbbbb", redacted)
        self.assertNotIn("secret-token-value", redacted)
        self.assertIn("[REDACTED_TOKEN]", redacted)

    def test_load_env_file_reads_simple_key_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            env_path.write_text(
                "MINIMAX_API_KEY = example-local-key\n"
                "MIMO_BASE_URL='https://token-plan-sgp.xiaomimimo.com/v1'\n"
                "# comment\n",
                encoding="utf-8",
            )

            values = load_env_file(env_path)

        self.assertEqual(values["MINIMAX_API_KEY"], "example-local-key")
        self.assertEqual(values["MIMO_BASE_URL"], "https://token-plan-sgp.xiaomimimo.com/v1")

    def test_resolve_provider_uses_env_over_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            providers_path = Path(tmp) / "providers.example.json"
            providers_path.write_text(
                json.dumps(
                    {
                        "mimo": {
                            "base_url_env": "MIMO_BASE_URL",
                            "api_key_env": "MIMO_API_KEY",
                            "model_env": "MIMO_MODEL",
                            "default_base_url": "https://api.xiaomimimo.com/v1",
                            "default_model": "mimo-v2.5-pro",
                            "token_limit_field": "max_completion_tokens",
                        }
                    }
                ),
                encoding="utf-8",
            )

            providers = load_providers(providers_path)
            provider = resolve_provider(
                "mimo",
                providers,
                {
                    "MIMO_BASE_URL": "https://token-plan-sgp.xiaomimimo.com/v1",
                    "MIMO_API_KEY": "local-key",
                    "MIMO_MODEL": "mimo-v2.5-pro",
                },
                require_key=True,
            )

        self.assertEqual(provider["base_url"], "https://token-plan-sgp.xiaomimimo.com/v1")
        self.assertEqual(provider["api_key"], "local-key")
        self.assertEqual(provider["model"], "mimo-v2.5-pro")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: FAIL or import error because `scripts/delegation_lib.py` does not exist yet.

- [ ] **Step 3: Commit after the red-green loop for Task 1**

After Task 2 makes these tests pass, commit the library and tests together:

```powershell
git add -- tests/test_delegation_lib.py scripts/delegation_lib.py
git commit -m "Add delegation provider helpers"
```

---

### Task 2: Implement Shared Delegation Library

**Files:**
- Create: `scripts/delegation_lib.py`
- Test: `tests/test_delegation_lib.py`

- [ ] **Step 1: Implement the minimal shared helper module**

Create `scripts/delegation_lib.py`:

```python
from __future__ import annotations

import json
import os
import re
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request

ROOT = Path(__file__).resolve().parents[1]
DELEGATION_DIR = ROOT / "delegation"
TASKS_DIR = DELEGATION_DIR / "tasks"
PROMPTS_DIR = DELEGATION_DIR / "prompts"
PROVIDERS_PATH = DELEGATION_DIR / "providers.example.json"
ENV_PATH = ROOT / ".env"

TASK_TYPES = {"research", "summary", "risk-check"}
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


def build_messages(task_type: str, prompt_text: str, sources: list[str]) -> list[dict[str, str]]:
    template = read_worker_template(task_type)
    source_block = "\n".join(f"- {source}" for source in sources) if sources else "- None"
    user_prompt = (
        f"Task type: {task_type}\n\n"
        f"Sources:\n{source_block}\n\n"
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
```

- [ ] **Step 2: Run tests for Task 1**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: PASS for the three tests.

---

### Task 3: Add Provider Metadata, Prompt Templates, And Env Template

**Files:**
- Create: `delegation/providers.example.json`
- Create: `delegation/prompts/worker-research.md`
- Create: `delegation/prompts/worker-summary.md`
- Create: `delegation/prompts/worker-risk-check.md`
- Create: `delegation/tasks/pending/.gitkeep`
- Create: `delegation/tasks/completed/.gitkeep`
- Create: `delegation/tasks/rejected/.gitkeep`
- Modify: `.env.example`

- [ ] **Step 1: Create provider metadata without secrets**

Create `delegation/providers.example.json`:

```json
{
  "minimax": {
    "base_url_env": "MINIMAX_BASE_URL",
    "api_key_env": "MINIMAX_API_KEY",
    "model_env": "MINIMAX_MODEL",
    "default_base_url": "https://api.minimaxi.com/v1",
    "default_model": "MiniMax-M2.7",
    "token_limit_field": "max_tokens"
  },
  "mimo": {
    "base_url_env": "MIMO_BASE_URL",
    "api_key_env": "MIMO_API_KEY",
    "model_env": "MIMO_MODEL",
    "default_base_url": "https://api.xiaomimimo.com/v1",
    "default_model": "mimo-v2.5-pro",
    "token_limit_field": "max_completion_tokens"
  }
}
```

- [ ] **Step 2: Add worker prompt templates**

Create `delegation/prompts/worker-research.md`:

```markdown
You are a bounded research worker for the Make Money project.

Rules:
- Do not request or process secrets, private keys, seed phrases, wallet passwords, or API keys.
- Do not recommend wallet signing or fund movement as a completed action.
- Treat profit as uncertain.
- Prefer verifiable facts and cite sources passed in the prompt.

Return Markdown with these headings:
## Answer
## Sources Used
## Confidence
## Missing Information
## Money Or Wallet Risks
## Suggested Next Questions
```

Create `delegation/prompts/worker-summary.md`:

```markdown
You are a bounded summarization worker for the Make Money LLM-Wiki.

Rules:
- Summarize only the material provided in the task.
- Mark uncertain claims clearly.
- Do not invent source URLs.
- Do not process secrets, private keys, seed phrases, wallet passwords, or API keys.

Return Markdown with these headings:
## Short Summary
## Key Facts
## Entities And Protocols
## Claims Needing Verification
## Suggested Wiki Updates
```

Create `delegation/prompts/worker-risk-check.md`:

```markdown
You are a bounded risk-check worker for crypto strategy research.

Rules:
- Focus on failure modes, wallet safety, contract risk, operational risk, and hidden costs.
- Do not say an opportunity is safe without listing evidence and assumptions.
- Do not request or process secrets, private keys, seed phrases, wallet passwords, or API keys.
- Do not produce transaction payloads or signing instructions.

Return Markdown with these headings:
## Risk Categories
## Likely Failure Modes
## Required Human Checks
## Do-Not-Proceed Conditions
## Safer Alternatives
```

- [ ] **Step 3: Add task directories**

Create empty `.gitkeep` files:

```text
delegation/tasks/pending/.gitkeep
delegation/tasks/completed/.gitkeep
delegation/tasks/rejected/.gitkeep
```

- [ ] **Step 4: Update `.env.example`**

Ensure `.env.example` includes:

```text
MINIMAX_MODEL=MiniMax-M2.7
```

- [ ] **Step 5: Run tests**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: PASS.

- [ ] **Step 6: Commit provider and prompt scaffolding**

Run:

```powershell
git add -- delegation .env.example
git commit -m "Add delegation provider and prompt templates"
```

---

### Task 4: Implement Delegate CLI With Dry Run

**Files:**
- Create: `scripts/delegate_task.py`
- Modify: `tests/test_delegation_lib.py`

- [ ] **Step 1: Add tests for task record writing and redaction**

Append to `DelegationLibTests` in `tests/test_delegation_lib.py`:

```python
    def test_write_task_redacts_prompt_and_sources(self):
        import delegation_lib

        with tempfile.TemporaryDirectory() as tmp:
            old_tasks_dir = delegation_lib.TASKS_DIR
            delegation_lib.TASKS_DIR = Path(tmp) / "tasks"
            try:
                record = {
                    "task_id": "task-1",
                    "created_at": "2026-05-20T00:00:00+00:00",
                    "updated_at": "2026-05-20T00:00:00+00:00",
                    "provider": "mimo",
                    "model": "mimo-v2.5-pro",
                    "task_type": "research",
                    "title": "Secret test",
                    "input_prompt": "token sk-test-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sources": ["api-key: tp-test-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"],
                    "status": "pending",
                }

                path = delegation_lib.write_task(record, "pending")
                saved = path.read_text(encoding="utf-8")
            finally:
                delegation_lib.TASKS_DIR = old_tasks_dir

        self.assertIn("[REDACTED_TOKEN]", saved)
        self.assertNotIn("sk-test-aaaaaaaa", saved)
        self.assertNotIn("tp-test-bbbbbbbb", saved)
```

- [ ] **Step 2: Run test to verify current behavior**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: PASS if Task 2 already redacts recursively, otherwise FAIL and fix `write_task`.

- [ ] **Step 3: Implement `scripts/delegate_task.py`**

Create `scripts/delegate_task.py`:

```python
from __future__ import annotations

import argparse
import json
import sys

from delegation_lib import (
    DelegationError,
    build_messages,
    call_chat_completion,
    extract_output_text,
    load_providers,
    merged_env,
    new_task_record,
    read_prompt_text,
    resolve_provider,
    write_task,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Delegate a bounded task to a worker model.")
    parser.add_argument("--provider", required=True, choices=["minimax", "mimo"])
    parser.add_argument("--type", required=True, choices=["research", "summary", "risk-check"])
    parser.add_argument("--title", required=True)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-output-tokens", type=int, default=1200)
    parser.add_argument("--timeout", type=int, default=120)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        env = merged_env()
        providers = load_providers()
        provider = resolve_provider(args.provider, providers, env, require_key=not args.dry_run)
        prompt_text = read_prompt_text(args.prompt, args.prompt_file)
        messages = build_messages(args.type, prompt_text, args.source)
        record = new_task_record(provider, args.type, args.title, prompt_text, args.source)
        pending_path = write_task(record, "pending")

        if args.dry_run:
            print(f"Dry run task saved: {pending_path}")
            return 0

        response = call_chat_completion(provider, messages, args.max_output_tokens, args.timeout)
        record["worker_output"] = extract_output_text(response)
        record["raw_response"] = response
        completed_path = write_task(record, "completed")
        pending_path.unlink(missing_ok=True)
        print(f"Completed task saved: {completed_path}")
        return 0
    except DelegationError as exc:
        print(f"delegation error: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"json error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run dry-run smoke command**

Run:

```powershell
python scripts/delegate_task.py --provider mimo --type research --title "Dry run" --prompt "Summarize the safety rules for this project." --dry-run
```

Expected: command exits 0 and prints `Dry run task saved: ...delegation\tasks\pending\...json`.

- [ ] **Step 5: Inspect the pending dry-run file**

Run:

```powershell
Get-ChildItem delegation/tasks/pending -Filter *.json | Select-Object -First 1 | Get-Content
```

Expected: JSON task record contains no API keys and has status `pending`.

- [ ] **Step 6: Commit delegate CLI**

Run:

```powershell
git add -- scripts/delegate_task.py tests/test_delegation_lib.py delegation/tasks/pending
git commit -m "Add delegation task CLI"
```

---

### Task 5: Implement Review CLI

**Files:**
- Create: `scripts/review_task.py`
- Modify: `tests/test_delegation_lib.py`

- [ ] **Step 1: Add tests for approve and reject helpers**

Append to `DelegationLibTests`:

```python
    def test_approve_and_reject_task_update_review_state(self):
        import delegation_lib

        with tempfile.TemporaryDirectory() as tmp:
            old_tasks_dir = delegation_lib.TASKS_DIR
            delegation_lib.TASKS_DIR = Path(tmp) / "tasks"
            try:
                record = {
                    "task_id": "task-2",
                    "created_at": "2026-05-20T00:00:00+00:00",
                    "updated_at": "2026-05-20T00:00:00+00:00",
                    "provider": "minimax",
                    "model": "MiniMax-M2.7",
                    "task_type": "summary",
                    "title": "Review test",
                    "input_prompt": "hello",
                    "sources": [],
                    "worker_output": "result",
                    "status": "completed",
                }
                delegation_lib.write_task(record, "completed")

                approved_path = delegation_lib.approve_task("task-2", "looks useful")
                approved = json.loads(approved_path.read_text(encoding="utf-8"))

                record["task_id"] = "task-3"
                delegation_lib.write_task(record, "completed")
                rejected_path = delegation_lib.reject_task("task-3", "unsupported claim")
                rejected = json.loads(rejected_path.read_text(encoding="utf-8"))
            finally:
                delegation_lib.TASKS_DIR = old_tasks_dir

        self.assertEqual(approved["status"], "completed")
        self.assertEqual(approved["review"]["decision"], "approved")
        self.assertEqual(rejected["status"], "rejected")
        self.assertEqual(rejected["review"]["decision"], "rejected")
```

- [ ] **Step 2: Run tests**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: PASS if Task 2 helpers are correct.

- [ ] **Step 3: Implement `scripts/review_task.py`**

Create `scripts/review_task.py`:

```python
from __future__ import annotations

import argparse
import sys

from delegation_lib import DelegationError, approve_task, reject_task


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review a completed delegated task.")
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--decision", required=True, choices=["approved", "rejected"])
    parser.add_argument("--reason", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.decision == "approved":
            path = approve_task(args.task_id, args.reason)
        else:
            path = reject_task(args.task_id, args.reason)
        print(f"Review saved: {path}")
        return 0
    except DelegationError as exc:
        print(f"review error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run review tests**

Run:

```powershell
python -m unittest tests/test_delegation_lib.py -v
```

Expected: PASS.

- [ ] **Step 5: Commit review CLI**

Run:

```powershell
git add -- scripts/review_task.py tests/test_delegation_lib.py
git commit -m "Add delegation review CLI"
```

---

### Task 6: Add Delegation README And Final Verification

**Files:**
- Create: `delegation/README.md`
- Modify if needed: `docs/superpowers/specs/2026-05-20-delegation-agent-design.md`

- [ ] **Step 1: Write user-facing README**

Create `delegation/README.md`:

```markdown
# Delegation Agent

This directory contains the lightweight local task delegation layer for the Make Money project.

## Safety Rules

- Real provider credentials go only in `.env`.
- `.env` is ignored by git.
- Do not paste API keys, wallet secrets, seed phrases, or private keys into prompts.
- Worker models may research, summarize, and risk-check.
- Worker models must not connect wallets, sign transactions, prepare transactions, or write directly to `llm-wiki/`.
- Approved task output still needs strategy-lead review before wiki writeback.

## Setup

Copy `.env.example` to `.env` and enter rotated provider credentials:

```text
MINIMAX_API_KEY=
MIMO_API_KEY=
```

If Mimo Token Plan gives a cluster-specific URL, set `MIMO_BASE_URL` to that value.

## Dry Run

```powershell
python scripts/delegate_task.py --provider mimo --type research --title "Dry run" --prompt "Summarize the safety rules for this project." --dry-run
```

## Run A Worker Task

```powershell
python scripts/delegate_task.py --provider minimax --type summary --title "Protocol summary" --prompt "Summarize the provided source note." --source "llm-wiki/raw/sources/example.md"
```

## Review A Task

```powershell
python scripts/review_task.py --task-id "TASK_ID" --decision approved --reason "Useful and source-backed"
python scripts/review_task.py --task-id "TASK_ID" --decision rejected --reason "Unsupported claims"
```
```

- [ ] **Step 2: Run all unit tests**

Run:

```powershell
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 3: Verify secret ignore rules**

Run:

```powershell
git check-ignore -v .env .env.local
```

Expected: `.gitignore` rules match both files.

- [ ] **Step 4: Search for leaked token prefixes**

Run:

```powershell
rg -n "sk-cp-|tp-ck" .
rg -n "MINIMAX_API_KEY=.+|MIMO_API_KEY=.+" --glob "!docs/superpowers/plans/*.md" .
```

Expected: no matches for real token material or non-empty committed API key values.

- [ ] **Step 5: Commit docs and final verification fixes**

Run:

```powershell
git add -- delegation/README.md
git commit -m "Document delegation workflow"
```

---

## Self-Review Checklist

- Spec coverage: provider metadata, `.env` secret handling, task lifecycle, worker prompts, dry-run, review, and no-wallet-action constraints are covered.
- Placeholders: no task uses placeholder markers or unspecified future work.
- Type consistency: provider keys, task status values, and task type names match across tests, scripts, and docs.
- Verification: unit tests, dry-run, git ignore check, and token-pattern search are required before completion.
