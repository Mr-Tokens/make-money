import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectReadmeTests(unittest.TestCase):
    def test_chinese_and_english_readmes_explain_project_for_owner(self):
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")

        self.assertIn("Make Money", chinese)
        self.assertIn("Codex", chinese)
        self.assertIn("LLM-Wiki", chinese)
        self.assertIn("当前收入：0", chinese)
        self.assertIn("不是财务建议", chinese)
        self.assertNotIn("API", chinese)
        self.assertNotIn("私钥", chinese)
        self.assertNotIn(".env", chinese)
        self.assertLess(len(chinese.splitlines()), 90)

        self.assertIn("Make Money", english)
        self.assertIn("Codex", english)
        self.assertIn("LLM-Wiki", english)
        self.assertIn("Current revenue: 0", english)
        self.assertIn("not financial advice", english.lower())
        self.assertNotIn("API", english)
        self.assertNotIn("private key", english.lower())
        self.assertNotIn(".env", english)
        self.assertLess(len(english.splitlines()), 90)


if __name__ == "__main__":
    unittest.main()
