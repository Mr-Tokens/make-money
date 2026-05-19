# sh1pt Listen Notes PR Draft

Date: 2026-05-20
Strategy: [Micro Cash Sprint](../strategies/2026-05-20-micro-cash-sprint.md)
Raw source bundle: [sh1pt Listen Notes PR Draft Source Bundle](../../raw/sources/2026-05-20-sh1pt-listennotes-pr-draft-sources.md)
Related scan: [Micro Cash Scan Batch 001](2026-05-20-micro-cash-scan-batch-001.md)

## Hypothesis

A small, real adapter PR against `profullstack/sh1pt` can become the first stackable micro-cash proof-of-work.

The target remains **5-20 USDT/USDC-equivalent**, but this specific draft may be below that by itself. It is useful if it can become one of several accepted small PRs.

## Target

Selected local contribution: `packages/outreach/listennotes`.

Reason:

- Listed under the `sh1pt` adapter/platform backlog.
- Existing implementation returned empty results.
- Official Listen Notes API docs provide a clear `GET /search` path.
- Scope is small enough for a focused PR with tests.

## Implementation Draft

Local external worktree:

- Path: `.worktrees/sh1pt`
- Branch: `sesame/listennotes-outreach-search`
- Commit: `8d9f5ab02437b57d135ed42bcb8ed4dafb2e4b10`

Implemented:

- `outreach-listennotes.search()` now builds Listen Notes `/search` requests.
- Dry-run mode returns request plans without network calls.
- Live mode requires `LISTENNOTES_API_KEY` or `config.apiKey`.
- API calls send `X-ListenAPI-Key` and map podcast results into compact candidate records.
- API errors include status and a short body excerpt.
- Focused tests cover dry-run, live mapping, missing key, and API errors.

## Verification

TDD red check:

- `npm exec --package=pnpm@9.12.0 -- pnpm exec vitest run packages/outreach/listennotes/src/index.test.ts`
- Expected failure before implementation: 4 new tests failed because the adapter returned `{ podcasts: [] }`.

Green checks:

- `npm exec --package=pnpm@9.12.0 -- pnpm exec vitest run packages/outreach/listennotes/src/index.test.ts` passed: 6 tests.
- `npm exec --package=pnpm@9.12.0 -- pnpm --filter @profullstack/sh1pt-outreach-listennotes typecheck` passed.
- `npm exec --package=pnpm@9.12.0 -- pnpm --filter @profullstack/sh1pt-outreach-listennotes build` passed.
- `npm exec --package=pnpm@9.12.0 -- pnpm --filter @profullstack/sh1pt typecheck` passed.
- `git diff --check` passed.

## Public Submission State

Not submitted.

Blocker: the active GitHub CLI account is not confirmed as the project identity. Do not open external issues, PRs, or comments until the project identity is active.

## PR Draft

Title:

`feat(outreach): implement Listen Notes search`

Body:

```text
Implements a focused Listen Notes outreach adapter slice.

Changes:
- Adds real /search request construction for podcast discovery.
- Keeps dry-run side-effect free by returning request plans.
- Requires LISTENNOTES_API_KEY or config.apiKey for live search.
- Maps Listen Notes podcast results into compact candidate records.
- Surfaces API errors with status and body excerpts.
- Adds focused Vitest coverage for dry-run, live mapping, missing key, and API errors.

Verification:
- pnpm exec vitest run packages/outreach/listennotes/src/index.test.ts
- pnpm --filter @profullstack/sh1pt-outreach-listennotes typecheck
- pnpm --filter @profullstack/sh1pt-outreach-listennotes build
- pnpm --filter @profullstack/sh1pt typecheck
- git diff --check
```

## Result

Revenue remains `0`.

The attempt produced verified proof-of-work but no submitted PR and no payment yet.
