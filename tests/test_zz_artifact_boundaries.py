import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ArtifactBoundaryTests(unittest.TestCase):
    def test_python_cache_is_ignored_when_created_under_scripts(self):
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")

        self.assertIn("__pycache__/", gitignore)


if __name__ == "__main__":
    unittest.main()
