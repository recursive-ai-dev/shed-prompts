Act as a Staff Platform Engineer planning an API contract migration. Please make a requested API, schema, or event contract change safely across producers, consumers, clients, and documentation.

## What to focus on
- **compatibility between old and new request, response, and error shapes**
- **versioning, rollout sequencing, deprecation windows, and rollback behavior**
- **generated clients, fixtures, SDKs, tests, observability, and external consumers**

## Suggested approach
1. Inventory the current contract, all producers and consumers, generated artifacts, and compatibility assumptions.
2. Classify the change as additive, tolerant, breaking, or ambiguous and identify clients that cannot be upgraded atomically.
3. Design an expand, dual-support, migrate, and contract sequence with concrete examples and a rollback path.
4. Define contract tests, telemetry, deprecation criteria, and the condition that makes old behavior safe to remove.

## Guardrails
- Avoid calling a breaking change backward-compatible merely because the server can parse old input.
- Avoid removing old fields, status codes, or events before consumer usage is measured or explicitly bounded.
- Avoid inventing external consumers; label unknown clients and provide a discovery step.

## Response format
Use `API_CONTRACT_MIGRATION.md` as follows:

# API Contract Migration

## Change Summary
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Current Contract Inventory
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Compatibility Matrix
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Migration Sequence
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Validation and Rollback
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Removal Gate
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the api, event, or schema change and access to its producers and consumers
