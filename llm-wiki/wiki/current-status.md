# Current Status

Date: 2026-05-20

## Project State

- Repository: initialized on `master`.
- LLM-Wiki: initial skeleton created.
- Delegation Agent: implemented as local scripts under `scripts/` and `delegation/`.
- Wallets: public addresses recorded in `llm-wiki/wallets.md`.
- Initial capital: zero.
- Strategy scope: any lawful, ethical, low-capital path, not limited to onchain activity.
- Marketing system: focused skills installed under `.agents/skills/`, with canonical context in `.agents/product-marketing.md`.
- Active first strategy: [Web3 Builder Reputation Sprint](strategies/2026-05-20-web3-builder-reputation-sprint.md).
- Python environment: `uv` project with ignored `.venv/`, `openai-agents`, and an Agents SDK manager scaffold in `scripts/openai_agent_manager.py`.

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7`: active MiniMax provider policy uses only the non-high-speed model. It still needs a non-high-speed smoke test.

## Next Actions

1. Run a MiniMax non-high-speed smoke test with `MiniMax-M2.7`.
2. Use Mimo to scan for at least 10 bounties, grants, hackathons, and public-good contribution opportunities.
3. Rank the top 3 candidates with the [Opportunity Scorecard](templates/opportunity-scorecard.md).
4. Choose the first no-capital deliverable.
5. Gradually route routine research, wiki, code, and marketing chores through the [OpenAI Agents SDK Protocol](protocols/openai-agent-sdk.md).
6. Draft the first build-in-public post only after the first candidate ranking is complete.
