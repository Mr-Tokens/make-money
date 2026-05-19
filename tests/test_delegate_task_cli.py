import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
PENDING_DIR = ROOT / "delegation" / "tasks" / "pending"
from test_paths import make_artifact_dir, remove_artifact_dir


class DelegateTaskCliTests(unittest.TestCase):
    def test_writing_dry_run_creates_pending_task_without_api_key(self):
        artifact_dir = make_artifact_dir("delegate-writing-cli-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        task_dir = artifact_dir / "tasks"
        env = os.environ.copy()
        env["DELEGATION_TASKS_DIR"] = str(task_dir)
        env["PYTHONDONTWRITEBYTECODE"] = "1"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/delegate_task.py",
                "--provider",
                "mimo",
                "--type",
                "writing",
                "--title",
                "Writing dry run",
                "--prompt",
                "Draft a lighter README.",
                "--dry-run",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            env=env,
        )

        created = list((task_dir / "pending").glob("*.json"))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(created), 1)

        record = json.loads(created[0].read_text(encoding="utf-8"))
        self.assertEqual(record["task_type"], "writing")

    def test_dry_run_creates_pending_task_without_api_key(self):
        artifact_dir = make_artifact_dir("delegate-cli-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        task_dir = artifact_dir / "tasks"
        before = set(PENDING_DIR.glob("*.json"))
        env = os.environ.copy()
        env["DELEGATION_TASKS_DIR"] = str(task_dir)
        env["PYTHONDONTWRITEBYTECODE"] = "1"

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
            env=env,
        )

        after = set(PENDING_DIR.glob("*.json"))
        created = list((task_dir / "pending").glob("*.json"))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Dry run task saved:", result.stdout)
        self.assertEqual(after, before)
        self.assertEqual(len(created), 1)

        record = json.loads(created[0].read_text(encoding="utf-8"))
        self.assertEqual(record["status"], "pending")
        self.assertEqual(record["provider"], "mimo")
        self.assertEqual(record["model"], "mimo-v2.5-pro")
        self.assertNotIn("api_key", record)


if __name__ == "__main__":
    unittest.main()
