# Proposed Acceptance Checklist

This checklist is for scope discussion with Tether. It is not an official Tether acceptance list.

## Bounty Gap

The bounty page says WDK starter templates are currently available for React Native, while developers using frameworks such as Next.js, Vue, Svelte, Angular, or Flutter must build integrations from scratch.

The proposed v0.1 closes one part of that gap: a Next.js starter path.

## Checklist

- [ ] The repository uses Next.js and TypeScript.
- [ ] A developer can clone the repository and run the mock demo locally.
- [ ] The default demo requires no real wallet connection.
- [ ] No private keys, seed phrases, wallet passwords, or real credentials are committed.
- [ ] `.env.example` documents only safe placeholder values.
- [ ] The codebase separates wallet UI, wallet state, and WDK-oriented adapter boundaries.
- [ ] Mock data is clearly labeled and cannot be confused with real balances.
- [ ] The README explains the purpose of mock mode.
- [ ] The README explains how a real WDK integration would be added after scope approval.
- [ ] The architecture note explains client/server boundaries in Next.js.
- [ ] The template includes a path for adding additional chains or modules.
- [ ] The template avoids live signing, broadcasting, swaps, bridging, or fund movement.
- [ ] The final package includes a short limitations section.
- [ ] The final package links back to official WDK documentation.

## Review Questions For Tether

1. Should the first version include only mock mode, or a read-only WDK example as well?
2. Which framework target is preferred first: Next.js, Vue, Svelte, Angular, or Flutter?
3. Which WDK module should be demonstrated first?
4. Should the template be hosted as a demo, or is a repository plus local run instructions enough?
5. Are there brand, license, or naming requirements for the starter repository?
