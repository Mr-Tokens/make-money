# Opportunity Scan Batch 002

Status: manager-selected second target
Date: 2026-05-20
Strategy: [Web3 Builder Reputation Sprint](../strategies/2026-05-20-web3-builder-reputation-sprint.md)
Raw source bundle: [Opportunity Scan Batch 002 Source Bundle](../../raw/sources/2026-05-20-opportunity-scan-batch-002-sources.md)

## Objective

Find the next no-capital opportunity that can be advanced without waiting for the human project owner after the Tether application was submitted.

Hard filters remain unchanged:

- no startup capital;
- no agent wallet actions;
- no private-key custody;
- no spam, sybil behavior, or fake credentials;
- evidence before revenue claims;
- human-only actions for legal terms, identity, KYC, signatures, payout, and wallet setup.

## Candidate Scorecard

| ID | Candidate | Type | Evidence | Decision | Reason |
|----|-----------|------|----------|----------|--------|
| opp-2026-05-20-016 | Interledger Open Payments SDK grant: Arazzo flow documentation | grant / developer documentation | Official Interledger page and GitHub wiki | Shortlist as second target | Smallest useful deliverable is a public Arazzo flow sketch plus proposal pack. Strong fit for docs, standards, payments, and zero-capital work. |
| opp-2026-05-20-017 | Circle Developer Grants | grant / product integration | Official Circle grant page | Monitor | Strong sponsor and stablecoin fit, but favors teams with shipped products, usage, pilots, revenue, or Arc/Circle integration roadmap. Better after Make Money has a usable tool. |
| opp-2026-05-20-018 | IOTA Grants | grant / open-source / education | Official IOTA grant page | Monitor | Supports open-source tooling and education, but scope is broad; needs a sharper project idea before application. |
| opp-2026-05-20-019 | The Graph Grants | grant / tooling / data services | Official The Graph grant page | Monitor | The program fits tooling and data services, but the page showed no open RFPs. A custom proposal is possible later. |
| opp-2026-05-20-020 | Avalanche Foundation Research Grants | research grant | Official Avalanche Foundation post | Monitor, not immediate | High potential value, but deadline is 2026-06-01, scope is academic, proposals need rigorous methodology and researcher CVs, and work runs 12 months. |

## Manager Decision

The **Interledger Open Payments SDK grant** is the best second execution target.

Target the listed theme **Documenting Open Payments flows in Arazzo Specification** because it can begin with a public, reviewable artifact before any legal or account submission. The first useful output should be an application pack plus an Arazzo flow sketch that maps Open Payments grant, incoming payment, quote, and outgoing payment steps into candidate workflow documentation.

## Why Interledger Wins This Batch

- It has a public official grant page and an official GitHub wiki.
- The program is open on a rolling basis until the budget is awarded.
- Individuals and organizations not subject to US sanctions are eligible.
- Generative AI is allowed if disclosed, but must be reviewed by humans.
- The work can be advanced through documentation and standards analysis without wallet signing or funds.
- A public artifact can become reusable even if no grant is awarded.

## Known Risks

- Interledger's public page and GitHub wiki show a budget-detail mismatch: the page lists Arazzo flow documentation as "up to $1,000", while the GitHub wiki info box says the SDK grant amount is `$5,000-$25,000`. Treat this as a sponsor-clarification item before submission.
- Submission through Interledger's grant manager is still human-only.
- The project must disclose AI assistance if submitted.
- A polished proposal is not acceptance, and acceptance is not payment.

## Next Action

Create `Interledger Open Payments Arazzo Application Pack v0.1` with:

- concise application brief;
- Arazzo flow sketch;
- scope and milestones;
- human-only action checklist;
- safety boundaries;
- evidence list.
