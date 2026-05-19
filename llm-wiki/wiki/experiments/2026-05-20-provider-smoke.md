# Provider Smoke Test

Date: 2026-05-20

## Hypothesis

The local Delegation Agent can call OpenAI-compatible worker providers using credentials stored only in ignored `.env`.

## Budget

Small API smoke-test calls. No wallet funds.

## Steps Taken

1. Created local `.env` with user-authorized provider credentials. The file is ignored by git.
2. Ran an initial MiniMax high-speed provider smoke task through `scripts/delegate_task.py`.
3. Ran a Mimo smoke task through `scripts/delegate_task.py`.
4. Re-ran Mimo with a higher output cap after the first response used its budget mostly on reasoning tokens.

## Result

- Mimo `mimo-v2.5-pro`: usable. A completed task produced the summary line "Mimo worker is connected."
- The initial MiniMax high-speed provider path was blocked by provider-side rate limit. That path is now historical only.

## Lessons Learned

- Mimo can be used now for bounded worker tasks.
- Mimo may spend a meaningful share of small output limits on reasoning tokens, so practical smoke and research calls should use a less tiny output cap.
- Active MiniMax work should use only the non-high-speed `MiniMax-M2.7` provider.
- MiniMax non-high-speed should receive its own smoke test before being marked usable.
- Provider credentials must remain local-only in `.env` and must not be copied into raw sources, wiki pages, task JSON committed to git, or logs.

## Related Files

- `delegation/providers.example.json`
- `delegation/README.md`
- `llm-wiki/raw/sources/2026-05-20-minimax-docs.md`
- `llm-wiki/raw/sources/2026-05-20-mimo-docs.md`
