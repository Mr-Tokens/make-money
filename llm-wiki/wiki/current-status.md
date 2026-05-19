# Current Status

Date: 2026-05-20

## Project State

- Repository: published at https://github.com/Mr-Tokens/make-money on `master`.
- LLM-Wiki: initial skeleton created.
- Delegation Agent: implemented as local scripts under `scripts/` and `delegation/`.
- Wallets: public addresses recorded in `llm-wiki/wallets.md`.
- Initial capital: zero.
- Strategy scope: any lawful, ethical, low-capital path, not limited to onchain activity.
- Marketing system: focused skills installed under `.agents/skills/`, with canonical context in `.agents/product-marketing.md`.
- Active first strategy: [Web3 Builder Reputation Sprint](strategies/2026-05-20-web3-builder-reputation-sprint.md).
- Latest experiment: [Provider Smoke Test](experiments/2026-05-20-provider-smoke.md).
- First execution target: [Tether Template Wallet Verification](experiments/2026-05-20-tether-template-wallet-verification.md).
- First deliverable package: [Tether Template Wallet Application Pack v0.1](../../deliverables/tether-template-wallet-application-pack-v0.1/README.md), now including a public-safe submission form draft.
- Active execution subthreads: [Execution Subthreads Protocol](protocols/execution-subthreads.md).
- Python environment: `uv` project with ignored `.venv/`, `openai-agents`, and an Agents SDK manager scaffold in `scripts/openai_agent_manager.py`.

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7`: usable through the local Delegation Agent under the non-high-speed-only policy. Its output may include reasoning tags, so public writeback requires manager cleanup.

## Next Actions

1. Human review of the Tether Template Wallet Application Pack v0.1 and `submission-form-draft.md`.
2. Human decides whether Tether can receive the project representative identity or requires legal-name submission.
3. Human submits the Tether form if terms, eligibility, and risk boundaries are acceptable.
4. Record the submission date and non-secret evidence if the form is submitted.
5. Keep [Tari bounty verification](../raw/sources/2026-05-20-tari-bounty-verification.md) as a contested backup path; do not execute unless maintainers invite more work.
6. Use [Web3Grants verification](../raw/sources/2026-05-20-web3grants-verification.md) as a research multiplier for the second scan batch.
7. Gradually route routine research, wiki, code, and marketing chores through the [OpenAI Agents SDK Protocol](protocols/openai-agent-sdk.md).
8. Draft the first build-in-public post after either the Tether application is submitted or the project intentionally chooses the next target.
