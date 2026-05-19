# Make Money LLM-Wiki Design

Date: 2026-05-20
Status: Draft for user review

## Purpose

Build a local LLM-maintained knowledge base for the Make Money project. The system should record public wallet addresses, research money-making opportunities, preserve raw sources, turn useful findings into interlinked wiki pages, and keep every experiment auditable for future agents and users.

This project is experimental and must treat capital preservation, scam avoidance, and transparent recordkeeping as first-class goals. No private keys, seed phrases, passwords, browser wallet sessions, or signing authority are ever stored in the project.

## Source Ideas

The design follows the LLM-Wiki pattern from Andrej Karpathy's gist:

- Raw sources are immutable source material.
- The wiki is a persistent Markdown synthesis layer maintained by the LLM.
- A schema file such as `AGENTS.md` defines conventions, workflows, and guardrails.
- `index.md` is the content map.
- `log.md` is the chronological append-only activity trail.
- Regular ingest, query, and lint passes keep the knowledge base useful.

The design also borrows a few implementation ideas from practical LLM-Wiki scaffolds:

- Keep provenance explicit so wiki claims can be traced back to raw files.
- Use a manifest for raw sources instead of relying on filenames alone.
- Start with direct Markdown navigation and avoid vector/RAG tooling until the wiki is too large to inspect comfortably.
- Treat writeback as mandatory: decisions, strategy changes, experiment results, and risk findings should be written into the wiki, not left only in chat.

Reference sources used for this design:

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://github.com/Ss1024sS/LLM-wiki

## Directory Layout

The LLM-Wiki lives under a single root folder:

```text
llm-wiki/
  AGENTS.md
  wallets.md
  raw/
    README.md
    manifest.md
    sources/
  wiki/
    index.md
    log.md
    current-status.md
    strategies/
    protocols/
    risks/
    experiments/
    glossaries/
```

The repository root stays small. Future code, scripts, dashboards, or automation tools may live outside `llm-wiki/`, but the knowledge system itself is contained in `llm-wiki/`.

## Initial Wallet Records

`llm-wiki/wallets.md` records public addresses only:

| Chain | Public address | Notes |
| --- | --- | --- |
| Ethereum | `0x3c98bE78f1D84774637481e613e5B1d063BA806b` | EVM address shared with Base and Linea |
| Base | `0x3c98bE78f1D84774637481e613e5B1d063BA806b` | Same EVM address |
| Linea | `0x3c98bE78f1D84774637481e613e5B1d063BA806b` | Same EVM address |
| Bitcoin | `bc1qeqgmg34p8j85w2gcvzadc4azyr9ujwqj72uxnr` | Public receive address |
| Solana | `EzGu4B1C6tsppefS9ZT8AQykrtgqQUvrkGmaxMksYA1S` | Public address |

## Agent Safety Model

Agents may:

- Research protocols, rewards, quests, grants, bounties, and airdrop opportunities.
- Save source material under `llm-wiki/raw/sources/` and register it in `llm-wiki/raw/manifest.md`.
- Write and update wiki pages with citations to raw sources.
- Produce step-by-step instructions for the human wallet owner.
- Analyze public wallet state, balances, permissions, and transactions.
- Create local scripts for read-only monitoring and simulation.

Agents must not:

- Request, store, infer, or handle private keys, seed phrases, passwords, keystore files, or 2FA secrets.
- Connect to MetaMask or any wallet as the user.
- Sign, approve, bridge, swap, stake, lend, borrow, mint, claim, or transfer funds without the human executing the wallet action.
- Treat expected returns as guaranteed.
- Recommend strategies without cost, risk, success criteria, and exit criteria.

## Wiki Page Types

Strategy pages live in `llm-wiki/wiki/strategies/`. Each page should include:

- Summary
- Opportunity class
- Chains and required wallets
- Capital requirement
- Estimated non-capital cost, including time and gas
- Risk model
- Execution steps
- Human signing checklist
- Success criteria
- Exit criteria
- Source links
- Experiment links

Protocol pages live in `llm-wiki/wiki/protocols/`. Each page should include:

- What the protocol does
- Supported chains
- Relevant contracts or official links
- Reward or incentive mechanics
- Known risks
- Source links
- Related strategies

Risk pages live in `llm-wiki/wiki/risks/`. Each page should explain a reusable risk pattern, such as infinite approvals, phishing, malicious RPCs, bridged-asset risk, smart contract risk, oracle risk, liquidation risk, or sybil filtering.

Experiment pages live in `llm-wiki/wiki/experiments/`. Each page should record a concrete attempt:

- Hypothesis
- Date started
- Wallet and chain
- Budget
- Steps taken
- Transactions or human actions
- Result
- Lessons learned
- Links to strategy, protocol, and raw sources

## Operations

### Ingest

When a new source is found:

1. Save the source or a source note under `llm-wiki/raw/sources/`.
2. Add an entry to `llm-wiki/raw/manifest.md` with title, URL, date accessed, file path, and source type.
3. Create or update relevant wiki pages.
4. Update `llm-wiki/wiki/index.md`.
5. Append an entry to `llm-wiki/wiki/log.md`.

### Query

When answering a project question:

1. Read `llm-wiki/wiki/index.md` first.
2. Read the relevant wiki pages.
3. Check raw sources when a claim affects money, wallet safety, or execution.
4. Answer with source references.
5. If the answer creates durable knowledge, write it back to the wiki.

### Lint

Periodically inspect the wiki for:

- Stale claims.
- Missing raw provenance.
- Strategy pages without risk or exit criteria.
- Orphan pages not linked from `index.md`.
- Experiments without results.
- Wallet-related actions missing a human signing checklist.

## First Strategy Scope

The first strategies should prioritize low-capital or no-capital paths:

- Airdrop and quest research.
- Developer bounties and grants.
- Testnet participation.
- Read-only wallet hygiene and authorization checks.
- Low-cost onchain identity and reputation building.

Higher-risk DeFi strategies such as leverage, lending loops, illiquid liquidity pools, memecoin trading, MEV, or automated trading should not be first-wave strategies.

## Success Criteria

The v0 system is successful when:

- Future agents can read `llm-wiki/AGENTS.md` and know how to operate the project safely.
- Public wallet addresses are recorded without any secrets.
- Raw sources can be stored and traced from wiki pages.
- Every strategy page includes risk, cost, success criteria, and exit criteria.
- `index.md` and `log.md` make recent activity and available knowledge easy to find.
- No execution step requires the agent to hold wallet signing authority.

## Project Decisions

- Initialize this project as a git repository so the wiki has history, diffs, and rollback.
- Raw captures should store a short source note for every source. When practical and allowed, also store a Markdown or text copy of the source.
- First-stage automation is limited to read-only monitoring, data collection, and simulation. It must not prepare or submit transactions.
