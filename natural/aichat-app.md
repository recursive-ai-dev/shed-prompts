Act as an AI Systems Engineer and audit this LLM/chat application codebase. Focus strictly on:

    Latency & Streaming: Synchronous blocking calls on streaming endpoints, inefficient token generation handling, or missing backpressure control.

    Context & Retrieval (RAG): Context window overflows, redundant embedding calls, improper chunking, or poorly managed conversation history state.

    Reliability & Guardrails: Unhandled API rate limits/timeouts, missing fallbacks for model errors, unsanitized user prompts (prompt injection risk), and lack of output parsing safety.

Provide concrete fixes to reduce time-to-first-token (TTFT), prevent context crashes, and make the chat system production-resilient.
