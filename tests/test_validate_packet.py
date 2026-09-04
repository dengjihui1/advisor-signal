import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_packet import _errors


def valid_packet():
    return {
        "schema_version": "0.1",
        "applicant": {"profile_sources": ["https://portfolio.invalid/app"]},
        "supervisor": {"sources": ["https://university.invalid/lab"]},
        "fit": {"score": 70, "confidence": "medium"},
        "papers": [{"title": "Paper", "url": "https://doi.org/10.0000/test"}],
        "deliverables": {"email": "Subject: Prospective PhD opportunity\n\nWould you be open to discussing doctoral supervision opportunities?"},
        "unknowns": []
    }


class ValidatorTests(unittest.TestCase):
    def test_demo_packet_passes(self):
        packet = json.loads(Path("demo/packet.json").read_text(encoding="utf-8"))
        self.assertEqual(_errors(packet), [])

    def test_three_papers_fail(self):
        packet = valid_packet()
        packet["papers"] = packet["papers"] * 3
        self.assertIn("at most two papers are allowed", _errors(packet))

    def test_placeholder_email_fails(self):
        packet = valid_packet()
        packet["deliverables"]["email"] = "Subject: Prospective PhD opportunity\nDear Dr. Example, contact your email"
        self.assertTrue(any("placeholder" in error for error in _errors(packet)))

    def test_cli_returns_zero_for_demo(self):
        result = subprocess.run([sys.executable, "scripts/validate_packet.py", "demo/packet.json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
