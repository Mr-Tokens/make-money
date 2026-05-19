# Arazzo Flow Sketch

Status: proof-of-work sketch, not official documentation

## Candidate Workflow

Name: `openPaymentsOneTimePayment`

Goal: document the sequence a developer follows to accept a one-time payment with Open Payments.

## Flow Map

| Step | Open Payments action | Source doc | Arazzo role |
|------|----------------------|------------|-------------|
| 1 | Get wallet address info | Wallet address / Open Payments docs | Establish receiver wallet metadata, resource server, and auth server. |
| 2 | Request incoming payment grant | Create incoming payment grant request | Authorize incoming payment resource creation. |
| 3 | Create incoming payment | Create incoming payment | Create the receiver-side incoming payment resource and amount boundary. |
| 4 | Request quote grant | Create quote grant request | Authorize quote creation for the payment path. |
| 5 | Create quote | Create a quote | Calculate payment terms before outgoing authorization. |
| 6 | Request outgoing payment grant | Create outgoing payment grant request | Request sender-side grant with explicit interactive consent. |
| 7 | Continue outgoing grant | Continue a grant request | Complete grant flow after user interaction when needed. |
| 8 | Create outgoing payment | Create outgoing payment | Initiate the outgoing payment within grant and quote limits. |
| 9 | Read payment state | Get outgoing payment / Get incoming payment | Document status verification and reconciliation. |

## Important Documentation Boundaries

- Outgoing payment grants are interactive and require explicit user consent.
- Incoming payment resources must exist before payments can be sent to a wallet address.
- The flow sketch should use sample values only.
- The pack should not include real wallet credentials, client keys, access tokens, or private material.
- Any runnable example should use a test wallet and separate human approval before execution.

## Candidate Arazzo Artifact Shape

```yaml
arazzo: 1.0.1
info:
  title: Open Payments One-Time Payment Flow
  version: 0.1.0
sourceDescriptions:
  - name: openPayments
    url: https://openpayments.dev/
    type: openapi
workflows:
  - workflowId: openPaymentsOneTimePayment
    summary: Document the steps for a one-time Open Payments flow.
    dependsOn: []
    steps:
      - stepId: getWalletAddress
      - stepId: requestIncomingPaymentGrant
      - stepId: createIncomingPayment
      - stepId: requestQuoteGrant
      - stepId: createQuote
      - stepId: requestOutgoingPaymentGrant
      - stepId: continueOutgoingGrant
      - stepId: createOutgoingPayment
      - stepId: verifyPaymentState
```

This sketch is intentionally incomplete. The grant proposal should ask Interledger whether they prefer:

- one end-to-end Arazzo workflow;
- separate workflows for incoming, quote, and outgoing flows;
- examples tied to existing Open Payments OpenAPI operation IDs;
- a docs-only pack or a docs-plus-validation setup.
