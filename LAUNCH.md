# Hermes Agent Template — Launch Documentation

## Launch Readiness Snapshot

| Field | Value |
| --- | --- |
| Repo | `hermes-agent-template` |
| Default branch | `master` |
| License | MIT |
| Commercial baseline | CI, `CONTRIBUTING.md`, `SECURITY.md`, `LAUNCH.md`, `VERIFICATION.md` |
| Products | Hermes Agent Template / Audit / Bundle |

## Verified
- `scripts/validate_agent_contract.py` present for contract validation
- `agent/agent.spec.md` enforces contract-first agent design
- README documents lifecycle, memory model, permissions, and failure taxonomy

## Launch Gates
- [ ] CI workflow green on `master` before release tag
- [ ] Branch protection enabled on `master`
- [ ] GitHub secret scanning and vulnerability alerts enabled
- [ ] Package artifacts bundled and linked in README before customer delivery

## Release Workflow
1. Update `README.md` and `LAUNCH.md` for the release version.
2. Tag a release with semver: `git tag vX.Y.Z && git push --tags`.
3. Attach deliverables to the GitHub release or support handoff.
4. Rotate audit or support access credentials if shared externally.

## Support
- Support contact: `conradcjwilson0@gmail.com`
