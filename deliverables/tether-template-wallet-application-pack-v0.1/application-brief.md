# Application Brief

## Target

Tether.dev Template Wallet bounty:

- Official page: https://tether.dev/grants/bounties/2800541287/
- Listed amount: `2,000 USDt`
- Posted date shown on page: `24/03/2026`

## Proposal

Build a **Next.js WDK Template Wallet starter** that helps web developers evaluate Tether's Wallet Development Kit without starting from a blank integration.

The public bounty page states that WDK currently offers starter templates only for React Native, while developers using frameworks such as Next.js, Vue, Svelte, Angular, or Flutter must build integrations from scratch. This proposal targets that gap with a Next.js-first starter because Next.js is a common choice for web wallet interfaces, dashboards, documentation demos, and developer portals.

## Proposed Outcome

The deliverable would be a small open-source starter repository with:

- a Next.js App Router scaffold;
- a WDK-oriented adapter boundary;
- mock-first wallet flows for onboarding and UI exploration;
- safe environment handling through `.env.example`;
- a README that teaches setup, architecture, and extension paths;
- an acceptance checklist mapped to the bounty description.

The first version should focus on onboarding clarity and implementation pattern quality. It should not be a production wallet, a custody product, or a live transaction demo.

## Why This Fits The Bounty

This application focuses on the specific problem described by Tether:

- developers outside React Native need a starter path;
- inconsistent patterns slow adoption;
- a framework-native template can reduce onboarding friction;
- documentation and examples can make WDK easier to evaluate.

The proposed template would give Next.js developers a concrete path from "what is WDK?" to "how would a web app organize WDK-related wallet flows?"

## Applicant Notes For Human Submission

The application form includes identity and contact fields. Those must be completed by the human project owner or an authorized project representative.

Suggested short proposal text:

```text
I propose a Next.js WDK Template Wallet starter that addresses the current framework gap described in the Template Wallet bounty. The package would include a Next.js App Router scaffold, a WDK-oriented adapter boundary, mock-first wallet flows, safe environment handling, and documentation that explains setup, architecture, and extension paths. The initial demo would avoid real wallet connection, signing, or fund movement while making the integration pattern clear for developers evaluating WDK. If accepted, I would coordinate scope with Tether before implementing any production-facing wallet behavior.
```

Suggested relevant experience framing:

```text
This project can produce documentation-first developer tooling, public repositories, application packages, and source-backed technical writeups. The Make Money project already maintains an LLM-Wiki, opportunity scorecards, and agent-reviewed source notes. For this bounty, the focus would be a narrow, auditable starter package rather than speculative or custodial wallet behavior.
```

Do not paste private credentials, wallet secrets, or API keys into the application.
