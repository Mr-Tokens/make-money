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

## Credentials

The user has explicitly allowed locally using provider API credentials. Credentials must only be stored in ignored `.env` files. They must not be written to `llm-wiki/`, raw source notes, task JSON, logs, or committed files.

## Worker Providers

- Mimo `mimo-v2.5-pro`: usable through the local Delegation Agent.
- MiniMax `MiniMax-M2.7-highspeed`: provider returned HTTP 429 during smoke test. Retry after `2026-05-20T05:00:00+08:00`.

## Next Actions

1. Retry MiniMax after the provider reset time.
2. Use Mimo to scan for at least 10 bounties, grants, hackathons, and public-good contribution opportunities.
3. Rank the top 3 candidates with the [Opportunity Scorecard](templates/opportunity-scorecard.md).
4. Choose the first no-capital deliverable.
5. Draft the first build-in-public post only after the first candidate ranking is complete.
