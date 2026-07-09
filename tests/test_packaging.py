"""Tests for Hermes Agent Template packaging and validator behavior."""
from pathlib import Path
import subprocess
import sys
import textwrap

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_agent_contract.py"


def test_repo_required_files_exist():
    required = ["README.md", "LICENSE", "TOS.md", "docs/setup-checklist.md"]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), f"Missing required file: {rel}"


def test_validator_requires_path_argument():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2


def test_validator_reports_missing_section(tmp_path):
    contract = tmp_path / "contract.md"
    contract.write_text(
        textwrap.dedent(
            """
            Not a valid contract
            """
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(contract)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "missing" in (result.stdout + result.stderr).lower()


def test_validator_imports_cleanly():
    script = REPO_ROOT / "scripts" / "validate_agent_contract.py"
    source = script.read_text(encoding="utf-8")
    compile(source, str(script), "exec")


def test_example_contract_present():
    assert (REPO_ROOT / "example-agent" / "contract.md").exists()
    assert (REPO_ROOT / "example-agent" / "SOUL.md").exists()
