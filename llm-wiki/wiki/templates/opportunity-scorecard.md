# Opportunity Scorecard Template

Use this template before spending meaningful time on a bounty, grant, hackathon, contribution, airdrop, or service opportunity.

## Candidate Summary

| Field | Value |
|-------|-------|
| Candidate ID | `opp-YYYY-MM-DD-###` |
| Name | |
| Opportunity type | bounty / grant / hackathon / docs contribution / research / free tool / service / other |
| Source URL | |
| Date accessed | |
| Sponsor/platform | |
| Status | discovered / rejected / shortlisted / in progress / submitted / awarded / paid / abandoned |

## Hard Filter

| Filter | Pass/Fail | Notes |
|--------|-----------|-------|
| Requires zero user-provided capital | | |
| No private-key, seed phrase, or wallet-password exposure | | |
| No agent-executed wallet signing or transaction submission | | |
| No upfront fee, deposit, paid boost, or paid access | | |
| No sybil, fake identity, spam, or wash activity | | |
| Acceptance criteria are documentable | | |
| Sponsor/source appears credible | | |

Reject immediately if any hard filter fails.

## Scoring

Score each field from 0 to 5 unless noted.

| Field | Score | Notes |
|-------|------:|-------|
| Sponsor credibility | | |
| Expected value | | |
| Time to first feedback | | |
| Deliverable clarity | | |
| Agent fit | | |
| Marketing value | | |
| Reusability | | |
| Effort cost | | Lower is better |
| Risk cost | | Lower is better |

Priority formula:

```text
priority = sponsor_credibility + expected_value + time_to_feedback + deliverable_clarity + agent_fit + marketing_value + reusability - effort_cost - risk_cost
```

## Decision

| Field | Value |
|-------|-------|
| Priority score | |
| Decision | reject / monitor / shortlist / execute now |
| Decision reason | |
| Smallest useful deliverable | |
| Owner | Codex / worker model / human |
| Next action | |
| Review date | |

## Evidence

- Source note:
- Related raw files:
- Related strategy:
- Related experiment:
- Submission/artifact link:
- Outcome proof:

## Postmortem

Fill after action or rejection.

| Question | Answer |
|----------|--------|
| What happened? | |
| Was the score directionally accurate? | |
| Did it create money, trust, learning, or reusable assets? | |
| What should future agents change? | |
