# Project Conversation Requirements

Date captured: 2026-05-20  
Source type: Conversation-derived source note

## Durable Requirements

- The project is named Make Money.
- The knowledge base must follow the LLM-Wiki pattern.
- `llm-wiki/` is the root folder for all LLM-Wiki content.
- Raw materials belong under `llm-wiki/raw/`.
- Public wallet addresses may be stored locally.
- Private wallet material must never be stored.
- Delegation to MiniMax and Mimo is allowed through OpenAI-compatible APIs.
- API credentials explicitly provided by the user may be used locally, but must only live in ignored `.env` files and must not be committed or written to the wiki.
- The user will not provide initial project funding.
- Money-making paths are not limited to onchain activity.
- Proceeds from successful experiments may be reinvested or risked, including going to zero, after documenting risk and exit criteria.
- Test-created files must stay under `tests/`, normally `tests/artifacts/`.
- If `.worktrees/` is used, finished work must be merged back to `master` and the worktree cleaned up.
