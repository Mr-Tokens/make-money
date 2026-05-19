import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
sys.dont_write_bytecode = True
from test_paths import make_artifact_dir, remove_artifact_dir

import delegation_lib


class ReviewTaskCliTests(unittest.TestCase):
    def test_review_cli_approves_completed_task(self):
        artifact_dir = make_artifact_dir("review-cli-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        task_dir = artifact_dir / "tasks"
        old_tasks_dir = delegation_lib.TASKS_DIR
        delegation_lib.TASKS_DIR = task_dir
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
        try:
            completed_path = delegation_lib.write_task(record, "completed")
        finally:
            delegation_lib.TASKS_DIR = old_tasks_dir
        env = os.environ.copy()
        env["DELEGATION_TASKS_DIR"] = str(task_dir)
        env["PYTHONDONTWRITEBYTECODE"] = "1"

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
            env=env,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        reviewed = json.loads(completed_path.read_text(encoding="utf-8"))
        self.assertEqual(reviewed["review"]["decision"], "approved")
        self.assertEqual(reviewed["review"]["reason"], "source-backed")


if __name__ == "__main__":
    unittest.main()
