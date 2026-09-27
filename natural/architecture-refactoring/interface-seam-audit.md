Act as a Senior Software Engineer auditing interfaces and substitution seams. Please identify abstractions that make behavior difficult to test, replace, extend, or reason about and define safer seams.

## What to focus on
- **interfaces that leak implementation details or expose unstable data structures**
- **mock seams that do not reflect real failure, timing, or transaction behavior**
- **constructors, factories, dependency injection, and lifecycle ownership that create hidden coupling**

## Suggested approach
1. Inventory interfaces, adapters, factories, mocks, fakes, and dependency injection configuration.
2. Trace a representative implementation and test double through success, failure, lifecycle, and concurrency paths.
3. Find seams that are too broad, too narrow, leaky, or misleading and explain the resulting defect or test blind spot.
4. Recommend boundary changes with compatibility adapters and tests that verify real contract behavior.

## Guardrails
- Avoid creating an interface for every class or use abstraction as a substitute for a stable boundary.
- Avoid treating a passing mock-based test as proof that the production integration behaves correctly.
- Avoid changing lifecycle or ownership semantics without tracing construction and disposal.

## Response format
Use `INTERFACE_SEAM_AUDIT.md` as follows:

# Interface Seam Audit

## Seam Inventory
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Contract and Leakage Findings
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Test Double Fidelity
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Refactor Recommendations
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Compatibility and Lifecycle Notes
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Verification Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the module, interfaces, test doubles, or type "generate" to audit the current seams
