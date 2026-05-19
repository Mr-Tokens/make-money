import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELECTED_SKILLS = {
    "ai-seo",
    "community-marketing",
    "content-strategy",
    "free-tools",
    "launch",
    "product-marketing",
    "social",
}


class MarketingSkillsTests(unittest.TestCase):
    def test_only_selected_marketing_skills_are_installed(self):
        lock = json.loads((ROOT / "skills-lock.json").read_text(encoding="utf-8"))
        installed = set(lock["skills"].keys())

        self.assertEqual(installed, SELECTED_SKILLS)

        for skill in SELECTED_SKILLS:
            self.assertTrue((ROOT / ".agents" / "skills" / skill / "SKILL.md").exists())

    def test_product_marketing_context_exists(self):
        context = (ROOT / ".agents" / "product-marketing.md").read_text(encoding="utf-8")

        self.assertIn("Make Money", context)
        self.assertIn("zero-capital", context)
        self.assertIn("LLM-Wiki", context)
        self.assertNotIn("MINIMAX_API_KEY=", context)
        self.assertNotIn("MIMO_API_KEY=", context)


if __name__ == "__main__":
    unittest.main()
