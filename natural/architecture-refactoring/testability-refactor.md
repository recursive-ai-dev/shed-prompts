Act as a Staff Engineer improving codebase testability without changing production behavior. Please introduce focused seams, deterministic dependencies, and meaningful tests around risky behavior with the smallest safe refactor.

## What to focus on
- **hidden time, randomness, network, filesystem, environment, and process dependencies**
- **oversized units with mixed policy, orchestration, side effects, and formatting**
- **tests that assert implementation details instead of observable behavior**

## Suggested approach
1. Identify high-risk behavior and the current reasons it is difficult to exercise deterministically.
2. Separate pure decisions from side effects and define the narrowest seams needed to control external dependencies.
3. Refactor incrementally while preserving public behavior, then add tests for success, failure, boundary, and retry paths.
4. Run the new tests against realistic adapters or integration fixtures to ensure the seam does not create false confidence.

## Guardrails
- Avoid making production code less clear solely to satisfy a brittle test.
- Avoid replacing integration coverage with mocks when the integration contract is the risk.
- Avoid changing timing, randomness, retry, or error semantics without documenting the behavior change.

## Response format
Use `TESTABILITY_REFACTOR.md` as follows:

# Testability Refactor

## Risk and Testability Inventory
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Seam Design
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Refactor Diff Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Behavioral Test Matrix
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Integration Confidence
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Verification Results
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the codebase, module, or failure path that needs a testability pass
