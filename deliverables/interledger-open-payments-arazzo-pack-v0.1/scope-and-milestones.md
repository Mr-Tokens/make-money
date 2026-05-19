# Scope And Milestones

## Scope

Prepare a documentation-first package for Open Payments Arazzo workflow documentation.

In scope:

- map one-time payment flow steps;
- identify source Open Payments docs and API reference anchors;
- draft a candidate Arazzo workflow skeleton;
- write a companion developer explanation;
- document consent, grant continuation, token, and payment-state boundaries;
- publish as a small public artifact if accepted.

Out of scope for v0.1:

- live payment execution;
- wallet account setup;
- production SDK changes;
- Kiota generator changes;
- official Interledger docs changes without maintainer review;
- legal, tax, sanctions, or KYC representation by an agent.

## Proposed Milestones

| Milestone | Deliverable | Review signal |
|-----------|-------------|---------------|
| 1 | Flow inventory and source map | Interledger confirms target flow shape and preferred source docs. |
| 2 | Candidate Arazzo workflow draft | Maintainer or sponsor feedback on structure, operation mapping, and terminology. |
| 3 | Companion developer guide | Review confirms the guide improves onboarding clarity and does not misstate payment behavior. |
| 4 | Final docs package | Accepted public docs artifact or agreed delivery repository. |

## Proposed Timeline

Small docs-only version: 2 to 4 weeks after acceptance and scope confirmation.

Expanded version with validation tooling or examples: needs sponsor clarification before estimating.

## Budget Note

Public sources show a budget detail mismatch:

- Interledger grant page lists "Documenting Open Payments flows in Arazzo Specification" as up to `$1,000`.
- The GitHub wiki info box lists the SDK grant amount as `$5,000-$25,000`.

The application should avoid overclaiming budget and ask Interledger which amount applies to this narrow documentation scope.
