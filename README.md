# Ship 4 — IBM Granite Agentic RAG Pipeline — Local

**The moment the fleet stopped being a lookup table.**

Ship 4 of A Mirror of My Becoming™. Built August–September 2026 on an 8 GB Intel MacBook Air. Runs fully local: IBM Granite 4.1 (3B) and nomic-embed-text via Ollama, plus a ReAct agent with tool-calling. No cloud account, no API key, no data leaving the machine.

**Author:** Evelyn Caro

---

## What it does

Everything Ship 3 does — local corpus, local chunking, local embeddings, local Chroma store — plus a tool-calling layer. The system is given a `get_mirror_context` tool bound to its vector store, and a ReAct agent (LangChain's `create_react_agent`) that decides what to do with a question: retrieve context, act, or answer directly. The agent reasons about which tool to use and when.

The retrieval window is 4 chunks per query (`search_kwargs={"k": 4}`), tuned for the curated corpus size.

---

## Why it exists

Ship 2 introduced agency; Ship 4 continued it cross-platform and made it the fleet's default posture. The distinction this ship demonstrates: a RAG system that only retrieves is a search engine with extra steps. An agentic system **decides** — and the decision layer is where the interesting engineering lives: prompt design, tool binding, and the difference between a model that answers and a model that plans.

---

## Requirements

- Python 3 with: `langchain`, `langchain-community`, `langchain-text-splitters`, `langchain-ollama`, `langchain-chroma`, `langchain-core` (tools), `langchain-classic` (agents)
- [Ollama](https://ollama.com) running locally, with `granite4.1:3b` and `nomic-embed-text` pulled
- `data/CURATED_PUBLIC_DATA.md` — your own corpus

---

## Quickstart

1. Install the packages named at the top of Ship4_IBM_Granite_RAG_demo.py
2. Pull the models: ollama pull granite4.1:3b && ollama pull nomic-embed-text
3. Put your corpus in data/CURATED_PUBLIC_DATA.md
4. Run: python3 Ship4_IBM_Granite_RAG_demo.py
The agent gets the get_mirror_context tool and decides when to use it.
text


---


---

## The fleet

- **[Ship 1](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship1-deepseek-rag-local)** — DeepSeek RAG, rebuilt local after AWS lost the original
- **[Ship 2](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship2-ibm-granite-agentic)** — IBM Granite Agentic RAG
- **[Ship 3](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship3-ibm-granite)** — IBM Granite Standard RAG
- **[Ship 4](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship4-ibm-granite-agentic)** — IBM Granite Agentic RAG
- **[Ship 5](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship5-ibm-granite-agentic-evidenceflow)** — IBM Granite Agentic RAG with EvidenceFlow
- **[Ship 6 — Suite: Ingestion Tools](https://github.com/qaevelyn/a-mirror-of-my-becoming-suite-ingestion-tools)** — the suite
- **[Ship 7 — msgvault adapter](https://github.com/qaevelyn/a-mirror-of-my-becoming-suite-msgvault-adapter)** — the mail bridge
**[Suite: Ingestion Tools](https://github.com/qaevelyn/a-mirror-of-my-becoming-suite-ingestion-tools)** — the tooling that gets documents into the vector stores these ships read from.

**[A Mirror of My Becoming™](https://github.com/qaevelyn/a-mirror-of-my-becoming)** — the parent index for the entire practice.

**[Fleet index + SETUP.md](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-pipelines)** — how to point any ship at your own corpus.

---


## License

Dual-licensed:

- **AGPL-3.0** — free to use, modify, and redistribute under the terms of the license. Full text in [LICENSE](LICENSE).
- **Commercial license** — available for organizations that need to use the code without the AGPL-3.0 obligations. Contact the author for pricing.

Free does not mean free to exploit. If you build a product on this work, the author expects to be paid.

---

## Author

**Evelyn Caro** — Sovereign AI Builder.

**[qaevelyn.github.io](https://qaevelyn.github.io)** · Commercial licensing: **evelyn.caro.cloud@gmail.com**

---

© 2026 Evelyn Caro. All rights reserved.
