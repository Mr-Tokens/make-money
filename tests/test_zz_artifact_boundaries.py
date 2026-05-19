import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ArtifactBoundaryTests(unittest.TestCase):
    def test_tests_do_not_create_python_cache_under_scripts(self):
        self.assertFalse((ROOT / "scripts" / "__pycache__").exists())


if __name__ == "__main__":
    unittest.main()
