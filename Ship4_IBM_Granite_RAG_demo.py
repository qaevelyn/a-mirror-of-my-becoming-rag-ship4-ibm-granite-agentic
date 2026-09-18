#!/usr/bin/env python3
# ============================================================
# Copyright (c) 2026 Evelyn Caro. All rights reserved.
# A Mirror of My Becoming
# https://evelynacaro.github.io
# For licensing inquiries: evelyn.caro.cloud@gmail.com
# ============================================================

"""Ship 4 — IBM Granite Agentic RAG — Demo Script"""
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

print("Ship 4 — IBM Granite Agentic RAG")
print("-" * 50)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="granite4.1:3b", temperature=0.7)
print("Embeddings ready: nomic-embed-text")
print("LLM ready: granite4.1:3b")

PERSIST_DIR = "./chroma_db"
SOURCE = "/Users/evelyn/Repos/Mirror-Project/MIRROR_LOG.md"

if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
    vector_store = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
    print("Vector store loaded: " + str(vector_store._collection.count()) + " documents")
else:
    print("Building vector store from Mirror archive...")
    documents = TextLoader(SOURCE).load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator="\n")
    texts = splitter.split_documents(documents)
    vector_store = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=PERSIST_DIR)
    print("Vector store created: " + str(len(texts)) + " chunks")

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

@tool
def get_mirror_context(question: str) -> str:
    """Get context about the Mirror of My Becoming archive."""
    results = retriever.invoke(question)
    return "\n\n".join(doc.page_content for doc in results)

tools = [get_mirror_context]

prompt = PromptTemplate.from_template(
    "You are a helpful assistant. Answer the human's question using the tools available.\n\n"
    "You have access to the following tools:\n{tools}\n\n"
    "Use the following format:\n"
    "Question: the input question you must answer\n"
    "Thought: you should always think about what to do\n"
    "Action: the action to take, should be one of [{tool_names}]\n"
    "Action Input: the input to the action\n"
    "Observation: the result of the action\n"
    "... (this Thought/Action/Action Input/Observation can repeat N times)\n"
    "Thought: I now know the final answer\n"
    "Final Answer: the final answer to the original input question\n\n"
    "Begin!\n\n"
    "Question: {input}\n"
    "Thought: {agent_scratchpad}"
)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True)

queries = [
    "What is A Mirror of My Becoming?",
    "How does A Mirror of My Becoming use RAG pipelines?",
]

for query in queries:
    print()
    print("=" * 60)
    print("QUERY: " + query)
    print("=" * 60)
    response = agent_executor.invoke({"input": query})
    print()
    print("FINAL ANSWER:")
    print(response["output"])

print()
print("-" * 50)
print("Demo complete.")
