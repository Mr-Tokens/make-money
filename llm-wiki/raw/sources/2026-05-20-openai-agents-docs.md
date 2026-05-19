# OpenAI Agents Docs

URL: https://developers.openai.com/api/docs/guides/agents
Related: https://developers.openai.com/api/docs/guides/agents/orchestration
Python SDK: https://openai.github.io/openai-agents-python/quickstart/
Models: https://openai.github.io/openai-agents-python/models/
Sandbox Skills: https://openai.github.io/openai-agents-python/sandbox_agents/
Date accessed: 2026-05-20

## Source Note

OpenAI's agent guidance supports manager/worker orchestration. For this project, Codex remains the strategy lead and external OpenAI-compatible models are bounded workers called through local scripts.

The Python Agents SDK quickstart documents creating a virtual environment and installing the SDK with `pip install openai-agents` or `uv add openai-agents`.

The Agents page documents two broad multi-agent patterns:

- Manager agents that invoke specialist agents exposed as tools.
- Handoffs where another agent takes over the conversation.

The Models page says OpenAI-only workflows should prefer the default Responses path, while OpenAI-compatible non-OpenAI providers often need Chat Completions or custom model/provider configuration. It also warns that provider feature differences matter.

The Sandbox Agents quickstart shows local repo staging and lazy loading of local Skills from a host directory via `LocalDirLazySkillSource`.

## Project Implications

- Use worker calls as auditable tool-like steps.
- Keep final strategy judgment with the strategy lead.
- Require review before wiki writeback or any execution recommendation.
- Use `uv` and commit `pyproject.toml` plus `uv.lock`.
- Keep `.venv/` ignored.
- Provide a manager agent with specialist workers as tools.
- Let future Sandbox Agent workflows load `.agents/skills` from the project folder.
- Disable tracing by default unless explicitly enabled, especially when routing through non-OpenAI-compatible endpoints.
