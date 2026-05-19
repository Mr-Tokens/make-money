# Opportunity Scan Batch 001

Status: manager-reviewed pre-screen
Date: 2026-05-20
Strategy: [Web3 Builder Reputation Sprint](../strategies/2026-05-20-web3-builder-reputation-sprint.md)
Raw source bundle: [Opportunity Scan Batch 001 Source Bundle](../../raw/sources/2026-05-20-opportunity-scan-batch-001-sources.md)
Worker task: `20260519T202500Z-opportunity-scan-batch-001-pre-screen-63fa3c7f`

## Objective

Find at least 10 current no-capital earning opportunities that fit the Make Money constraints:

- no user-provided capital;
- no agent wallet actions;
- no private-key or seed-phrase handling;
- real deliverables over speculation;
- public proof where possible;
- revenue claims only after evidence.

## Candidates

| ID | Candidate | Type | Initial Decision | Reason |
|----|-----------|------|------------------|--------|
| opp-2026-05-20-001 | Superteam Earn bounties | bounty / gig marketplace | Monitor | Good marketplace fit, but specific active listings and payout flow need verification. |
| opp-2026-05-20-002 | Superteam Earn projects | project contribution | Monitor | Could produce proof of work, but needs current acceptance criteria. |
| opp-2026-05-20-003 | Tether.dev grants and bounties | grant / bounty | Shortlist | Official source lists concrete task values and desired docs, tutorials, onboarding, code libraries, apps, research, and tooling. |
| opp-2026-05-20-004 | Tether local-first AI and payments grants | grant | Shortlist | Recent official announcement and strong fit for research/tooling deliverables. |
| opp-2026-05-20-005 | Lightning Bounties | GitHub bounty | Monitor | Public PR flow is attractive, but payout requires human Lightning setup. |
| opp-2026-05-20-006 | BountyPay | GitHub bounty | Human-only monitor | Requires wallet linkage; agent can only prepare code if a human handles platform setup. |
| opp-2026-05-20-007 | ETHGlobal New York 2026 | hackathon | Conditional | Likely high marketing value, but IRL logistics and remote participation need verification. |
| opp-2026-05-20-008 | ETHOnline 2026 | online hackathon | Monitor | Remote format fits, but dates, prize tracks, and registration details are later. |
| opp-2026-05-20-009 | Chainlink grants | grant | Monitor | Credible ecosystem, but current application path and fit need more detail. |
| opp-2026-05-20-010 | Web3Grants database | research multiplier | Shortlist | Useful for finding more grant targets; not a direct income source. |
| opp-2026-05-20-011 | Potlock | public goods funding | Reject for now | Direct earning path unclear from first pass. |
| opp-2026-05-20-012 | SHAFT Foundation | AI/Web3 bounty ecosystem | Reject pending verification | Claims require team and payout verification before use. |
| opp-2026-05-20-013 | Tari bounty program | GitHub bounty | Shortlist | Public GitHub workflow and AI-assisted development appears allowed; active issues and token value need verification. |
| opp-2026-05-20-014 | Opentribe | Polkadot marketplace | Monitor | Polkadot grants/bounties/RFPs may fit, but active board needs verification. |
| opp-2026-05-20-015 | AgentBounty | AI-agent bounty platform | Reject | First pass found stale due dates and high credibility risk. |

## Manager Top 3

1. **Tether.dev grants and bounties**
   - Fit: strongest first target.
   - Smallest useful deliverable: docs/tutorial/onboarding review or starter template proposal.
   - Next verification: inspect current application form, task requirements, terms, payout/KYC requirements, and whether a public artifact can be prepared before human submission.

2. **Tari bounty program**
   - Fit: GitHub-public contribution backup, now marked contested.
   - Smallest useful deliverable: one small documentation/test/code PR against a confirmed open bounty issue.
   - Verification result: [Tari Bounty Verification](../../raw/sources/2026-05-20-tari-bounty-verification.md) found a possible docs issue, but it already has competing PRs and should not be executed before maintainer confirmation.

3. **Web3Grants database**
   - Fit: research multiplier, not direct revenue.
   - Smallest useful deliverable: a filtered report of grants matching zero-capital, docs/tooling/research, and public-proof criteria.
   - Next verification: test whether the database can surface current grants without account friction.

## Rejections

- **AgentBounty:** rejected for this batch because crawler-visible due dates were stale and activity claims require verification.
- **SHAFT Foundation:** rejected pending verification because payout claims and bounty listings need stronger proof.
- **Potlock:** rejected for now because direct earning path was not clear enough for a first execution target.

## Risks

- Wallet setup for payout is human-only.
- Platform accounts, KYC, forms, and payout addresses are human-only until a safe dedicated process exists.
- Worker output is useful but not primary evidence.
- All expected values remain unverified until a sponsor accepts a deliverable or payment is received.

## Decision

Batch 001 successfully produced more than 10 candidates and a first top 3. The next execution step is **Tether verification**, because it has the best combination of source credibility, no-capital fit, deliverable clarity, and public proof potential.

## Next Action

Open Tether.dev grant/bounty details, identify one documentation/tutorial/onboarding deliverable, and write a first proposal or artifact outline. If Tether requires account-only access before details are visible, ask the human to complete only the account step and share non-secret task details.
