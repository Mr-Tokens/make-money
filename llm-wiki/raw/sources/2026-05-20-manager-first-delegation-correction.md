# Manager-First Delegation Correction

Date recorded: 2026-05-20
Source type: conversation-derived correction plus reviewed worker outputs

## Trigger

The user corrected the workflow: Codex/Sesame was still doing too much directly instead of assigning bounded work to Mimo and MiniMax.

## Worker Tasks Reviewed

| Task | Provider | Decision | Use |
|------|----------|----------|-----|
| `20260519T221857Z-manager-first-delegation-protocol-draft-988bc7b3` | Mimo V2.5 Pro | Approved | Provided the first manager/worker responsibility split and next-task structure. |
| `20260519T221857Z-sh1pt-listennotes-pr-submit-risk-check-7303d607` | MiniMax M2.7 | Approved | Identified sh1pt PR submission blockers: project GitHub identity, payout-chain verification, platform rules, and secret hygiene. |

## Integration Boundary

Worker outputs are not copied directly into public project knowledge.

Codex/Sesame must review, trim, remove any reasoning tags or unsafe wording, and integrate only concrete instructions, risks, and decisions.

## Resulting Rule

Default execution should be manager-first:

- delegate research, drafting, risk checks, scans, summaries, tests, and routine wiki maintenance;
- keep strategy, final judgment, public submission, identity use, wallet/fund handling, secrets, and legal/KYC decisions under Codex/Sesame or human control;
- review every worker output before durable writeback.
