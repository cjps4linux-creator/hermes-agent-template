# Hermes Agent Template — Launch Documentation

## Launch Readiness Snapshot
- Repo: `hermes-agent-template`
- Default branch: `master`
- License: MIT
- Products: Hermes Agent Template / Audit / Bundle
- Support contact: `conradcjwilson0@gmail.com`

## Evidence
- `scripts/validate_agent_contract.py` present for contract validation
- `agent/agent.spec.md` enforces contract-first agent design
- README documents lifecycle, memory model, permissions, and failure taxonomy
- Pricing tiers present in README

## Assumptions
- Consumer runs contract validator before publishing agents
- Shell scaffolding requires Git Bash/WSL on Windows

## Post-Launch Actions
- Enable GitHub secret scanning and vulnerability alerts
- Add branch protection after first public release tag
- Maintain SECURITY.md and issue templates for bug reports
