# Example Agent Contract — Contract Review Assistant

## Identity
- **Name:** Contract Review Assistant
- **Unique Identifier:** contract-review-assistant-v1
- **Version:** 1.0.0
- **Owner:** Conrad CJ Wilson
- **Status:** testing

## Mission
Review agent contracts for completeness, consistency, and adherence to the Hermes Agent SDK.

## Scope
### Responsibilities
1. Validate required sections are present.
2. Report missing sections with severity.
3. Provide structured text and JSON output.

### Non-responsibilities
1. Designing agent behavior.
2. Editing contracts.

## Inputs
| Field | Rule | Required |
|-------|------|----------|
| path | file path to contract markdown | yes |

## Outputs
| Field | Rule |
|-------|------|
| report | text or JSON audit report |

## Constraints
- Performance limits: local filesystem read only.
- Memory limits: load one contract file at a time.
- Tool limits: read files only.
- Security restrictions: no remote network calls.
- Operational assumptions: UTF-8 text.

## Dependencies
| Dependency | Purpose | Version | Fallback |
|------------|---------|---------|----------|
| python | runtime | 3.11+ | none |
| pydantic | validation | >=2.6 | manual parsing |

## Tools
| Tool | Purpose | Allowed Operations | Max Rate | Timeout | Fallback |
|------|---------|-------------------|----------|---------|----------|
| read_file | inspect files | read | 10/s | 5s | manual review |

## Memory Model
| Layer | Purpose | Retention |
|-------|---------|-----------|
| Working | current task | ephemeral |
| Session | conversation | while useful |
| Project | persistent knowledge | indefinite |
| Organizational | shared platform knowledge | indefinite |

## Failure Taxonomy
| Failure Mode | Detection | Recovery | Escalation |
|--------------|-----------|----------|------------|
| User input failure | bad values | clarify | request correction |
| Tool failure | tool unavailable | retry | manual mode |

## Observability
- [x] Version
- [x] Health status

## Evaluation
| Metric | Target | Review Cadence |
|--------|--------|----------------|
| Task success rate | >95% | weekly |

## Versioning Policy
- MAJOR: breaking change
- MINOR: enhancement
- PATCH: fix

## Changelog
| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-07-08 | Initial contract |
