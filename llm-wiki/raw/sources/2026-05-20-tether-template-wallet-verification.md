# Tether Template Wallet Verification

Date accessed: 2026-05-20
Subthread: `019e41f5-aa61-7840-a39b-feb25cb2c187`
Nickname: Goodall
Task: Tether Verification

## Official Sources

| Source | URL | Evidence captured |
|--------|-----|-------------------|
| Tether.dev bounties list | https://tether.dev/grants/bounties/ | Lists active grants and bounties, including WDK Module, WDK in eCommerce, Template Wallet, Browser Extension Starter, ANE Acceleration, LTX-2 Video Generation, and QVAC SDK Swift Client. |
| Template Wallet bounty | https://tether.dev/grants/bounties/2800541287/ | Lists "Template Wallet", date `24/03/2026`, grant amount `2,000 USD₮`, and explains that WDK currently offers starter templates only for React Native while other frameworks such as Next.js, Vue, Svelte, Angular, or Flutter require integrations from scratch. |
| Tether grants announcement | https://tether.io/news/tether-launches-developer-grants-program-to-fund-local-first-ai-and-payments-infrastructure/ | Official announcement for developer grants supporting local-first AI and payments infrastructure. Mentions documentation, tutorials, onboarding tools, tooling, integrations, and developer infrastructure. |
| Tether grant terms | https://tether.dev/grants/terms/ | Terms last updated 2026-04-01. Tether can request KYC, require additional information, accept/reject applications at its discretion, require a written agreement, and change/suspend/cancel the program. |

## Verified Opportunity

Candidate: **Tether.dev Template Wallet bounty**

Initial manager decision: shortlist as first execution target.

Why it fits:

- It is listed on an official Tether.dev bounty page.
- The visible award amount is `2,000 USD₮`.
- The requested work is a developer onboarding/template deliverable, not speculation.
- The page explicitly names frameworks such as Next.js, Vue, Svelte, Angular, and Flutter as gaps beyond React Native.
- A Next.js starter can be prepared without user-provided capital.
- Work can be made public as a repository, docs page, tutorial, or proposal package.

## Smallest Useful Deliverable

Prepare a **Next.js WDK Template Wallet proposal package**:

- one-page application brief for human submission;
- public repo outline;
- README tutorial outline;
- architecture notes;
- acceptance checklist mapped to the bounty description;
- mock-only demo mode that does not connect wallets, sign transactions, submit transactions, or move funds;
- `.env.example` only, with no real secrets.

This should be built as an application package first, not a full implementation. Tether's own bounty flow says they review applications, refine scope, and sign a bounty agreement before deliverables and payment.

## Human-Only Actions

- Submit the application form.
- Provide real contact/profile/experience details.
- Agree to Tether grant terms.
- Complete any KYC or due diligence.
- Sign any bounty agreement.
- Handle payout, tax, legal, and payment-address details.

## Risks And Unknowns

- No acceptance or payment is guaranteed.
- Tether can reject an application at its discretion.
- Tether can change, suspend, or cancel the program.
- KYC, jurisdiction, or due diligence can block participation.
- Application materials are not confidential under the terms.
- Exact acceptance criteria are not fully specified until scope refinement.
- Any payout setup is human-only and outside agent authority.

## Manager Recommendation

Proceed with a proposal package before writing production code.

Next step: create `Tether Template Wallet Application Pack v0.1` with a concise application brief, scope, mock-only safety model, milestone plan, and public README outline.
