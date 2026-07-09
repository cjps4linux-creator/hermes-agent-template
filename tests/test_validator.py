"""Tests for the Hermes Agent Template contract validator."""
from pathlib import Path
import subprocess
import sys
import textwrap

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_agent_contract.py"


def test_validator_reports_missing_section(tmp_path):
    contract = tmp_path / "contract.md"
    contract.write_text(
        textwrap.dedent(
            """
            id: test-agent
            version: 0.1.0
            """
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(contract)],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    combined = (result.stdout + result.stderr).lower()
    assert "missing" in combined or "failure" in combined or "required" in combined


def test_validator_passes_minimal_valid_contract(tmp_path):
    contract = tmp_path / "contract.md"
    contract.write_text(
        textwrap.dedent(
            """
            Identity
            Mission: Do one thing.
            Scope:
              does:
                - one thing
              does_not:
                - another thing
            Inputs
            Outputs
            Constraints
            Dependencies
            Tools
            Memory Model
            Failure Taxonomy
            Observability
            Evaluation
            """
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(contract)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
