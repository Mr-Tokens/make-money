# Execution Subthreads Protocol

Status: active
Date: 2026-05-20

## Purpose

Execution subthreads let the Make Money manager split verification and production work into bounded parallel tasks without flooding the main project thread.

The main thread remains responsible for:

- strategy decisions;
- risk boundaries;
- wallet and credential safety;
- final file edits;
- source-backed wiki writeback;
- revenue and evidence claims.

Subthreads gather evidence, test assumptions, and return manager-ready recommendations.

## Current Subthreads

| ID | Nickname | Task | Scope | File-write permission | Status |
|----|----------|------|-------|-----------------------|--------|
| `019e41f5-aa61-7840-a39b-feb25cb2c187` | Goodall | Tether Verification | Verify first no-capital Tether docs/tutorial/tooling opportunity | No tracked file edits | Completed; manager integrated |
| `019e41f5-aab3-7da2-981d-973ae138d630` | Planck | Tari Bounty Verification | Verify one small active Tari GitHub bounty backup | No tracked file edits | Completed; manager integrated |
| `019e41f5-ab11-7bd0-af10-5d932fb6551f` | James | Web3Grants Verification | Verify research multiplier fit and candidate programs | No tracked file edits | Completed; manager integrated |

## Subthread Rules

- Do not request or handle secrets.
- Do not connect wallets, sign transactions, submit transactions, or move funds.
- Do not create accounts or submit forms unless a future task explicitly grants a safe process.
- Do not claim revenue, payout, or safety.
- Cite source URLs.
- Separate agent-executable work from human-only actions.
- Return concise findings for manager review.
- Do not write durable wiki conclusions directly unless explicitly assigned a file ownership scope.

## Manager Review Rules

Subthread output is not evidence by itself. Before writing conclusions into `llm-wiki/`, the manager should:

1. Check source URLs.
2. Preserve uncertainty.
3. Record human-only actions.
4. Reject unsupported claims.
5. Link the final wiki note to raw sources or task outputs.

## Completion Pattern

When a subthread completes:

1. Read its final output.
2. Decide whether it is approved, partially useful, or rejected.
3. Write only durable, source-backed conclusions to LLM-Wiki.
4. Update this page's status table.
5. Choose the next manager action.
