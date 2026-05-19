# Provider Smoke Test

Date: 2026-05-20

## Hypothesis

The local Delegation Agent can call OpenAI-compatible worker providers using credentials stored only in ignored `.env`.

## Budget

Small API smoke-test calls. No wallet funds.

## Steps Taken

1. Created local `.env` with user-authorized provider credentials. The file is ignored by git.
2. Ran a MiniMax fast-provider smoke task through `scripts/delegate_task.py`.
3. Ran a Mimo smoke task through `scripts/delegate_task.py`.
4. Re-ran Mimo with a higher output cap after the first response used its budget mostly on reasoning tokens.

## Result

- Mimo `mimo-v2.5-pro`: usable. A completed task produced the summary line "Mimo worker is connected."
- MiniMax fast provider: blocked by provider-side rate limit. The API returned HTTP 429 and reported that the current 5-hour usage window was exhausted until `2026-05-20T05:00:00+08:00`.

## Lessons Learned

- Mimo can be used now for bounded worker tasks.
- Mimo may spend a meaningful share of small output limits on reasoning tokens, so practical smoke and research calls should use a less tiny output cap.
- MiniMax should be retried after the provider reset time before being marked unavailable.
- Provider credentials must remain local-only in `.env` and must not be copied into raw sources, wiki pages, task JSON committed to git, or logs.

## Related Files

- `delegation/providers.example.json`
- `delegation/README.md`
- `llm-wiki/raw/sources/2026-05-20-minimax-docs.md`
- `llm-wiki/raw/sources/2026-05-20-mimo-docs.md`
