# Hermes Agent Template — Setup Checklist

## Before you start
- [ ] Python 3.11+ installed
- [ ] Git installed and configured
- [ ] You have write access to the repo checkout path
- [ ] On Windows: use Git Bash or WSL2 for shell scripts

## Clone / unpack
- [ ] Repo contents are present locally
- [ ] `scripts/skeleton.sh` is executable if you plan to scaffold agents
- [ ] `agent/agent.spec.md` and `agent/AGENT.md` are present

## Install dependencies / verification
- [ ] `python scripts/validate_agent_contract.py --help` runs successfully
- [ ] Contract validator can read `agent/agent.spec.md` without import/runtime errors

## Validate your first contract
- [ ] Copy `agent/AGENT.md` into an agent folder
- [ ] Copy `agent/agent.spec.md` into the same folder as `contract.md`
- [ ] Update `contract.md` fields for your agent
- [ ] Run `python scripts/validate_agent_contract.py path/to/contract.md`
- [ ] Validation passes, or failures are documented and resolvable

## README/examples sanity check
- [ ] README quick-start commands run in order
- [ ] If a shell command fails, retry from the documented shell environment

## Support
- [ ] Community issues can be reproduced with the above steps
- [ ] For paid support, confirm product version, OS, Python version, and validator output
