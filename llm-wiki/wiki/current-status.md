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
- Active small-cash strategy: [Micro Cash Sprint](strategies/2026-05-20-micro-cash-sprint.md), targeting 5-20 USDT/USDC-equivalent.
- Latest experiment: [sh1pt Listen Notes PR Draft](experiments/2026-05-20-sh1pt-listennotes-pr-draft.md).
- First execution target: [Tether Template Wallet Verification](experiments/2026-05-20-tether-template-wallet-verification.md), submitted and pending review.
- First deliverable package: [Tether Template Wallet Application Pack v0.1](../../deliverables/tether-template-wallet-application-pack-v0.1/README.md), used for the submitted application.
- Second execution target: [Interledger Open Payments Arazzo Verification](experiments/2026-05-20-interledger-open-payments-arazzo-verification.md), proposal package prepared and not submitted.
- Second deliverable package: [Interledger Open Payments Arazzo Application Pack v0.1](../../deliverables/interledger-open-payments-arazzo-pack-v0.1/README.md).
- Current micro-cash target: `profullstack/sh1pt` small adapter contribution. A local Listen Notes outreach adapter patch is drafted and verified, but not publicly submitted.
- Current external-submission blocker: GitHub CLI identity must be switched to the project identity before opening issues, PRs, or comments on external repositories.
- Active execution subthreads: [Execution Subthreads Protocol](protocols/execution-subthreads.md).
- Active manager rule: [Manager-First Delegation Protocol](protocols/manager-first-delegation.md). Routine research, writing, scans, risk checks, and bounded test work should be delegated before Codex/Sesame implements directly.
- Python environment: `uv` project with ignored `.venv/`, `openai-agents`, and an Agents SDK manager scaffold in `scripts/openai_agent_manager.py`.

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7`: usable through the local Delegation Agent under the non-high-speed-only policy. Its output may include reasoning tags, so public writeback requires manager cleanup.

## Next Actions

1. Switch or confirm GitHub CLI authentication for the project identity before external PR submission.
2. Delegate the next Listen Notes test expansion to Mimo before changing the external worktree again.
3. Delegate Micro Cash Scan Batch 002 to MiniMax before selecting the next target.
4. Submit the local `sh1pt` Listen Notes patch only after the project identity is active and risk checks pass.
5. Wait for Tether's review response and record only non-secret updates.
6. Use the Interledger sponsor questions and eligibility/AI disclosure check before any human submission.
