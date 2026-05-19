# Web3 Builder Reputation Sprint

Status: active
Date: 2026-05-20
Horizon: 14 days

## Thesis

The first zero-to-one path should not be speculative trading or airdrop farming. It should be reputation-building work that can earn through bounties, grants, paid contribution opportunities, useful tooling, and public trust.

The compounding asset is not only money. It is a public record that proves the project can discover opportunities, filter risks, produce useful artifacts, submit work, and learn from outcomes.

## Success Criteria

By the end of the sprint:

- Research at least 10 current no-capital Web3 or adjacent earning opportunities.
- Rank at least 3 opportunities with a scorecard.
- Execute at least 1 real submission, contribution, or public deliverable.
- Create at least 1 reusable free tool or template from the process.
- Draft at least 3 public content atoms from the work.
- Spend no user-provided capital.
- Avoid wallet signing, private-key custody, upfront fees, and spam.

## Opportunity Types

| Type | Why it fits zero capital | Examples |
|------|--------------------------|----------|
| Bounties | Payment for deliverables, not speculation | Writing, research, code, analysis, docs, design |
| Grants | Funds public-good or ecosystem contributions | Small ecosystem grants, retroactive grants, community grants |
| Hackathons | Prize upside plus portfolio value | Tooling, dashboards, protocol integrations |
| Docs and devrel contributions | Builds trust and may lead to paid work | Tutorials, fixes, examples, issue triage |
| Research reports | Useful to protocols and communities | Opportunity maps, risk notes, ecosystem intelligence |
| Free tools | Attracts links, trust, and potential leads | Scorecards, trackers, calculators, analyzers |
| Careful testnet participation | Can build proof without spend when risk is low | Only when no wallet signing or value transfer is required by agents |

## Hard Filters

Reject opportunities that require:

- Private keys, seed phrases, wallet passwords, or browser wallet control.
- Agent-executed wallet signatures or transactions.
- Upfront payment, paid boosts, paid access, or "deposit to qualify" mechanics.
- Sybil behavior, fake identities, spam, wash activity, or fake engagement.
- Unrealistic guaranteed-return language.
- KYC evasion or account sharing.
- Work whose success cannot be documented.

## Scorecard

Use this table for each candidate:

| Field | Scoring prompt |
|-------|----------------|
| Source URL | Where did this opportunity come from? |
| Sponsor credibility | Known team, official platform, verified ecosystem link? |
| Expected value | Prize, bounty, grant size, relationship value, or portfolio value |
| Time to first feedback | How quickly can we know if it is worth continuing? |
| Required capital | Must be zero for this sprint |
| Wallet risk | Any signature, connection, transaction, custody, or phishing surface? |
| Deliverable clarity | Are acceptance criteria concrete? |
| Agent fit | Can Codex plus worker models produce a useful output? |
| Marketing value | Can the attempt become a public proof artifact? |
| Reusability | Does it create a template, tool, dataset, or wiki page for future agents? |

Initial ranking formula:

```text
priority = expected_value + marketing_value + reusability + sponsor_credibility - effort - risk
```

The formula is intentionally simple. The point is consistent judgment, not false precision.

## Execution Loop

1. Discover opportunities from reputable bounty, grant, hackathon, open-source, and ecosystem channels.
2. Save raw source notes under `llm-wiki/raw/` when practical.
3. Score each candidate and reject unsafe ones quickly.
4. Delegate focused research to worker models where useful.
5. Select one narrow deliverable that can be completed without capital.
6. Produce the artifact in the repository or as a documented external submission.
7. Record the submission, status, and lessons.
8. Convert the artifact into a wiki page, a public content draft, and a reusable tool or template when possible.

## Marketing Overlay

Each attempt should create at least one of these assets:

- A wiki strategy page or experiment page.
- A raw source bundle.
- A scorecard row future agents can compare.
- A reusable template or free tool.
- A build-in-public post draft.
- A postmortem that states what worked, what failed, and what changed.

No hype is allowed unless evidence has earned it. The public story is stronger when it is precise.

## First Deliverables

1. **Opportunity Scorecard Template**: a lightweight Markdown/CSV-style template for ranking bounties, grants, and public-good work. Created at `llm-wiki/wiki/templates/opportunity-scorecard.md`.
2. **Opportunity Scan Batch 001**: at least 10 candidates, with hard-filter notes and top 3 ranking.
3. **First Submission**: one useful deliverable submitted to a credible sponsor or public project.
4. **Public Launch Draft**: a short build-in-public thread/post explaining the experiment and linking back to evidence.

## Evidence To Capture

- Source URL and access date.
- Sponsor or platform name.
- Deliverable requirements.
- Rejection reason if filtered out.
- Final artifact path or submission link.
- Date submitted.
- Outcome status: pending, rejected, awarded, paid, abandoned, or converted to another path.
- Follow-up actions.

## Exit Criteria

Stop or pivot if:

- No credible opportunities survive the hard filters after 20 candidates.
- The first two submissions reveal that the project lacks necessary skills or channels.
- The best opportunities require human-only wallet, identity, or account actions that the user does not want to perform.
- A more credible no-capital path appears outside Web3.

If the sprint produces no money but creates reusable tools, public attention, or sponsor conversations, it can still count as strategic progress. If it produces only private notes, it failed the marketing half of the experiment.
