import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
sys.dont_write_bytecode = True
from test_paths import make_artifact_dir, remove_artifact_dir

from delegation_lib import (
    TASK_TYPES,
    load_env_file,
    load_providers,
    read_worker_template,
    redact_secrets,
    resolve_provider,
)


class DelegationLibTests(unittest.TestCase):
    def test_writing_worker_template_is_available(self):
        self.assertIn("writing", TASK_TYPES)
        template = read_worker_template("writing")

        self.assertIn("marketing", template.lower())
        self.assertIn("README", template)

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
        artifact_dir = make_artifact_dir("env-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        env_path = artifact_dir / ".env"
        try:
            env_path.write_text(
                "MINIMAX_API_KEY = example-local-key\n"
                "MIMO_BASE_URL='https://token-plan-sgp.xiaomimimo.com/v1'\n"
                "# comment\n",
                encoding="utf-8",
            )

            values = load_env_file(env_path)
        finally:
            pass

        self.assertEqual(values["MINIMAX_API_KEY"], "example-local-key")
        self.assertEqual(values["MIMO_BASE_URL"], "https://token-plan-sgp.xiaomimimo.com/v1")

    def test_resolve_provider_uses_env_over_defaults(self):
        artifact_dir = make_artifact_dir("providers-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        providers_path = artifact_dir / "providers.example.json"
        try:
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
        finally:
            pass

        self.assertEqual(provider["base_url"], "https://token-plan-sgp.xiaomimimo.com/v1")
        self.assertEqual(provider["api_key"], "local-key")
        self.assertEqual(provider["model"], "mimo-v2.5-pro")

    def test_write_task_redacts_prompt_and_sources(self):
        import delegation_lib

        artifact_dir = make_artifact_dir("write-task-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        old_tasks_dir = delegation_lib.TASKS_DIR
        delegation_lib.TASKS_DIR = artifact_dir / "tasks"
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

    def test_approve_and_reject_task_update_review_state(self):
        import delegation_lib

        artifact_dir = make_artifact_dir("review-lib-")
        self.addCleanup(remove_artifact_dir, artifact_dir)
        old_tasks_dir = delegation_lib.TASKS_DIR
        delegation_lib.TASKS_DIR = artifact_dir / "tasks"
        try:
            record = {
                "task_id": "task-2",
                "created_at": "2026-05-20T00:00:00+00:00",
                "updated_at": "2026-05-20T00:00:00+00:00",
                "provider": "minimax",
                "model": "MiniMax-M2.7",
                "task_type": "summary",
                "title": "Review test",
                "input_prompt": "hello",
                "sources": [],
                "worker_output": "result",
                "status": "completed",
            }
            delegation_lib.write_task(record, "completed")

            approved_path = delegation_lib.approve_task("task-2", "looks useful")
            approved = json.loads(approved_path.read_text(encoding="utf-8"))

            record["task_id"] = "task-3"
            delegation_lib.write_task(record, "completed")
            rejected_path = delegation_lib.reject_task("task-3", "unsupported claim")
            rejected = json.loads(rejected_path.read_text(encoding="utf-8"))
        finally:
            delegation_lib.TASKS_DIR = old_tasks_dir

        self.assertEqual(approved["status"], "completed")
        self.assertEqual(approved["review"]["decision"], "approved")
        self.assertEqual(rejected["status"], "rejected")
        self.assertEqual(rejected["review"]["decision"], "rejected")


if __name__ == "__main__":
    unittest.main()
