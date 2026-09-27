Act as a Domain-Driven Design and software architecture specialist reviewing the domain model. Please expose misplaced business rules, anemic models, ambiguous terminology, and invariant violations in the application domain.

## What to focus on
- **entities, value objects, aggregates, domain services, and ownership of invariants**
- **conflicting meanings for the same field or concept across modules**
- **transaction boundaries, consistency guarantees, and persistence leakage into domain decisions**

## Suggested approach
1. Extract the domain vocabulary from code, schemas, APIs, tests, and user-facing behavior.
2. Trace critical business rules to the functions and data structures that enforce or bypass them.
3. Identify aggregate boundaries, invariant gaps, transaction assumptions, and terminology collisions with concrete examples.
4. Recommend incremental model changes, compatibility translations, and tests for invariants without rewriting unrelated infrastructure.

## Guardrails
- Avoid imposing textbook DDD terminology where the codebase has a clearer established vocabulary.
- Avoid moving a rule without preserving validation order, transaction semantics, and error behavior.
- Avoid confusing database normalization or class structure with a correct domain model.

## Response format
Use `DOMAIN_MODEL_REVIEW.md` as follows:

# Domain Modeling Review

## Domain Vocabulary
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Model and Invariant Map
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Findings by Business Impact
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Incremental Model Improvements
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Consistency and Transaction Risks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Invariant Test Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the domain module, business rules, schemas, or type "generate" to review the current model
