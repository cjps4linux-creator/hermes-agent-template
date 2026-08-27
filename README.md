# Hermes Agent Template

Production-grade scaffold for designing, validating, and evolving AI agents with explicit contracts, bounded responsibilities, and observable behavior.

Built by Conrad CJ Wilson.

## What It Demonstrates

| Capability | Implementation |
|---|---|
| Agent contract schema | Formal specification covering identity, mission, scope, inputs, outputs, constraints, dependencies, and tool permissions |
| Layered memory model | Working, session, project, and organizational memory tiers with explicit promotion rules |
| Tool permissions | Principle of least privilege with per-tool authorization documentation |
| Failure taxonomy | Classified failure modes: user input, tool, dependency, reasoning, resource, and security failures |
| Lifecycle management | Defined states: draft, experimental, development, testing, production, deprecated, retired |
| Observability | Version, health status, latency, tool usage, and error reporting requirements |
| Contract validation | Python script to validate agent contracts against the schema |
| Agent scaffolding | Shell script to generate new agent directories from the template |

## Repository Layout

| Path | Purpose |
|---|---|
| `agent/AGENT.md` | Agent identity and execution profile template |
| `agent/agent.spec.md` | Formal contract schema |
| `docs/checklist.md` | Pre-publishing agent readiness checklist |
| `docs/migration.md` | Migration notes for common LLM backends |
| `scripts/validate_agent_contract.py` | Contract validator |
| `scripts/skeleton.sh` | New-agent scaffolding script |

## Quick Start

```bash
# Copy templates
cp agent/AGENT.md agents/your-agent/SOUL.md
cp agent/agent.spec.md agents/your-agent/contract.md

# Validate the contract
python scripts/validate_agent_contract.py agents/your-agent/contract.md
```

## Core Principles

- One primary responsibility per agent
- Explicit inputs, outputs, tool permissions, and failure modes
- Layered memory: working, session, project, organizational
- Observable health: version, health, latency, tool usage
- Lifecycle states: draft -> experimental -> development -> testing -> production -> deprecated -> retired

## Who This Is For

- Teams building multi-agent systems who need stable contracts
- Engineers migrating prompt wrappers into production-grade agents
- Founders who need repeatable agent design, not prompt roulette
- Operators who want agents that fail predictably and are safe to operate

## Troubleshooting

- If validation fails, run with `--help` for rule list
- If shell script fails on Windows, use Git Bash or WSL
- If fields are missing, consult `docs/checklist.md`

## License

MIT — use, modify, and ship freely.

**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
