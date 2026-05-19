import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import delegation_lib


class ReviewTaskCliTests(unittest.TestCase):
    def test_review_cli_approves_completed_task(self):
        record = {
            "task_id": "cli-review-test",
            "created_at": "2026-05-20T00:00:00+00:00",
            "updated_at": "2026-05-20T00:00:00+00:00",
            "provider": "mimo",
            "model": "mimo-v2.5-pro",
            "task_type": "summary",
            "title": "CLI review test",
            "input_prompt": "hello",
            "sources": [],
            "worker_output": "result",
            "status": "completed",
        }
        completed_path = delegation_lib.write_task(record, "completed")
        self.addCleanup(completed_path.unlink, missing_ok=True)

        result = subprocess.run(
            [
                sys.executable,
                "scripts/review_task.py",
                "--task-id",
                "cli-review-test",
                "--decision",
                "approved",
                "--reason",
                "source-backed",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        reviewed = json.loads(completed_path.read_text(encoding="utf-8"))
        self.assertEqual(reviewed["review"]["decision"], "approved")
        self.assertEqual(reviewed["review"]["reason"], "source-backed")


if __name__ == "__main__":
    unittest.main()
