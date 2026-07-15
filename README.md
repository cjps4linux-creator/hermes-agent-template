# Hermes Agent Template

Production-grade scaffold for designing, validating, and evolving AI agents with explicit contracts, bounded responsibilities, and observable behavior.

## What You Get

| Asset | Purpose |
|-------|---------|
| `agent/agent.spec.md` | Mandatory agent contract template |
| `agent/AGENT.md` | Runnable agent profile template |
| `docs/checklist.md` | Pre-publishing agent checklist |
| `docs/migration.md` | Migration notes for common LLM backends |
| `scripts/validate_agent_contract.py` | Contract linter |
| `scripts/skeleton.sh` | New-agent scaffolding script |

## Quick Start

```bash
cp agent/AGENT.md agents/your-agent/SOUL.md
cp agent/agent.spec.md agents/your-agent/contract.md
python scripts/validate_agent_contract.py agents/your-agent/contract.md
```

## Core Principles

- One primary responsibility per agent
- Explicit inputs, outputs, tool permissions, and failure modes
- Layered memory: working, session, project, organizational
- Observable health: version, health, latency, tool usage
- Lifecycle states: draft → experimental → development → testing → production → deprecated → retired

## Who This Is For

- Teams building multi-agent systems who need stable contracts
- Engineers migrating prompt wrappers into production-grade agents
- Founders who need repeatable agent design, not prompt roulette
- Operators who want agents that fail predictably and are safe to operate

## Why It Fits Hermes

Hermes runs on constrained hardware with zero cloud spend. This template keeps agents auditable, testable, and resource-aware — matching the rest of the platform.

## Repo Contents

| File/Folder | Purpose |
|-------------|---------|
| `agent/AGENT.md` | Agent identity + execution profile |
| `agent/agent.spec.md` | Formal contract schema |
| `docs/checklist.md` | Publish + production readiness checklist |
| `docs/migration.md` | Migration notes from common frameworks |
| `scripts/validate_agent_contract.py` | Contract validator |
| `scripts/skeleton.sh` | Agent scaffold |

## Troubleshooting

- If validation fails, run with `--help` for rule list
- If shell script fails on Windows, use Git Bash or WSL
- If fields are missing, consult `docs/checklist.md`

## Services

| Tier | Price | Deliverables |
|------|-------|--------------|
| Agent Health Audit | $197 | Contract review, failure taxonomy gap analysis, tool permission audit, observability review, improvement plan |
| Constrained-Infra Review | $297 | Resource usage review, memory budget reassessment, failure-mode review, recovery policy recommendations, Docker/runtime optimization notes |
| Retainer | Custom | Weekly architecture/implementation support, priority async review, playbook updates |

## Purchase

| Product | Price | Buy |
|---------|-------|-----|
| Hermes Agent Template | $49 | [Buy Now](https://www.paypal.com/ncp/payment/ZYQT5ZQTWD78N) |
| Hermes Bundle | $69 | [Buy Now](https://www.paypal.com/ncp/payment/SXA9G9LUDBW2A) |
| Constrained AI Stack | $39 | [Buy Now](https://www.paypal.com/ncp/payment/FCZREAP49FXTN) |

After payment, forward your PayPal confirmation to support to receive your files.

## License

MIT — use, modify, and ship freely.

**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
