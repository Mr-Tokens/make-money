# sh1pt Listen Notes PR Draft Source Bundle

Date accessed: 2026-05-20
Purpose: record the first local micro-cash code contribution attempt after selecting the small target band.

## Sources Checked

| Source | URL | Notes |
|--------|-----|-------|
| sh1pt umbrella CLI issue | https://github.com/profullstack/sh1pt/issues/133 | Open issue asking contributors to create issues and PRs for the main CLI command work, with payment after enough merged PRs through ugig.net. |
| sh1pt platform backlog issue | https://github.com/profullstack/sh1pt/issues/6 | Open issue tied to ugig work, asking for PRs for platforms listed in the README. It includes adapter backlog context. |
| sh1pt review-help issue | https://github.com/profullstack/sh1pt/issues/265 | Open issue from the maintainer asking for help reviewing and commenting on the large open PR queue. |
| Listen Notes API docs | https://www.listennotes.com/api/docs/ | Official docs show API v2, base URL `https://listen-api.listennotes.com/api/v2`, OpenAPI docs, mock server, and search endpoint references. |
| Listen Notes search help | https://www.listennotes.help/en/articles/5681273-use-podcast-search-apis | Official help page explains `GET /search` as the full-text search endpoint. |
| Listen Notes quickstart | https://www.listennotes.help/en/articles/4860027-podcast-api-quickstarts | Official quickstart shows `X-ListenAPI-Key` authentication and the base API request pattern. |
| Local sh1pt worktree | `.worktrees/sh1pt` | Local ignored worktree used for repository inspection and patch drafting. |

## Local Patch State

- External repository: `profullstack/sh1pt`
- Local branch: `sesame/listennotes-outreach-search`
- Local commit: `8d9f5ab02437b57d135ed42bcb8ed4dafb2e4b10`
- Changed package: `packages/outreach/listennotes`
- Public submission: not submitted yet

## Claim Boundary

This is not revenue and not an accepted bounty.

The patch exists locally as verified proof-of-work. Public PR submission is blocked until the active GitHub CLI account is confirmed as the project identity rather than a personal account.
