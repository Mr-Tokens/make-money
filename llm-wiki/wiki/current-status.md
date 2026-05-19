# Current Status

Date: 2026-05-20

## Project State

- Repository: initialized on `master`.
- LLM-Wiki: initial skeleton created.
- Delegation Agent: implemented as local scripts under `scripts/` and `delegation/`.
- Wallets: public addresses recorded in `llm-wiki/wallets.md`.
- Initial capital: zero.
- Strategy scope: any lawful, ethical, low-capital path, not limited to onchain activity.

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7-highspeed`: provider returned HTTP 429 during smoke test. Retry after `2026-05-20T05:00:00+08:00`.

## Next Actions

1. Retry MiniMax after the provider reset time.
2. Create the first zero-capital strategy pages.
3. Use Mimo to scan for bounties, grants, and airdrop/testnet opportunities.
4. Record every durable finding in this wiki.
