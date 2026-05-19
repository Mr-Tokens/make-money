# Web3Grants Verification

Date accessed: 2026-05-20
Subthread: `019e41f5-ab11-7bd0-af10-5d932fb6551f`
Nickname: James
Task: Web3Grants Verification

## Sources

| Source | URL | Evidence captured |
|--------|-----|-------------------|
| Web3Grants API | https://www.web3grants.co/api/grants | Public JSON grant dataset available without login or payment. Includes `status`, `website`, funding topics, deadline fields, and funding ranges. |
| Avalanche Research Grants | https://www.avax.network/about/blog/research-grants-avalanche-network-economics | Official Avalanche Foundation post dated 2026-04-29. Applications open for up to `$50,000` in research grants; deadline Monday June 1st, 2026. |
| Interledger Open Payments SDK grant | https://interledger.org/grant/open-payments-sdk | Official Interledger Foundation page. Open from April 1st, rolling review until budget awarded; individuals and organizations not subject to US sanctions are eligible. |

## Verification Result

Web3Grants is usable as a research multiplier.

It should not be treated as a source of truth. It is useful for candidate discovery because its API is public and can be filtered. Every candidate still needs direct official-source verification.

## Candidate Signals

### Tether Developer Grants / Bounties

Web3Grants lists Tether Developer Grants as active. This reinforces, but does not replace, the official Tether verification already captured in [Tether Template Wallet Verification](2026-05-20-tether-template-wallet-verification.md).

### Avalanche Foundation Research Grants

Potential fit:

- no-capital research proposal path;
- up to `$50,000` according to the official Avalanche post;
- independent scholars are eligible;
- deadline: Monday June 1st, 2026.

Weakness:

- scope is academic and 12-month milestone based;
- not ideal for the first fast feedback loop;
- would require a rigorous research proposal and researcher credentials.

### Interledger Open Payments SDK Grant Program

Potential fit:

- no-capital developer grant path;
- SDK, documentation, security-spec support, library, and tooling scope;
- awards listed by task category, including up to `$25,000` for some SDK/spec support tasks;
- rolling review until the budget is awarded.

Weakness:

- requires deeper technical scoping;
- may need 3 to 12 month work plan;
- application and payment details are human-only.

## Manager Interpretation

Web3Grants should be used in Batch 002 as a filterable source, especially for:

- active status;
- official-domain source URLs;
- developer/tooling/documentation topics;
- visible deadlines;
- no-capital proposal opportunities.

It should not displace Tether as the first execution target. Its immediate value is to create the next candidate pool after the Tether application pack is drafted.

## Next Scan Action

Pull active rows from the Web3Grants API and filter for:

- official project/domain links;
- `research`, `bounty`, `developer`, `documentation`, `open source`, `SDK`, or `tooling`;
- visible deadlines that have not passed;
- no startup traction, KYC-heavy, deposit, paid access, or wallet-signing requirement in the first action.
