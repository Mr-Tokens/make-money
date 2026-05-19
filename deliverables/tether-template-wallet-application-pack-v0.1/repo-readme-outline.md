# Future Repository README Outline

This is the proposed README structure for the future `tether-wdk-nextjs-template` repository if the bounty scope is accepted.

## README Shape

```md
# Tether WDK Next.js Template Wallet

Next.js starter template for exploring Tether WDK wallet application patterns.

## Status

Mock-first developer starter. No real wallet connection, signing, or fund movement.

## What This Is

A Next.js template that shows how a web wallet interface can organize WDK-oriented wallet flows, state, adapters, and documentation.

## What This Is Not

- Not a production wallet.
- Not a custody product.
- Not a transaction signing demo.
- Not a hosted financial service.

## Quick Start

```bash
npm install
npm run dev
```

## Mock Mode

Explain deterministic placeholder balances, addresses, history, and why mock mode is the default.

## Project Structure

Describe app routes, components, adapter layer, mock data, and docs.

## WDK Integration Path

Explain where real WDK modules can replace mock adapters after scope approval.

## Safety

Explain no private keys, no seed phrases, no signing, no transactions, no real funds.

## Extension Guide

How to add a chain, add a new flow, replace mock data, or migrate the pattern to another framework.

## License

MIT, unless Tether requests a different license.
```

## README Principles

- First screen explains status and safety.
- Setup is visible before deep architecture.
- Mock limitations are explicit.
- Extension path is clear but does not imply live wallet readiness.
- Official WDK docs are linked instead of copied.
