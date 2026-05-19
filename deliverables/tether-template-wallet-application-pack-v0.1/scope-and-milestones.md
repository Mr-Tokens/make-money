# Scope And Milestones

## Proposed Scope

| Area | Included | Notes |
|------|----------|-------|
| Framework | Yes | Next.js App Router, TypeScript, strict configuration. |
| WDK-oriented architecture | Yes | Adapter boundary and module organization designed around WDK concepts. |
| Mock-first demo mode | Yes | Default mode uses deterministic mock data and placeholder addresses. |
| Documentation | Yes | README, setup guide, architecture notes, extension guide. |
| Environment handling | Yes | `.env.example` only; no real secrets. |
| Wallet connection | No for v0.1 | No live wallet connection before Tether scope agreement. |
| Transaction signing | No | No signing, broadcasting, or live fund movement. |
| Production wallet readiness | No | This is a developer starter and onboarding asset. |
| Multi-framework delivery | No | Next.js first; later templates can reuse the pattern. |

## Deliverables

1. **Starter repository**
   - Proposed name: `tether-wdk-nextjs-template`
   - Includes Next.js app structure, WDK adapter boundary, mock data layer, and UI flow skeleton.

2. **README and tutorial**
   - Setup in a few commands.
   - Explanation of mock mode.
   - Architecture map.
   - How to replace mock adapters after scope approval.

3. **Architecture note**
   - Component boundaries.
   - Client/server split.
   - Environment variables.
   - Where WDK modules would be initialized and used.

4. **Safety note**
   - Explains that v0.1 contains no real signing or fund movement.
   - Lists human-only actions.
   - Documents assumptions and risks.

5. **Final package**
   - Tagged release or reviewable repository state if Tether accepts the scope.

## Milestone Plan

| Milestone | Output | Estimated Time |
|-----------|--------|----------------|
| M0: Scope agreement | Confirm framework, expected WDK depth, and acceptance criteria with Tether. | Human/Tether dependent |
| M1: Starter skeleton | Next.js project structure, mock wallet state, placeholder UI, safe env handling. | 2-3 days |
| M2: WDK adapter design | Adapter interfaces, module boundaries, docs explaining WDK integration path. | 2-3 days |
| M3: README and tutorial | Setup guide, architecture walkthrough, mock mode explanation, extension guide. | 2-3 days |
| M4: Review package | Acceptance checklist, QA pass, final polish, handoff notes. | 1-2 days |

The implementation should not begin as a full build until Tether confirms that a proposal-first scope is acceptable.

## Out Of Scope

- Real key generation.
- Real seed phrase handling.
- Wallet custody.
- Live chain transactions.
- Payout handling.
- Hosted production deployment.
- Legal, tax, KYC, or payment processing.
