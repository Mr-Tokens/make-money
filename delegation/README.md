# Delegation Agent

This directory contains the lightweight local task delegation layer for the Make Money project.

## Safety Rules

- Real provider credentials go only in `.env`.
- `.env` is ignored by git.
- Do not paste API keys, wallet secrets, seed phrases, or private keys into prompts.
- Worker models may research, summarize, and risk-check.
- Worker models must not connect wallets, sign transactions, prepare transactions, or write directly to `llm-wiki/`.
- Approved task output still needs strategy-lead review before wiki writeback.
- Tests must write runtime artifacts only under `tests/artifacts/`.

## Setup

Copy `.env.example` to `.env` and enter rotated provider credentials:

```text
MINIMAX_API_KEY=
MIMO_API_KEY=
```

If Mimo Token Plan gives a cluster-specific URL, set `MIMO_BASE_URL` to that value.

## Dry Run

```powershell
python scripts/delegate_task.py --provider mimo --type research --title "Dry run" --prompt "Summarize the safety rules for this project." --dry-run
```

## Run A Worker Task

```powershell
python scripts/delegate_task.py --provider minimax --type summary --title "Protocol summary" --prompt "Summarize the provided source note." --source "llm-wiki/raw/sources/example.md"
```

## Review A Task

```powershell
python scripts/review_task.py --task-id "TASK_ID" --decision approved --reason "Useful and source-backed"
python scripts/review_task.py --task-id "TASK_ID" --decision rejected --reason "Unsupported claims"
```
