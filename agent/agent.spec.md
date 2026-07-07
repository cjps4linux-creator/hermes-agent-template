# Agent Contract — Hermes Agent Template

## Mandatory Fields

### Identity
- **Name:** 
- **Unique Identifier:** 
- **Version:** 
- **Owner:** 
- **Status:** draft | experimental | development | testing | production | deprecated | retired

---

### Mission
One concise sentence. No vague capabilities.

Example:
> Transform engineering requirements into modular system architectures.

---

### Scope
**Responsibilities:**
1. 
2. 

**Non-responsibilities:**
1. 
2. 

---

### Inputs
| Field | Rule | Required |
|-------|------|----------|
|  |  | yes / no |
|  |  | yes / no |

Assumptions:
- 

---

### Outputs
| Field | Rule |
|-------|------|
|  |  |
|  |  |

Success conditions:
- 
- 

Failure conditions:
- 
- 

---

### Constraints
- Performance limits:
- Memory limits:
- Tool limits:
- Security restrictions:
- Operational assumptions:

---

### Dependencies
| Dependency | Purpose | Version | Fallback |
|------------|---------|---------|----------|
|  |  |  |  |

---

### Tools
| Tool | Purpose | Allowed Operations | Max Rate | Timeout | Fallback |
|------|---------|-------------------|----------|---------|----------|
|  |  |  |  |  |  |

---

### Memory Model
| Layer | Purpose | Retention |
|-------|---------|-----------|
| Working Memory | Current task context | Ephemeral |
| Session Memory | Conversation/project context | While useful |
| Project Memory | Persistent project knowledge | Indefinite |
| Organizational Memory | Shared platform knowledge | Indefinite |

Promotion criteria:
- 

---

### Failure Taxonomy
| Failure Mode | Detection | Recovery | Escalation |
|--------------|-----------|----------|------------|
| User input failure |  |  |  |
| Tool failure |  |  |  |
| Dependency failure |  |  |  |
| Reasoning failure |  |  |  |
| Resource failure |  |  |  |
| Security failure |  |  |  |

---

### Observability
Required exposures:
- [ ] Version
- [ ] Health status
- [ ] Last successful execution timestamp
- [ ] Error count / error rate
- [ ] Average latency
- [ ] Tool usage
- [ ] Resource consumption
- [ ] Current lifecycle state

---

### Evaluation
| Metric | Target | Review Cadence |
|--------|--------|----------------|
| Task success rate |  | Weekly |
| Hallucination rate |  | Weekly |
| Instruction adherence |  | Weekly |
| Confidence calibration |  | Monthly |
| Tool error rate |  | Weekly |

---

## Versioning Policy
- MAJOR: breaking interface or responsibility change
- MINOR: backward-compatible enhancement
- PATCH: fix or wording correction

## Changelog
| Version | Date | Change |
|---------|------|--------|
| 0.1.0 |  | Initial contract |
