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

    def test_root_agent_rules_allow_explicit_env_credentials_only(self):
        rules = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("explicitly provides API credentials", rules)
        self.assertIn(".env", rules)
        self.assertIn("never commit", rules.lower())


if __name__ == "__main__":
    unittest.main()
