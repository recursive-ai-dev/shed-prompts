Act as a Performance Engineer and conduct a measurement-driven optimization audit. Look specifically for:

    Database query inefficiencies (N+1s, missing indexes, unbounded fetches).

    Synchronous I/O or unbatched network calls on hot paths.

    Wasteful re-renders, unmemoized compute, or excessive memory overhead.

    Payload bloat and unhandled memory leaks.

Focus only on high-impact, hot execution paths. Back every finding with a baseline measurement and a post-fix measurement (or clearly labeled estimates if profiling data isn't directly available). Ensure every caching suggestion includes a valid invalidation strategy without sacrificing correctness. Present your findings ranked strictly by performance impact.
