# OpenAI Agents SDK Protocol

Status: active
Date: 2026-05-20

## Purpose

This project will use the OpenAI Agents SDK as the long-term orchestration layer. Codex remains the strategy lead, but routine work should move toward a manager agent that delegates to specialist workers.

## Local Environment

- Python dependencies are managed with `uv`.
- The virtual environment is `.venv/` and is ignored by git.
- Dependency state is tracked in `pyproject.toml` and `uv.lock`.
- Current SDK dependency: `openai-agents`.
- `httpx[socks]` is included because this workstation may route model calls through a SOCKS proxy.

Useful commands:

```powershell
uv sync
uv run python scripts/openai_agent_manager.py inspect
uv run python scripts/openai_agent_manager.py dry-run
```

## Manager Scaffold

Entry point:

```text
scripts/openai_agent_manager.py
```

The scaffold provides:

- `load_project_skills()`: reads installed project skills from `.agents/skills/*/SKILL.md`.
- `build_manager_instructions()`: builds the manager system prompt from project rules, skills, and product-marketing context.
- `build_manager_agent()`: creates a manager agent with specialist agents exposed as tools, plus restricted tools for listing skills, reading one installed skill, and reading product-marketing context.
- `build_sandbox_manager_agent()`: prepares a Sandbox Agent that can lazily load local project skills.
- `safe_sandbox_sources()`: defines a whitelist of host paths that may be exposed to Sandbox Agents.
- `inspect` and `dry-run` CLI commands that do not call a model.

## Worker Roles

| Worker | Responsibility |
|--------|----------------|
| Opportunity Research Worker | Finds, summarizes, and risk-filters zero-capital opportunities. |
| LLM-Wiki Maintainer | Drafts and updates source-backed wiki pages. |
| Code Maintenance Worker | Makes small, tested repo changes while keeping artifacts contained. |
| Marketing Worker | Turns verified evidence into positioning, launch, social, community, and free-tool drafts. |
| Owner-Facing Writing Worker | Polishes README and progress updates so the project owner can read them like light public updates instead of internal engineering notes. |

## Skills

Project skills are committed under `.agents/skills/`. The manager prompt lists them, and future Sandbox Agent workflows can load them from the project folder.

Rule: read the relevant `SKILL.md` before applying a skill. The ordinary manager and workers use restricted project-context tools; they do not get arbitrary filesystem access. Skills supplement project rules; they do not override wallet safety, credential handling, or documentation boundaries.

## Safety Defaults

- Real API keys remain only in ignored `.env` files.
- Tracing is disabled by default unless `OPENAI_AGENTS_ENABLE_TRACING=1`.
- For OpenAI-compatible non-OpenAI endpoints, set `OPENAI_AGENTS_DEFAULT_API=chat_completions` when the provider does not support Responses.
- Agents must not connect wallets, request private keys, sign transactions, submit transactions, or move funds.
- Worker output requires manager review before durable wiki writeback.
- Sandbox Agents must not mount the whole repository. Use the safe source whitelist, which excludes `.env`, `secret.md/`, `.venv/`, and the project root itself.

## Cleanliness Rules

- `.venv/`, `.env`, ignored task JSON, `secret.md/`, and Python caches stay untracked.
- `scripts/__pycache__/` is acceptable local cache noise and is ignored.
- Do not create root-level scratch files.
- Test runtime output belongs under `tests/artifacts/`.

## Reuse Policy

The manager scaffold and worker roles are reusable project assets. Future agents should adjust prompts and roles in place instead of creating one-off orchestration scripts for every task.

The `writing` worker type in the local Delegation Agent is the preferred route for Chinese README polish, owner-facing updates, launch copy, and social-style status text. Codex still reviews the output before committing it.

## Next Integration Steps

1. Add a real `run` command after choosing the first OpenAI or OpenAI-compatible runtime model.
2. Route Mimo and non-high-speed `MiniMax-M2.7` through Agents SDK only after validating provider tool/JSON behavior.
3. Give each worker a sharper prompt based on actual failed or successful tasks.
4. Consider Sandbox Agent runs for code and wiki work once Windows/local sandbox support is verified for this workstation.
