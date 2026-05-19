from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".agents"
SKILLS_DIR = AGENTS_DIR / "skills"
PRODUCT_MARKETING_PATH = AGENTS_DIR / "product-marketing.md"
LLM_WIKI_DIR = ROOT / "llm-wiki"
SAFE_SANDBOX_DIRS = {
    "llm-wiki": LLM_WIKI_DIR,
    "skills": SKILLS_DIR,
    "docs": ROOT / "docs",
    "scripts": ROOT / "scripts",
    "tests": ROOT / "tests",
}
SAFE_SANDBOX_FILES = {
    "AGENTS.md": ROOT / "AGENTS.md",
    ".env.example": ROOT / ".env.example",
    "pyproject.toml": ROOT / "pyproject.toml",
    "uv.lock": ROOT / "uv.lock",
    "skills-lock.json": ROOT / "skills-lock.json",
    "product-marketing.md": PRODUCT_MARKETING_PATH,
    "delegation-providers.example.json": ROOT / "delegation" / "providers.example.json",
}


@dataclass(frozen=True)
class ProjectSkill:
    name: str
    description: str
    path: str


def _read_text_if_exists(path: Path, max_chars: int | None = None) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    return text if max_chars is None else text[:max_chars]


def _frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def load_project_skills(skills_dir: Path = SKILLS_DIR) -> list[ProjectSkill]:
    if not skills_dir.exists():
        return []

    skills: list[ProjectSkill] = []
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_path = skill_dir / "SKILL.md"
        text = _read_text_if_exists(skill_path)
        if not text:
            continue
        name = _frontmatter_value(text, "name") or skill_dir.name
        description = _frontmatter_value(text, "description")
        skills.append(
            ProjectSkill(
                name=name,
                description=description,
                path=str(skill_path.relative_to(ROOT)),
            )
        )
    return skills


def _skill_path(skill_name: str) -> Path:
    normalized = re.sub(r"[^a-zA-Z0-9_-]", "", skill_name.strip())
    if not normalized or normalized != skill_name.strip():
        raise ValueError(f"Invalid skill name: {skill_name!r}")

    skill_path = SKILLS_DIR / normalized / "SKILL.md"
    try:
        resolved = skill_path.resolve()
        skills_root = SKILLS_DIR.resolve()
    except FileNotFoundError as exc:
        raise ValueError(f"Unknown project skill: {skill_name}") from exc
    if not resolved.is_relative_to(skills_root) or not resolved.exists():
        raise ValueError(f"Unknown project skill: {skill_name}")
    return resolved


def read_project_skill_text(skill_name: str) -> str:
    return _skill_path(skill_name).read_text(encoding="utf-8")


def read_product_marketing_context() -> str:
    return _read_text_if_exists(PRODUCT_MARKETING_PATH) or "No product marketing context exists yet."


def _build_project_context_tools():
    from agents import function_tool

    @function_tool
    def list_project_skills() -> str:
        """List installed Make Money project skills and their local paths."""
        return json.dumps([asdict(skill) for skill in load_project_skills()], ensure_ascii=False)

    @function_tool
    def read_project_skill(skill_name: str) -> str:
        """Read one installed project skill by exact skill name."""
        return read_project_skill_text(skill_name)

    @function_tool
    def read_project_marketing_context() -> str:
        """Read the canonical Make Money product marketing context."""
        return read_product_marketing_context()

    return [list_project_skills, read_project_skill, read_project_marketing_context]


def _format_skill_catalog(skills: Iterable[ProjectSkill]) -> str:
    lines = []
    for skill in skills:
        description = skill.description or "No description captured."
        lines.append(f"- `{skill.name}` ({skill.path}): {description}")
    return "\n".join(lines) or "- No project skills installed yet."


