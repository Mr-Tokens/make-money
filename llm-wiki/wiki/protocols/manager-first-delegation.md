# Manager-First Delegation Protocol

Date: 2026-05-20
Raw source: [Manager-First Delegation Correction](../../raw/sources/2026-05-20-manager-first-delegation-correction.md)

## Purpose

Sesame should operate as a manager, not as a solo worker.

The default loop is:

1. Define the goal.
2. Split off bounded worker tasks.
3. Review worker output.
4. Integrate only useful, verified findings.
5. Decide the next external action.

## Default Delegation Rule

Before doing non-sensitive work directly, ask:

> Can Mimo or MiniMax do a bounded first pass without secrets, wallets, legal claims, or external account actions?

If yes, delegate first.

If no, record why the manager must do it directly.

## Responsibility Split

| Work type | Default owner | Notes |
|-----------|---------------|-------|
| Strategy choice | Codex/Sesame | Manager decides priorities, tradeoffs, and exit criteria. |
| Opportunity scans | MiniMax | Use templates, produce tables, include source links, do not execute. |
| Source summaries | MiniMax | Summarize only from provided or public sources. |
| Risk checks | MiniMax | Focus on blockers, no encouragement language. |
| Chinese/English polish | Mimo | Keep reader-facing copy clean and non-flattering. |
| Test expansion | Mimo | Add bounded tests when source code and scope are safe to share. |
| Wiki draft structure | Mimo or MiniMax | Workers may draft; Codex/Sesame performs final writeback. |
| Code implementation | Worker only when scope is isolated | Manager may implement only urgent, tiny, or sensitive changes. |
| Public PR/issue/comment submission | Codex/Sesame or human | Requires correct project identity and final review. |
| Wallets, funds, signatures | Human only | Agents may prepare instructions, never move funds. |
| Secrets, API keys, legal/KYC | Human or manager-only boundary | Workers must not receive secrets. |

## Worker Task Format

Each delegated task must include:

- worker name and provider;
- task type;
- source files or public links;
- exact output format;
- acceptance criteria;
- forbidden actions;
- whether the output is allowed to become public after manager review.

## Review Rule

Worker output is evidence, not truth.

Codex/Sesame must:

- approve or reject the task record;
- strip reasoning tags, filler, hype, and unverifiable claims;
- check for secret leakage;
- verify important claims against sources;
- decide whether the result updates a strategy, experiment, risk note, README, or no durable file.

## Current Queue

1. Mimo: draft additional edge-case tests for the `sh1pt` Listen Notes adapter without touching production code.
2. MiniMax: scan the next micro-cash candidate batch using the Micro Cash Sprint rejection rules.
3. Codex/Sesame: resolve project GitHub identity before any external PR, issue, or comment.

## Do Not Delegate

Do not delegate:

- private keys, seed phrases, wallet passwords, 2FA, browser sessions, or API keys;
- external account login or identity switching;
- wallet connection or transaction signing;
- legal, sanctions, tax, KYC, or payout representations;
- final claims of revenue;
- public submissions before manager review.
