import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLM_WIKI = ROOT / "llm-wiki"


class LlmWikiStructureTests(unittest.TestCase):
    def test_required_llm_wiki_files_exist(self):
        required_paths = [
            LLM_WIKI / "AGENTS.md",
            LLM_WIKI / "wallets.md",
            LLM_WIKI / "raw" / "README.md",
            LLM_WIKI / "raw" / "manifest.md",
            LLM_WIKI / "wiki" / "index.md",
            LLM_WIKI / "wiki" / "log.md",
            LLM_WIKI / "wiki" / "current-status.md",
            LLM_WIKI / "wiki" / "strategies" / "README.md",
            LLM_WIKI / "wiki" / "marketing" / "github-readme-style.md",
            LLM_WIKI / "wiki" / "protocols" / "README.md",
            LLM_WIKI / "wiki" / "protocols" / "execution-subthreads.md",
            LLM_WIKI / "wiki" / "protocols" / "manager-first-delegation.md",
            LLM_WIKI / "wiki" / "risks" / "README.md",
            LLM_WIKI / "wiki" / "experiments" / "README.md",
            LLM_WIKI / "wiki" / "glossaries" / "README.md",
        ]

        missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]

        self.assertEqual(missing, [])

    def test_wallets_record_public_addresses_only(self):
        wallets = (LLM_WIKI / "wallets.md").read_text(encoding="utf-8")

        self.assertIn("0x3c98bE78f1D84774637481e613e5B1d063BA806b", wallets)
        self.assertIn("bc1qeqgmg34p8j85w2gcvzadc4azyr9ujwqj72uxnr", wallets)
        self.assertIn("EzGu4B1C6tsppefS9ZT8AQykrtgqQUvrkGmaxMksYA1S", wallets)
        self.assertNotIn("private_key:", wallets.lower())
        self.assertNotIn("seed_phrase:", wallets.lower())
        self.assertNotIn("mnemonic:", wallets.lower())

    def test_manifest_tracks_initial_sources(self):
        manifest = (LLM_WIKI / "raw" / "manifest.md").read_text(encoding="utf-8")

        self.assertIn("Karpathy LLM-Wiki gist", manifest)
        self.assertIn("MiniMax model docs", manifest)
        self.assertIn("Mimo platform docs", manifest)
        self.assertIn("OpenAI Agents docs", manifest)
        self.assertIn("GitHub Trending README style references", manifest)
        self.assertIn("Tether Template Wallet submission confirmation", manifest)
        self.assertIn("Opportunity Scan Batch 002 source bundle", manifest)
        self.assertIn("Micro Cash Scan Batch 001 source bundle", manifest)
        self.assertIn("sh1pt Listen Notes PR draft source bundle", manifest)
        self.assertIn("Manager-first delegation correction", manifest)

    def test_github_readme_style_guide_protects_public_claims(self):
        style = (LLM_WIKI / "wiki" / "marketing" / "github-readme-style.md").read_text(encoding="utf-8")

        self.assertIn("Current status and revenue", style)
        self.assertIn("evidence", style.lower())
        self.assertIn("not an investment", style.lower())
        self.assertIn("public wallet addresses", style.lower())
        self.assertNotIn("highest authority observer", style)

    def test_execution_subthreads_protocol_keeps_safety_boundaries(self):
        protocol = (LLM_WIKI / "wiki" / "protocols" / "execution-subthreads.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("main thread remains responsible", protocol.lower())
        self.assertIn("Do not request or handle secrets", protocol)
        self.assertIn("Do not connect wallets", protocol)
        self.assertIn("Tether Verification", protocol)
        self.assertIn("manager integrated", protocol)

    def test_manager_first_delegation_protocol_keeps_manager_out_of_chores(self):
        protocol = (
            LLM_WIKI / "wiki" / "protocols" / "manager-first-delegation.md"
        ).read_text(encoding="utf-8")
        rules = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("delegate first", protocol.lower())
        self.assertIn("Mimo", protocol)
        self.assertIn("MiniMax", protocol)
        self.assertIn("public submission", protocol)
        self.assertIn("Workers may draft", protocol)
        self.assertIn("Before doing non-sensitive execution work directly", rules)

    def test_root_agent_rules_allow_explicit_env_credentials_only(self):
        rules = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("explicitly provides API credentials", rules)
        self.assertIn(".env", rules)
        self.assertIn("never commit", rules.lower())

    def test_current_status_tracks_worker_and_submission_state(self):
        status = (LLM_WIKI / "wiki" / "current-status.md").read_text(encoding="utf-8")
        smoke = (LLM_WIKI / "wiki" / "experiments" / "2026-05-20-provider-smoke.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("MiniMax `MiniMax-M2.7`: usable", status)
        self.assertIn("submitted and pending review", status)
        self.assertIn("Wait for Tether's review response", status)
        self.assertIn("MiniMax `MiniMax-M2.7`: usable", smoke)
        self.assertIn("non-high-speed", smoke)

    def test_batch_002_selects_interledger_without_revenue_claims(self):
        batch = (LLM_WIKI / "wiki" / "experiments" / "2026-05-20-opportunity-scan-batch-002.md").read_text(
            encoding="utf-8"
        )
        interledger = (
            LLM_WIKI / "wiki" / "experiments" / "2026-05-20-interledger-open-payments-arazzo-verification.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Interledger Open Payments SDK grant", batch)
        self.assertIn("second execution target", interledger)
        self.assertIn("Do not claim grant acceptance or revenue", interledger)
        self.assertIn("not submitted", interledger)

    def test_micro_cash_strategy_targets_small_real_payouts(self):
        strategy = (
            LLM_WIKI / "wiki" / "strategies" / "2026-05-20-micro-cash-sprint.md"
        ).read_text(encoding="utf-8")
        batch = (
            LLM_WIKI / "wiki" / "experiments" / "2026-05-20-micro-cash-scan-batch-001.md"
        ).read_text(encoding="utf-8")
        source = (
            LLM_WIKI / "raw" / "sources" / "2026-05-20-micro-cash-scan-batch-001-sources.md"
        ).read_text(encoding="utf-8")

        self.assertIn("5-20 USDT/USDC-equivalent", strategy)
        self.assertIn("profullstack/sh1pt#133", batch)
        self.assertIn("web3/web3.js", batch)
        self.assertIn("archived/read-only", batch)
        self.assertIn("No submission yet", batch)
        self.assertIn("Revenue remains `0`", batch)
        self.assertIn("Superteam Earn FAQ", source)

    def test_sh1pt_listennotes_pr_draft_records_submission_blocker(self):
        draft = (
            LLM_WIKI / "wiki" / "experiments" / "2026-05-20-sh1pt-listennotes-pr-draft.md"
        ).read_text(encoding="utf-8")
        status = (LLM_WIKI / "wiki" / "current-status.md").read_text(encoding="utf-8")

        self.assertIn("8d9f5ab02437b57d135ed42bcb8ed4dafb2e4b10", draft)
        self.assertIn("packages/outreach/listennotes", draft)
        self.assertIn("Not submitted", draft)
        self.assertIn("GitHub CLI account", draft)
        self.assertIn("Revenue remains `0`", draft)
        self.assertIn("project identity", status)


if __name__ == "__main__":
    unittest.main()
