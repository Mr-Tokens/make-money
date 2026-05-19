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
        self.assertNotIn("我是", chinese)
        self.assertNotIn("我的任务", chinese)
        self.assertNotIn("你的角色", chinese)
        self.assertNotIn("最高权限", chinese)
        self.assertNotIn("不是在追热点", chinese)
        self.assertNotIn("把故事做出来", chinese)
        self.assertNotIn("复利的收入系统", chinese)
        self.assertLess(len(chinese.splitlines()), 90)

        self.assertIn("Make Money", english)
        self.assertIn("Codex", english)
        self.assertIn("LLM-Wiki", english)
        self.assertIn("Current revenue: 0", english)
        self.assertIn("not financial advice", english.lower())
        self.assertNotIn("API", english)
        self.assertNotIn("private key", english.lower())
        self.assertNotIn(".env", english)
        self.assertNotIn("This is Codex", english)
        self.assertNotIn("Your role", english)
        self.assertNotIn("highest-authority observer", english)
        self.assertNotIn("My job", english)
        self.assertNotIn("tell a story", english)
        self.assertNotIn("chasing trends", english)
        self.assertNotIn("income system that compounds", english)
        self.assertLess(len(english.splitlines()), 90)


if __name__ == "__main__":
    unittest.main()
