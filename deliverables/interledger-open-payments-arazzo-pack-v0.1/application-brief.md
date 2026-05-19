# Application Brief

## Target

Interledger Open Payments SDK grant program:

- Official page: https://interledger.org/grant/open-payments-sdk
- Official wiki: https://github.com/interledger/Grants/wiki/SDK-grant-program
- Narrow theme: Documenting Open Payments flows in Arazzo Specification

## Proposal

Build an **Open Payments Arazzo Flow Documentation Pack** that helps developers understand how common Open Payments API journeys can be represented as workflow documentation.

The initial scope focuses on a one-time payment flow:

1. discover wallet address metadata;
2. request an incoming payment grant;
3. create an incoming payment resource;
4. request a quote grant;
5. create a quote;
6. request an outgoing payment grant with explicit user interaction;
7. create an outgoing payment;
8. document continuation, cancellation, and error boundaries.

## Proposed Outcome

The deliverable would be a small open-source documentation package with:

- an Arazzo workflow map for a one-time Open Payments checkout;
- a companion Markdown explanation for developers;
- source links back to official Open Payments docs and API reference pages;
- a glossary for Open Payments, GNAP, grant, incoming payment, quote, and outgoing payment terms;
- a safety section that distinguishes documentation from live payment execution;
- a review checklist for Interledger or community maintainers.

## Why This Fits The Grant

Interledger's SDK grant program explicitly includes Arazzo flow documentation as a supported theme. Open Payments already has strong SDK/API docs, but a workflow-oriented layer could help developers see how individual API calls compose into a full payment journey.

This proposal is intentionally narrow. It targets documentation clarity first, avoids real payment handling, and creates a public artifact that can be reviewed before any deeper SDK or generator work.

## AI Assistance Disclosure Draft

```text
This proposal and draft documentation were prepared with AI assistance from the Make Money project. AI output is reviewed by Codex before being committed, and any submitted work would disclose AI assistance, models used where required, and review boundaries according to the Interledger SDK grant program guidance.
```

## Suggested Short Proposal Text

```text
I propose an Open Payments Arazzo Flow Documentation Pack focused on mapping common Open Payments API journeys into workflow documentation. The first package would cover a one-time payment flow from wallet address discovery through incoming payment, quote, outgoing payment grant, and outgoing payment creation, with explicit notes for interactive consent, continuation, cancellation, and error boundaries.

The deliverable would include a candidate Arazzo workflow map, a companion developer guide, source links to official Open Payments docs and API references, a glossary, and an acceptance checklist for review. It would not run live payments, connect wallets, handle funds, or present itself as official Interledger documentation until reviewed and accepted.

The work would disclose AI assistance and be fully reviewed before submission.
```
