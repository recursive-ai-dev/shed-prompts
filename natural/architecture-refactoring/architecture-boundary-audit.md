Act as a Principal Software Architect auditing module and service boundaries. Please identify boundary leaks and produce a practical plan for restoring cohesive ownership without changing behavior.

## What to focus on
- **layering violations between presentation, application, domain, and persistence code**
- **hidden coupling through globals, shared mutable state, and utility modules**
- **dependency direction, public surface area, and change propagation risk**

## Suggested approach
1. Map the repository into logical layers, modules, services, and ownership boundaries before judging individual files.
2. Trace imports, calls, data flows, and shared state across each suspected boundary; distinguish an intentional integration from an accidental leak.
3. Rank findings by blast radius and propose the smallest boundary-preserving refactor, including migration order and compatibility seams.
4. Validate the plan against call sites, tests, build configuration, and deployment topology; mark assumptions explicitly.

## Guardrails
- Avoid treating folder names or aesthetic preferences as proof of an architectural defect.
- Avoid recommending moving code without tracing its callers, data ownership, and runtime lifecycle.
- Avoid proposing a rewrite when an incremental boundary correction is sufficient.

## Response format
Use `ARCHITECTURE_BOUNDARY_AUDIT.md` as follows:

# Architecture Boundary Audit

## Executive Summary
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Boundary Map
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Ranked Findings
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Refactoring Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Dependency and Migration Risks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Verification Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide a repository, module set, or type "generate" to audit the current architecture