def build_manager_instructions(skills: list[ProjectSkill] | None = None) -> str:
    skills = load_project_skills() if skills is None else skills
    product_context = _read_text_if_exists(PRODUCT_MARKETING_PATH, max_chars=5000)
    product_context_block = product_context or "No product marketing context exists yet."

    return f"""You are the Make Money Manager Agent.

You are responsible for strategy, delegation, review, and evidence discipline. Delegate focused work to specialist agents instead of doing every task yourself. Keep final judgment with the manager.

Project boundaries:
- Read and obey `AGENTS.md` and `llm-wiki/AGENTS.md` before changing project files.
- Durable knowledge belongs in `llm-wiki/`; raw sources belong under `llm-wiki/raw/` when practical.
- Test-created runtime artifacts belong under `tests/artifacts/`.
- Python `__pycache__` directories are acceptable if ignored by git.
- Secrets belong only in ignored local files such as `.env` or `secret/`.
- You must not connect wallets, sign transactions, submit transactions, move funds, request private keys, or request seed phrases.
- Public claims must point to source notes, wiki pages, submissions, artifacts, or wallet evidence.
- Keep the repository tidy: prefer small committed files, ignored runtime output, and no root-level scratch files.

Delegation posture:
- Use specialist agents for research, LLM-Wiki maintenance, code maintenance, marketing, and risk checks.
- Improve worker instructions after each run when you discover sharper role boundaries.
- Review worker output before writing durable conclusions into the wiki.
- Reject unsupported claims, unsafe wallet actions, and hype that lacks evidence.

Project Skills:
Project skills live under `.agents/skills`. Read the relevant `SKILL.md` before applying a skill.
{_format_skill_catalog(skills)}

Product marketing context excerpt:
{product_context_block}
"""


def build_worker_instructions(
    role: str,
    skill_names: Iterable[str] = (),
    include_product_context: bool = False,
) -> str:
    selected = {name for name in skill_names}
    skills = [skill for skill in load_project_skills() if skill.name in selected]
    skill_block = _format_skill_catalog(skills)
    product_context_block = (
        f"\nCanonical product marketing context:\n{read_product_marketing_context()}\n"
        if include_product_context
        else ""
    )
    return f"""You are a specialist worker for the Make Money project.

Role: {role}

Work only inside the requested scope. Prefer precise, source-backed output over broad exploration. Do not handle secrets, private keys, wallet signing, or transaction submission. If you produce files, keep durable knowledge in `llm-wiki/` and runtime/test artifacts in `tests/artifacts/`.

Relevant project skills:
{skill_block}
{product_context_block}
"""


def build_worker_agent(
    name: str,
    role: str,
    skill_names: Iterable[str] = (),
    model: str | None = None,
    include_product_context: bool = False,
):
    from agents import Agent

    return Agent(
        name=name,
        instructions=build_worker_instructions(
            role=role,
            skill_names=skill_names,
            include_product_context=include_product_context,
        ),
        model=model,
        tools=_build_project_context_tools(),
    )


def build_manager_agent(model: str | None = None):
    from agents import Agent

    research_worker = build_worker_agent(
        "Opportunity Research Worker",
        "Find, summarize, and risk-filter zero-capital opportunities with source URLs.",
        skill_names=("content-strategy",),
        model=model,
    )
    wiki_worker = build_worker_agent(
        "LLM-Wiki Maintainer",
        "Maintain source-backed LLM-Wiki pages and keep provenance clear.",
        skill_names=("content-strategy", "ai-seo"),
        model=model,
    )
    code_worker = build_worker_agent(
        "Code Maintenance Worker",
        "Make small, tested repository changes while keeping artifacts contained.",
        skill_names=(),
        model=model,
    )
    marketing_worker = build_worker_agent(
        "Marketing Worker",
        "Turn verified project evidence into positioning, launch, social, and community drafts.",
        skill_names=("product-marketing", "launch", "social", "community-marketing", "free-tools"),
        model=model,
        include_product_context=True,
    )
    writing_worker = build_worker_agent(
        "Owner-Facing Writing Worker",
        "Polish reader-facing Chinese and English project updates with a light social-media feel and minimal internal detail.",
        skill_names=("product-marketing", "social", "launch"),
        model=model,
        include_product_context=True,
    )

    return Agent(
        name="Make Money Manager",
        instructions=build_manager_instructions(),
        model=model,
        tools=[
            *_build_project_context_tools(),
            research_worker.as_tool(
                tool_name="opportunity_research_worker",
                tool_description="Researches and risk-filters current zero-capital opportunities.",
            ),
            wiki_worker.as_tool(
                tool_name="llm_wiki_maintainer",
                tool_description="Drafts and updates LLM-Wiki pages with provenance and concise structure.",
            ),
            code_worker.as_tool(
                tool_name="code_maintenance_worker",
                tool_description="Implements small repository changes and reports verification commands.",
            ),
            marketing_worker.as_tool(
                tool_name="marketing_worker",
                tool_description="Creates evidence-backed positioning, launch, social, community, and free-tool drafts.",
            ),
            writing_worker.as_tool(
                tool_name="owner_facing_writing_worker",
                tool_description="Polishes owner-facing README, updates, and social-style project explanations.",
            ),
        ],
    )


