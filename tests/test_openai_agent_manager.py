import subprocess
import sys
import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import openai_agent_manager


class OpenAIAgentManagerTests(unittest.TestCase):
    def test_project_skills_are_loaded_from_agents_directory(self):
        skills = openai_agent_manager.load_project_skills()
        names = {skill.name for skill in skills}
        lock = json.loads((ROOT / "skills-lock.json").read_text(encoding="utf-8"))

        self.assertEqual(names, set(lock["skills"].keys()))
        self.assertIn("product-marketing", names)
        self.assertIn("content-strategy", names)
        self.assertIn("social", names)

    def test_manager_instructions_include_project_boundaries_and_skills(self):
        instructions = openai_agent_manager.build_manager_instructions()

        self.assertIn(".agents/skills", instructions)
        self.assertIn("LLM-Wiki", instructions)
        self.assertIn("must not connect wallets", instructions)
        self.assertIn("tests/artifacts", instructions)
        self.assertIn("product-marketing", instructions)

    def test_sdk_manager_agent_builds_without_api_call_inside_uv(self):
        script = (
            "from scripts.openai_agent_manager import build_manager_agent;"
            "agent = build_manager_agent();"
            "print(agent.name);"
            "print(len(agent.tools));"
            "print(','.join(sorted(tool.name for tool in agent.tools)))"
        )

        result = subprocess.run(
            ["uv", "run", "python", "-c", script],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.strip().splitlines()
        self.assertEqual(lines[0], "Make Money Manager")
        self.assertGreaterEqual(int(lines[1]), 8)
        self.assertIn("read_project_skill", lines[2])
        self.assertIn("list_project_skills", lines[2])
        self.assertIn("owner_facing_writing_worker", lines[2])

    def test_worker_agent_has_skill_reader_tool(self):
        script = (
            "from scripts.openai_agent_manager import build_worker_agent;"
            "worker = build_worker_agent('Test Worker', 'Inspect skills.', skill_names=('content-strategy',));"
            "print(','.join(sorted(tool.name for tool in worker.tools)))"
        )

        result = subprocess.run(
            ["uv", "run", "python", "-c", script],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        tool_names = set(result.stdout.strip().split(","))

        self.assertIn("read_project_skill", tool_names)
        self.assertIn("list_project_skills", tool_names)

    def test_marketing_worker_instructions_include_product_context(self):
        instructions = openai_agent_manager.build_worker_instructions(
            "Create public marketing drafts.",
            skill_names=("product-marketing", "social"),
            include_product_context=True,
        )

        self.assertIn("Canonical product marketing context", instructions)
        self.assertIn("Make Money", instructions)
        self.assertIn("zero-capital", instructions)

    def test_skill_reader_rejects_path_traversal(self):
        with self.assertRaises(ValueError):
            openai_agent_manager.read_project_skill_text("../product-marketing")

        with self.assertRaises(ValueError):
            openai_agent_manager.read_project_skill_text("missing-skill")

    def test_dry_run_cli_builds_manager_agent_inside_uv(self):
        result = subprocess.run(
            ["uv", "run", "python", "scripts/openai_agent_manager.py", "dry-run"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"agent": "Make Money Manager"', result.stdout)

    def test_sandbox_manager_agent_can_load_project_skill_source_inside_uv(self):
        script = (
            "from scripts.openai_agent_manager import build_sandbox_manager_agent;"
            "agent = build_sandbox_manager_agent();"
            "print(agent.name)"
        )

        result = subprocess.run(
            ["uv", "run", "python", "-c", script],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Make Money Sandbox Manager")

    def test_safe_sandbox_sources_exclude_local_secrets_and_runtime_dirs(self):
        sources = openai_agent_manager.safe_sandbox_sources()
        root = ROOT.resolve()

        self.assertNotIn("repo", sources)
        self.assertIn("skills", sources)
        self.assertIn("llm-wiki", sources)
        for src in sources.values():
            resolved = Path(src).resolve()
            relative_parts = set(resolved.relative_to(root).parts)
            self.assertNotEqual(resolved, root)
            self.assertNotIn(".env", relative_parts)
            self.assertNotIn("secret", relative_parts)
            self.assertNotIn(".venv", relative_parts)


if __name__ == "__main__":
    unittest.main()
