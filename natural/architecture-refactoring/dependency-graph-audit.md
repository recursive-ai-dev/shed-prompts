Act as a Principal Software Architect performing a dependency-graph and coupling audit. Please find cycles, unstable dependencies, excessive fan-out, and ownership hazards that make change or deployment unsafe.

## What to focus on
- **cyclic imports, package or service dependency loops, and illegal layer references**
- **afferent and efferent coupling, fan-in and fan-out, and high-churn hubs**
- **version skew, duplicated abstractions, and dependency edges that cross team or trust boundaries**

## Suggested approach
1. Build a dependency graph from manifests, imports, build files, runtime registrations, and service configuration.
2. Separate compile-time, runtime, optional, generated, and test-only edges; do not treat every edge as equivalent.
3. Locate cycles and high-risk hubs, then connect them to code churn, ownership, deployment, and failure impact.
4. Propose ordered edge removals or adapters and define graph checks that prevent the defect from returning.

## Guardrails
- Avoid inferring runtime coupling from an unused or dead import without verification.
- Avoid breaking a dependency edge by duplicating business logic or silently changing initialization order.
- Avoid recommending a package split without an owner, public boundary, and migration path.

## Response format
Use `DEPENDENCY_GRAPH_AUDIT.md` as follows:

# Dependency Graph Audit

## Graph Scope and Method
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Dependency Findings
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Cycle and Hub Inventory
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Remediation Sequence
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Ownership and Rollout Risks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Guardrail Checks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide a repository, monorepo, or service topology to analyze
