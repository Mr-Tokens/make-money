import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from delegation_lib import (
    load_env_file,
    load_providers,
    redact_secrets,
    resolve_provider,
)


class DelegationLibTests(unittest.TestCase):
    def test_redact_secrets_masks_known_token_shapes(self):
        text = (
            "minimax sk-test-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
            "mimo tp-test-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb "
            "bearer Authorization: Bearer secret-token-value"
        )

        redacted = redact_secrets(text)

        self.assertNotIn("sk-test-aaaaaaaa", redacted)
        self.assertNotIn("tp-test-bbbbbbbb", redacted)
        self.assertNotIn("secret-token-value", redacted)
        self.assertIn("[REDACTED_TOKEN]", redacted)

    def test_load_env_file_reads_simple_key_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            env_path = Path(tmp) / ".env"
            env_path.write_text(
                "MINIMAX_API_KEY = example-local-key\n"
                "MIMO_BASE_URL='https://token-plan-sgp.xiaomimimo.com/v1'\n"
                "# comment\n",
                encoding="utf-8",
            )

            values = load_env_file(env_path)

        self.assertEqual(values["MINIMAX_API_KEY"], "example-local-key")
        self.assertEqual(values["MIMO_BASE_URL"], "https://token-plan-sgp.xiaomimimo.com/v1")

    def test_resolve_provider_uses_env_over_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            providers_path = Path(tmp) / "providers.example.json"
            providers_path.write_text(
                json.dumps(
                    {
                        "mimo": {
                            "base_url_env": "MIMO_BASE_URL",
                            "api_key_env": "MIMO_API_KEY",
                            "model_env": "MIMO_MODEL",
                            "default_base_url": "https://api.xiaomimimo.com/v1",
                            "default_model": "mimo-v2.5-pro",
                            "token_limit_field": "max_completion_tokens",
                        }
                    }
                ),
                encoding="utf-8",
            )

            providers = load_providers(providers_path)
            provider = resolve_provider(
                "mimo",
                providers,
                {
                    "MIMO_BASE_URL": "https://token-plan-sgp.xiaomimimo.com/v1",
                    "MIMO_API_KEY": "local-key",
                    "MIMO_MODEL": "mimo-v2.5-pro",
                },
                require_key=True,
            )

        self.assertEqual(provider["base_url"], "https://token-plan-sgp.xiaomimimo.com/v1")
        self.assertEqual(provider["api_key"], "local-key")
        self.assertEqual(provider["model"], "mimo-v2.5-pro")

    def test_write_task_redacts_prompt_and_sources(self):
        import delegation_lib

        with tempfile.TemporaryDirectory() as tmp:
            old_tasks_dir = delegation_lib.TASKS_DIR
            delegation_lib.TASKS_DIR = Path(tmp) / "tasks"
            try:
                record = {
                    "task_id": "task-1",
                    "created_at": "2026-05-20T00:00:00+00:00",
                    "updated_at": "2026-05-20T00:00:00+00:00",
                    "provider": "mimo",
                    "model": "mimo-v2.5-pro",
                    "task_type": "research",
                    "title": "Secret test",
                    "input_prompt": "token sk-test-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sources": ["api-key: tp-test-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"],
                    "status": "pending",
                }

                path = delegation_lib.write_task(record, "pending")
                saved = path.read_text(encoding="utf-8")
            finally:
                delegation_lib.TASKS_DIR = old_tasks_dir

        self.assertIn("[REDACTED_TOKEN]", saved)
        self.assertNotIn("sk-test-aaaaaaaa", saved)
        self.assertNotIn("tp-test-bbbbbbbb", saved)


if __name__ == "__main__":
    unittest.main()
