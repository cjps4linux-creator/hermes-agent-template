# Migration Notes

## From Prompt Wrappers
- Move roleplay into bounded Mission/Scope sections
- Split generic behaviors into Responsibility items
- Add explicit failure modes instead of implicit fallback text

## From OpenAI Assistants
- Map `tools` arrays to tool permissions table
- Map `instructions` to Mission + Scope + Constraints
- Add contract versioning and evaluation thresholds

## From LangGraph / CrewAI
- Map nodes to agent responsibilities
- Map edges to coordination rules
- Keep agent count low: one responsibility per agent
