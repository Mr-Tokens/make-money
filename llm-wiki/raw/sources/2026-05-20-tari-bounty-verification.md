# Tari Bounty Verification

Date accessed: 2026-05-20
Subthread: `019e41f5-aab3-7da2-981d-973ae138d630`
Nickname: Planck
Task: Tari Bounty Verification

## Sources

| Source | URL | Evidence captured |
|--------|-----|-------------------|
| Tari bounty board | https://github.com/tari-project/bounties | Public bounty board. Rules: comment intent, fork, submit PR with closing keyword, first PR that passes review and merges wins, payout in XTM. Board showed 35 bounties, `2,280,000 XTM`, last updated 2026-05-19 09:43 UTC. |
| Tari Universe issue #3111 | https://github.com/tari-project/universe/issues/3111 | Open issue: `[BUG] No Linux Support`, labeled `bounty`, `bounty-S`, `good first issue`; bounty title is "Update Linux Build Documentation", tier S, `15,000 XTM`. |
| Tari Universe PR #3183 | https://github.com/tari-project/universe/pull/3183 | Open competing PR for #3111. README-only update with multiple approval signals and review activity. |

## Verified Opportunity

Candidate: **Tari Universe #3111: Update Linux Build Documentation**

Initial manager decision: monitor, do not execute immediately.

Why it was interesting:

- It is public and GitHub-native.
- The work is documentation-oriented.
- It does not require capital to prepare.
- The issue explicitly says AI-assisted development is expected and encouraged.
- The bounty amount is visible as `15,000 XTM`.

Why it is not first:

- The bounty is already contested.
- The board marks the bounty as `PR Open`.
- PR #3183 appears to address the issue and has approvals.
- Tari's rule says the first PR that passes review and merges wins.
- A late duplicate README PR has high no-payout risk.

## Smallest Useful Deliverable If Reopened

Only proceed if maintainers explicitly invite more work. A useful scope would be:

- README-only Linux build documentation patch;
- correction/removal of `.deb` and `.AppImage` artifact claims;
- tested Linux build-from-source steps;
- evidence that the instructions were run in a Linux environment;
- no wallet, payout, or token handling in the PR itself.

## Human-Only Actions

- Comment on the GitHub issue to signal intent.
- Submit PR from a GitHub account if needed.
- Provide payout details only after acceptance.
- Handle any wallet address, token, tax, or payout action.

## Risks And Unknowns

- XTM value and liquidity are uncertain.
- Payment timing is uncertain.
- The current issue may be merged before Make Money can act.
- Documentation validation may require Linux environment time.
- A duplicate contribution can produce useful public work but no bounty.

## Manager Recommendation

Do not start coding blindly. If Tether stalls, check whether #3111 is still open and ask the maintainers whether additional Linux docs work would be useful given PR #3183. Otherwise, keep Tari as a backup GitHub-public contribution path.