def _resolve_safe_sandbox_path(path: Path) -> Path:
    resolved = path.resolve()
    root = ROOT.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"Sandbox path escapes project root: {path}")
    forbidden_names = {".env", "secret", ".venv"}
    if any(part in forbidden_names for part in resolved.relative_to(root).parts):
        raise ValueError(f"Sandbox path exposes local-only secret/runtime state: {path}")
    return resolved


def safe_sandbox_sources() -> dict[str, Path]:
    entries = {}
    for name, path in SAFE_SANDBOX_DIRS.items():
        if path.exists():
            entries[name] = _resolve_safe_sandbox_path(path)
    for name, path in SAFE_SANDBOX_FILES.items():
        if path.exists():
            entries[name] = _resolve_safe_sandbox_path(path)
    return entries


def build_sandbox_manifest():
    from agents.sandbox import Manifest
    from agents.sandbox.entries import LocalDir, LocalFile

    entries = {}
    for name, path in safe_sandbox_sources().items():
        entries[name] = LocalDir(src=path) if path.is_dir() else LocalFile(src=path)
    return Manifest(entries=entries)


def build_sandbox_manager_agent(model: str | None = None):
    from agents.sandbox import SandboxAgent
    from agents.sandbox.capabilities import Capabilities, LocalDirLazySkillSource, Skills
    from agents.sandbox.entries import LocalDir

    return SandboxAgent(
        name="Make Money Sandbox Manager",
        model=model,
        instructions=build_manager_instructions(),
        default_manifest=build_sandbox_manifest(),
        capabilities=Capabilities.default()
        + [
            Skills(
                lazy_from=LocalDirLazySkillSource(
                    source=LocalDir(src=SKILLS_DIR),
                )
            )
        ],
    )


def configure_agents_runtime() -> None:
    from agents import set_default_openai_api, set_tracing_disabled

    default_api = os.environ.get("OPENAI_AGENTS_DEFAULT_API")
    if default_api in {"responses", "chat_completions"}:
        set_default_openai_api(default_api)

    tracing_enabled = os.environ.get("OPENAI_AGENTS_ENABLE_TRACING") == "1"
    set_tracing_disabled(not tracing_enabled)


def inspect_project() -> dict[str, object]:
    skills = load_project_skills()
    return {
        "root": str(ROOT),
        "venv": str(ROOT / ".venv"),
        "llm_wiki": str(LLM_WIKI_DIR),
        "skills_dir": str(SKILLS_DIR),
        "skill_count": len(skills),
        "skills": [asdict(skill) for skill in skills],
        "manager_agent": "Make Money Manager",
        "worker_agents": [
            "Opportunity Research Worker",
            "LLM-Wiki Maintainer",
            "Code Maintenance Worker",
            "Marketing Worker",
            "Owner-Facing Writing Worker",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect and build the Make Money OpenAI manager agent.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("inspect", help="Print project agent configuration as JSON.")
    subparsers.add_parser("instructions", help="Print the manager system instructions.")
    subparsers.add_parser("dry-run", help="Import the SDK and build the manager agent without calling any model.")
    args = parser.parse_args(argv)

    if args.command == "inspect":
        print(json.dumps(inspect_project(), indent=2, ensure_ascii=False))
        return 0
    if args.command == "instructions":
        print(build_manager_instructions())
        return 0
    if args.command == "dry-run":
        configure_agents_runtime()
        agent = build_manager_agent(model=os.environ.get("OPENAI_MANAGER_MODEL"))
        print(json.dumps({"agent": agent.name, "tool_count": len(agent.tools)}, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
