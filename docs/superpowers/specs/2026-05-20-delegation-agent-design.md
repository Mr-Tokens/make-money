# Delegation Agent Design

Date: 2026-05-20
Status: Draft for user review

## Purpose

Create a lightweight local delegation layer for the Make Money project. The layer lets the Codex strategy lead assign bounded research and summarization tasks to OpenAI-compatible worker models, preserve their outputs for review, and only promote approved results into `llm-wiki/`.

The system is intentionally small. It is not a full task platform, not an autonomous trading system, and not a wallet operator.

## Chosen Approach

Use only方案 A: a local file-based Delegation Agent.

The first version uses simple scripts and Markdown/JSON files:

- A task is created from a prompt, a provider key, and optional source references.
- A worker model runs the task through an OpenAI-compatible Chat Completions endpoint.
- The raw worker result is saved for audit.
- The strategy lead reviews the result before any wiki writeback.

## Source Guidance

Official OpenAI docs consulted:

- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/orchestration
- https://developers.openai.com/api/docs/guides/function-calling
- https://developers.openai.com/api/docs/guides/tools

Design implications:

- The project should use a manager-style pattern, where the main agent keeps final answer ownership and calls specialists as bounded helpers.
- Worker calls should be treated like tool calls: application code sends a task, receives output, validates it, and only then continues.
- Guardrails and human review are required before risky or money-affecting work continues.

## Providers

Provider credentials must live in `.env`, which is ignored by git.

Committed files may record only public provider metadata:

| Provider | Base URL | Model | Source |
| --- | --- | --- | --- |
| MiniMax | `https://api.minimaxi.com/v1` | `MiniMax-M2.7` | https://platform.minimaxi.com/docs/guides/models-intro |
| Xiaomi Mimo | `https://api.xiaomimimo.com/v1` | `mimo-v2.5-pro` | https://platform.xiaomimimo.com/docs/en-US/welcome |
| Xiaomi Mimo Token Plan | set via `MIMO_BASE_URL` | `mimo-v2.5-pro` | https://platform.xiaomimimo.com/llms.txt |

Policy update: active MiniMax delegation uses only the non-high-speed `MiniMax-M2.7` model.

Mimo Token Plan may require cluster-specific Base URLs from the subscription page. The implementation must read `MIMO_BASE_URL` from `.env` and treat the default direct API URL as a fallback only.

## Directory Layout

```text
delegation/
  README.md
  providers.example.json
  prompts/
    worker-research.md
    worker-summary.md
    worker-risk-check.md
  tasks/
    pending/
    completed/
    rejected/
scripts/
  delegate_task.py
  review_task.py
```

## Task Lifecycle

### Create

`delegate_task.py` creates a task from:

- provider name: `minimax` or `mimo`
- task type: `research`, `summary`, or `risk-check`
- title
- prompt text
- optional source URLs or local raw paths

The script writes a pending task file before calling a worker.

### Run

The script loads provider settings from `.env` and `providers.example.json`, calls the provider's OpenAI-compatible Chat Completions endpoint, and saves the response under `delegation/tasks/completed/`.

The saved result includes:

- task id
- created time
- provider
- model
- title
- input prompt
- source references
- worker output
- status: `completed`

It must not include API keys.

### Review

`review_task.py` changes a completed task into:

- `approved`: ready for manual wiki writeback by the strategy lead.
- `rejected`: moved to `delegation/tasks/rejected/` with a reason.

Approval does not automatically write to `llm-wiki/` in v0. The strategy lead performs wiki writeback separately after checking sources and risk.

## Worker Contracts

### Research Worker

Output:

- concise answer
- source list
- confidence rating
- missing information
- money or wallet risks
- suggested next questions

### Summary Worker

Output:

- short summary
- key facts
- entities and protocols mentioned
- claims that need source verification
- suggested wiki pages to update

### Risk Check Worker

Output:

- risk categories
- likely failure modes
- required human checks
- do-not-proceed conditions
- safer alternatives

## Permissions

Workers may:

- Read prompt text and source excerpts passed to them.
- Produce Markdown or JSON analysis.
- Suggest pages, questions, and follow-up research.

Workers must not:

- Receive API keys, private keys, seed phrases, wallet passwords, or browser session secrets.
- Connect to wallets.
- Sign, approve, submit, or prepare transactions.
- Directly edit `llm-wiki/`.
- Treat possible profit as guaranteed.
- Recommend execution without cost, risk, success criteria, and exit criteria.

## Secret Handling

`.env` is the only expected location for real provider credentials.

Required variables:

```text
MINIMAX_BASE_URL=https://api.minimaxi.com/v1
MINIMAX_API_KEY=
MINIMAX_MODEL=MiniMax-M2.7

MIMO_BASE_URL=https://api.xiaomimimo.com/v1
MIMO_API_KEY=
MIMO_MODEL=mimo-v2.5-pro
```

Any token pasted into chat, logs, git, raw sources, or wiki pages must be considered compromised and rotated.

## Error Handling

The scripts should fail closed:

- Missing `.env` key: print a clear setup message and do not create a completed task.
- Provider HTTP error: keep the pending task and write an error note.
- Malformed worker output: save it, but mark the task as needing review.
- Unknown provider or task type: reject before any API call.

## Testing

Initial verification:

- `git check-ignore -v .env .env.local` confirms secrets are ignored.
- `delegate_task.py --dry-run` creates a task payload without calling a provider.
- A smoke task can call each configured provider after the user supplies rotated local credentials.
- `review_task.py` can approve or reject a saved task without touching `llm-wiki/`.

## Success Criteria

The v0 Delegation Agent is successful when:

- Provider metadata is committed without secrets.
- Real credentials can be supplied locally through `.env`.
- A task can be delegated to MiniMax or Mimo.
- Worker output is saved in an auditable file.
- Rejected work is preserved with a reason.
- Approved work still requires strategy-lead review before wiki writeback.
- No script can perform wallet actions or persist secrets.
