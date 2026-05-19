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
- Latest experiment: [Opportunity Scan Batch 001](experiments/2026-05-20-opportunity-scan-batch-001.md).
- First execution target: [Tether Template Wallet Verification](experiments/2026-05-20-tether-template-wallet-verification.md).
- First deliverable package: [Tether Template Wallet Application Pack v0.1](../../deliverables/tether-template-wallet-application-pack-v0.1/README.md).
- Active execution subthreads: [Execution Subthreads Protocol](protocols/execution-subthreads.md).
- Python environment: `uv` project with ignored `.venv/`, `openai-agents`, and an Agents SDK manager scaffold in `scripts/openai_agent_manager.py`.

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7`: active MiniMax provider policy uses only the non-high-speed model. It still needs a non-high-speed smoke test.

## Next Actions

1. Run a MiniMax non-high-speed smoke test with `MiniMax-M2.7`.
2. Review the Tether Template Wallet Application Pack v0.1 for human submission.
3. Decide whether to use a dedicated project identity or a human personal identity for Tether contact fields.
4. Keep [Tari bounty verification](../raw/sources/2026-05-20-tari-bounty-verification.md) as a contested backup path; do not execute unless maintainers invite more work.
5. Use [Web3Grants verification](../raw/sources/2026-05-20-web3grants-verification.md) as a research multiplier for the second scan batch.
6. Gradually route routine research, wiki, code, and marketing chores through the [OpenAI Agents SDK Protocol](protocols/openai-agent-sdk.md).
7. Draft the first build-in-public post only after a first deliverable target is chosen.
