# Make Money Project Rules

These rules apply to every agent and script working in this repository.

## Operating Constraints

- Treat this as a zero-to-one capital experiment. The user will not provide initial funding.
- Money-making methods are not limited to onchain activity. Research and attempt any lawful, ethical, low-capital path that can plausibly produce funds, including bounties, grants, content, tooling, services, research, airdrops, and other non-onchain opportunities.
- The project may reinvest experimental proceeds into further attempts, and the user accepts that proceeds may go to zero. Agents still must document cost, risk, success criteria, and exit criteria before recommending any spend.
- Agents must not request, store, infer, or handle private keys, seed phrases, wallet passwords, keystore files, 2FA secrets, or browser sessions.
- If the user explicitly provides API credentials, store them only in ignored local `.env` files, never commit them, never write them to `llm-wiki/`, and never copy them into task JSON, logs, raw sources, or chat summaries.
- Agents must not connect wallets, sign transactions, submit transactions, or move funds. Any wallet action must be performed by the human wallet owner.

## Testing Rules

- Test-created files must stay under `tests/`.
- Use `tests/artifacts/` for runtime test output.
- Do not let tests write task JSON, logs, cache files, or temporary files into production directories such as `delegation/tasks/`, `llm-wiki/`, or the repository root.
- `tests/artifacts/` is ignored by git and may be deleted at any time.

## Git And Worktrees

- The default integration target is `master`.
- If an agent creates a `.worktrees/` worktree, it must merge finished work back to `master`, rerun verification on `master`, and clean up the worktree and feature branch.
- The user does not need to supervise each merge step. Agents are trusted to complete the worktree lifecycle carefully.

## Documentation

- Durable project knowledge belongs in `llm-wiki/` once that knowledge base exists.
- Raw sources should be saved under `llm-wiki/raw/` when practical and allowed.
- Strategy conclusions must be source-backed, risk-aware, and written so future agents can audit them.

## Marketing And Public Claims

- Use `.agents/product-marketing.md` as the canonical marketing context before creating positioning, launch, content, social, community, AI SEO, or free-tool plans.
- Project-installed marketing skills live under `.agents/skills/`; keep the installed set focused and explain additions in `llm-wiki/`.
- Treat marketing as part of the experiment, not decoration. Each public-facing claim should point back to a wiki page, source note, artifact, submission, transaction, or other auditable evidence.
- Social or community posts may be drafted by agents, but posting from human-owned accounts must remain a human action unless the user explicitly sets up a dedicated project account and grants safe posting access.
