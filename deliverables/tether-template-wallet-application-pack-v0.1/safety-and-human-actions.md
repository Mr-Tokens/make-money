# Safety And Human Actions

## Safety Model

The proposed template uses a **mock-first, secrets-excluded** safety model.

The default demo should:

- run without a wallet connection;
- run without private keys or seed phrases;
- run without real RPC credentials;
- show deterministic placeholder balances and history;
- never sign or broadcast transactions;
- clearly label mock data as mock data.

## Agent Boundaries

Agents may:

- draft the application package;
- build documentation;
- create safe starter code after scope approval;
- write `.env.example` files;
- run local tests;
- prepare a reviewable repository.

Agents must not:

- submit the Tether application;
- agree to terms;
- complete KYC;
- provide payment details;
- claim a bounty is earned or awarded;
- connect wallets;
- sign messages or transactions;
- handle private keys, seed phrases, wallet passwords, or real secrets;
- move funds.

Do not claim a bounty is earned or awarded. No automated system handles funds.

## Human-Only Actions

| Action | Owner |
|--------|-------|
| Submit application form | Human |
| Provide identity, contact, and relevant experience details | Human |
| Agree to Tether grant terms | Human |
| Complete KYC or due diligence if requested | Human |
| Sign bounty agreement | Human |
| Join calls or direct communication with Tether | Human |
| Provide payout/payment details after acceptance | Human |
| Handle tax, legal, and jurisdiction review | Human |

## Risks

- Tether may reject the application.
- Tether may not respond.
- Tether may request a different framework or deeper implementation.
- Tether may require KYC, due diligence, or a written agreement.
- Application materials may not be confidential under Tether's terms.
- Bounty scope or availability can change.
- No payment is due unless Tether accepts deliverables under its process.

## Assumptions

- A Next.js template is acceptable as one of the framework gaps named by the bounty.
- A mock-first starter is acceptable for scope discussion.
- Tether will clarify expected real WDK depth before implementation.
- Human submission can happen without agents controlling wallets or funds.

## Claim Rule

Until Tether confirms acceptance or payment, the Make Money project records this as:

```text
Status: application package prepared
Revenue: 0
```
