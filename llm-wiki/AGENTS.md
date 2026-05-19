# LLM-Wiki Agent Rules

This folder is the project knowledge base. Future agents should treat it as the durable memory layer for the Make Money experiment.

## Read Order

1. Read `llm-wiki/wiki/index.md`.
2. Read `llm-wiki/wiki/current-status.md`.
3. Read any linked strategy, protocol, risk, experiment, or raw source notes relevant to the task.
4. Check `llm-wiki/wiki/log.md` for recent decisions.

## Writeback Rules

- Durable findings belong in `llm-wiki/wiki/`.
- Source notes and raw captures belong in `llm-wiki/raw/`.
- Every strategy claim that affects money, safety, or execution needs provenance in `llm-wiki/raw/manifest.md`.
- Append meaningful project activity to `llm-wiki/wiki/log.md`.
- Update `llm-wiki/wiki/index.md` when adding pages.
- Follow the [Manager-First Delegation Protocol](wiki/protocols/manager-first-delegation.md): workers may draft, scan, summarize, test, and risk-check, but Codex/Sesame reviews before durable writeback.

## Safety Rules

- Never store private keys, seed phrases, wallet passwords, keystore files, 2FA secrets, browser sessions, or API credentials in this folder.
- Public wallet addresses may be stored in `llm-wiki/wallets.md`.
- API credentials may only live in ignored local `.env` files when explicitly provided by the user.
- Agents may research, summarize, simulate, and create instructions.
- Agents must not connect wallets, sign transactions, submit transactions, or move funds.
- The user starts with zero initial project capital. Prefer zero-capital and low-capital opportunities first.

## Strategy Quality Bar

Each strategy page must include:

- Summary
- Opportunity class
- Capital requirement
- Time and operational cost
- Risk model
- Execution steps
- Human signing checklist, if any wallet action is involved
- Success criteria
- Exit criteria
- Source links
- Experiment links
