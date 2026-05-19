import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProviderPolicyTests(unittest.TestCase):
    def test_active_minimax_provider_policy_excludes_highspeed(self):
        providers = json.loads((ROOT / "delegation" / "providers.example.json").read_text(encoding="utf-8"))
        env_example = (ROOT / ".env.example").read_text(encoding="utf-8")

        self.assertEqual(providers["minimax"]["default_model"], "MiniMax-M2.7")
        self.assertNotIn("minimax-fast", providers)
        self.assertNotIn("highspeed", json.dumps(providers))
        self.assertNotIn("MINIMAX_FAST_MODEL", env_example)
        self.assertNotIn("highspeed", env_example)

    def test_delegation_cli_rejects_minimax_fast_provider(self):
        result = subprocess.run(
            [
                sys.executable,
                "scripts/delegate_task.py",
                "--provider",
                "minimax-fast",
                "--type",
                "research",
                "--title",
                "No fast provider",
                "--prompt",
                "This should be rejected.",
                "--dry-run",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid choice", result.stderr)


if __name__ == "__main__":
    unittest.main()
