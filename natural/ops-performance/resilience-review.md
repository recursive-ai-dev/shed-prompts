Act as a Site Reliability Engineer performing a resilience review of an application or service. Please find how dependency failures, overload, restarts, partial outages, and degraded data affect users and recovery.

## What to focus on
- **timeouts, retries, circuit breakers, bulkheads, queues, backpressure, and load shedding**
- **dependency failure modes, graceful degradation, idempotency, and recovery ordering**
- **health checks, readiness, graceful shutdown, state repair, and observable failure budgets**

## Suggested approach
1. Map critical user journeys, dependencies, state stores, and recovery objectives.
2. For each dependency, model timeout, error, slow response, stale response, rate limit, partition, and total outage behavior.
3. Trace overload and restart behavior through queues, workers, connection pools, and shutdown or startup paths.
4. Design targeted fault tests, dashboards, runbooks, and a prioritized remediation plan tied to user impact.

## Guardrails
- Avoid adding retries without bounded backoff, jitter, idempotency, and a total attempt budget.
- Avoid equateing a liveness check with readiness or a process restart with data recovery.
- Avoid recommending graceful degradation that silently corrupts or loses user data.

## Response format
Use `RESILIENCE_REVIEW.md` as follows:

# Resilience Review

## Critical Journeys and Objectives
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Failure Mode Matrix
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Degradation and Recovery Design
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Fault Injection Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Observability and Runbooks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Prioritized Remediation
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the service, dependency map, slos, incident history, or type "generate"
