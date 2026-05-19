import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PENDING_DIR = ROOT / "delegation" / "tasks" / "pending"


class DelegateTaskCliTests(unittest.TestCase):
    def test_dry_run_creates_pending_task_without_api_key(self):
        before = set(PENDING_DIR.glob("*.json"))

        result = subprocess.run(
            [
                sys.executable,
                "scripts/delegate_task.py",
                "--provider",
                "mimo",
                "--type",
                "research",
                "--title",
                "Dry run from test",
                "--prompt",
                "Summarize safety rules.",
                "--dry-run",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        after = set(PENDING_DIR.glob("*.json"))
        created = list(after - before)
        for path in created:
            self.addCleanup(path.unlink)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Dry run task saved:", result.stdout)
        self.assertEqual(len(created), 1)

        record = json.loads(created[0].read_text(encoding="utf-8"))
        self.assertEqual(record["status"], "pending")
        self.assertEqual(record["provider"], "mimo")
        self.assertEqual(record["model"], "mimo-v2.5-pro")
        self.assertNotIn("api_key", record)


if __name__ == "__main__":
    unittest.main()
