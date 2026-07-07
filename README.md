# Hermes Agent Template

Reusable, versioned AI agent scaffold for Hermes-style systems.

Designed around explicit agent contracts, bounded responsibilities, least-privilege tool access, layered memory, observable health, and tested failure handling — not roleplay prompts.

**Based on:** Hermes Agent SDK patterns and production agent engineering standards

---

## What You Get

| Asset | Purpose |
|-------|---------|
| `agent/agent.spec.md` | Mandatory agent contract template |
| `agent/AGENT.md` | Runnable agent profile template |
| `docs/checklist.md` | Pre-publishing agent checklist |
| `docs/migration.md` | Adapter notes for common LLM backends |
| `scripts/validate_agent_contract.py` | Contract linter |
| `scripts/skeleton.sh` | New-agent scaffolding script |

---

## Quick Start

```bash
cp agent/AGENT.md agents/your-agent/SOUL.md
cp agent/agent.spec.md agents/your-agent/contract.md
# Edit fields, run validation
python scripts/validate_agent_contract.py agents/your-agent/contract.md
```

---

## Core Principles

- One primary responsibility per agent
- Explicit inputs, outputs, tool permissions, and failure modes
- Memory by purpose: working, session, project, organizational
- Observability: version, health, latency, tool usage
- Lifecycle states: draft → experimental → development → testing → production → deprecated → retired

---

## Who This Is For

- Teams building multi-agent systems and needing stable contracts
- Engineers migrating prompt wrappers into production-grade agents
- Founders who need repeatable agent design, not prompt roulette
- Anyone who wants agents that fail predictably and are safe to operate

---

## Services

| Tier | Price | Deliverables |
|------|-------|--------------|
| Agent Health Audit | $197 | Contract review, failure taxonomy gap analysis, tool permission audit, observability review, improvement plan |
| Constrained-Infra Review | $297 | Resource usage review, memory budget reassessment, failure-mode review, recovery policy recommendations, Docker/runtime optimization notes |
| Retainer | Custom | Weekly architecture/implementation support, priority async review, playbook updates |

Terms: 50% upfront, 50% on delivery. Scope freeze required before start. Rush add-ons priced separately.

---

## License

MIT — use, modify, and ship freely.  
**Author:** Conrad CJ Wilson  
**GitHub:** https://github.com/cjps4linux-creator  
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
