import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "deliverables" / "tether-template-wallet-application-pack-v0.1"


class DeliverableTests(unittest.TestCase):
    def test_tether_application_pack_exists_and_has_required_files(self):
        required = [
            "README.md",
            "application-brief.md",
            "scope-and-milestones.md",
            "safety-and-human-actions.md",
            "acceptance-checklist.md",
            "repo-readme-outline.md",
            "evidence.md",
            "human-submission-checklist.md",
            "submission-form-draft.md",
        ]

        missing = [name for name in required if not (PACK / name).exists()]

        self.assertEqual(missing, [])

    def test_tether_application_pack_preserves_safety_and_claim_boundaries(self):
        combined = "\n".join(path.read_text(encoding="utf-8") for path in PACK.glob("*.md"))

        self.assertIn("Bounty application: submitted", combined)
        self.assertIn("Bounty acceptance: none", combined)
        self.assertIn("Revenue: 0", combined)
        self.assertIn("submitted, pending review", combined)
        self.assertIn("Thank you for your application!", combined)
        self.assertIn("Tether submission confirmation note", combined)
        self.assertIn("Relevant Experience Draft", combined)
        self.assertIn("https://github.com/Mr-Tokens/make-money", combined)
        self.assertIn("Do not paste private credentials", combined)
        self.assertIn("Do not claim a bounty is earned or awarded", combined)
        self.assertIn("No automated system handles funds", combined)
        self.assertIn("Dedicated project email", combined)
        self.assertIn("Human legal name if required", combined)
        self.assertIn("Mr.Tokens", combined)
        private_email = "mr.tokens" + "@" + "qq.com"
        self.assertNotIn(private_email, combined)
        self.assertNotIn("guaranteed", combined.lower())
        self.assertNotIn("risk-free", combined.lower())


if __name__ == "__main__":
    unittest.main()
