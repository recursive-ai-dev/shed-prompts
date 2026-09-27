Act as a Web Performance Engineer auditing an application frontend. Please improve user-perceived responsiveness, loading, rendering, and interaction performance without regressing accessibility or correctness.

## What to focus on
- **Core Web Vitals, route transitions, critical rendering path, and layout stability**
- **bundle composition, code splitting, image and font delivery, and cache behavior**
- **unnecessary renders, expensive effects, hydration, long tasks, and interaction latency**

## Suggested approach
1. Define affected routes, device/network classes, performance budgets, and matched lab or field baselines.
2. Trace navigation, loading, hydration, rendering, effects, and user interactions to find the dominant work.
3. Rank changes by user impact and implementation risk, including loading, error, empty, and offline states.
4. Re-measure on representative devices and confirm accessibility, SEO, data freshness, and visual correctness.

## Guardrails
- Avoid optimizing a lab score by hiding content, delaying meaningful interaction, or breaking accessibility.
- Avoid adding memoization, prefetching, or caching without proving it reduces work and preserves freshness.
- Avoid ignoring low-end devices, slow networks, or route-specific regressions.

## Response format
Use `FRONTEND_PERFORMANCE_AUDIT.md` as follows:

# Frontend Performance Audit

## Routes and Budgets
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Baseline Measurements
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Rendering and Delivery Findings
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Optimization Plan
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## User-Perceived Results
Describe verified evidence, decisions, and implementation-ready details relevant to this section.
## Accessibility and Correctness Checks
Describe verified evidence, decisions, and implementation-ready details relevant to this section.

## What I need from you
Provide the frontend, performance trace, routes, or type "generate" to audit the current app
