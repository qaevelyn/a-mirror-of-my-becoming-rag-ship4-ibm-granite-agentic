# Ship 4: IBM Granite Agentic RAG Pipeline

**Built:** August 2026
**Author:** Evelyn Caro
**Status:** ✅ Built and working

**Naming note:** The code file is `Ship4_IBM_Granite_RAG_v2_Agentic.ipynb`. It began as a 
copy of the Ship 2 IBM Granite notebook and was adapted for agentic execution. The internal 
header and filename have been corrected to reflect Ship 4. The folder has always been correct.

---

## Origin

The fourth ship combined agency with cross-platform.

Ship 2 proved agency worked. Ship 3 proved the pattern crossed vendors. Ship 4 asked: 
does the pattern hold when both variables change at once? IBM Granite + agentic reasoning. 
The answer was yes.

---

## What It Does

An agentic RAG pipeline built on IBM Granite. Retrieval + action. The agent decides when 
to query the vector database, when to call APIs, and when to answer from what it already 
knows — running on a second LLM vendor from Ship 2.

---

## Architecture

- **Runtime:** Local, sovereign execution
- **Model:** IBM Granite
- **Pipeline:** Agentic RAG
- **Data source:** Local files — the Mirror personal archive
- **Storage:** Vector database
- **Cloud dependency:** None (current)

---

## Pipeline

1. Read local documents from the Mirror archive
2. Chunk into pieces
3. Vectorize (embed) each chunk
4. Store vectors in a vector database
5. Query at runtime → the agent decides whether to retrieve, call an API, or answer directly

---

## Integration

- Reads local data — the Mirror personal archive
- Chunks, vectorizes, stores in vector DB
- Agent decides when to query, when to act, when to answer
- **No cloud dependency.** Local-first. Sovereign.
- Demonstrates agency and cross-platform execution working together.

---

## Access and Copyright

This work was created by Evelyn Caro. DeepSeek is the only collaborator — used as a tool 
in the creative and technical process.

This is a personal portfolio project and is not open for collaboration or external access. 
The video and documentation speak for themselves.

Copyright © 2026 Evelyn Caro. All rights reserved. Copyright registration is pending.
