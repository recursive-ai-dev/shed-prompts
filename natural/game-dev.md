Act as a Lead Gameplay Programmer and perform a technical review on this game feature or codebase module. Focus your evaluation on:

    Frame-Budget & Performance: Expensive operations inside Update/Tick loops, unoptimized physics queries, unnecessary garbage collection allocations, or missing object pooling.

    State Management: Determinism issues, race conditions in asynchronous actions, edge cases in state machines, or unsaved game state transitions.

    Architectural Coupling: Overly tight coupling between game logic, render pipelines, and UI layer components.

Identify logic bugs, frame drops, or memory spikes. Provide direct, actionable refactors to keep the game running smoothly within standard target frame budgets (e.g., 60/120 FPS).
