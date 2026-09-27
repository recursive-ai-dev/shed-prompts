Act as a Principal Architect planning a safe monolith decomposition. Please partition a monolithic application along real business and operational boundaries without creating a distributed monolith.

## What to focus on
- **candidate bounded contexts, data ownership, transaction boundaries, and change coupling**
- **synchronous calls, shared databases, queues, and cross-context consistency costs**
- **deployment independence, failure isolation, observability, and team ownership**

## Suggested approach
1. Map business capabilities, runtime flows, data stores, integrations, and change history to find actual seams.
2. Score candidate partitions by cohesion, coupling, data ownership, latency, failure impact, and migration cost.
3. Design an incremental extraction slice with anti-corruption layers, data synchronization, and a reversible rollout.
4. Define service boundaries only where independent operation creates more value than distributed-systems cost.

## Guardrails
- Avoid splitting by technical layer or arbitrary table count alone.
- Avoid creating a service that requires synchronous access to another service for every useful operation.
- Avoid ignoring data migration, consistency, observability, on-call, and local-development costs.

## Response format
Use `MONOLITH_DECOMPOSITION_PLAN.md` as follows:

# Monolith Decomposition Plan

## Capability and Data Map
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Partition Candidates
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Cost and Risk Scorecard
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Extraction Sequence
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Consistency and Failure Model
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Decommission Criteria
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the monolith, business capabilities, data topology, and decomposition constraints
