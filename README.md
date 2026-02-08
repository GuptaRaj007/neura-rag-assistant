# 🧠 Neura RAG Assistant

### Prompt Engineering & Retrieval-Augmented Generation (RAG) Mini Project

> A grounded, hallucination-safe policy assistant built with **local LLMs**, **semantic search**, and **iterative prompt design**.

---

## 🌟 Overview

**Neura RAG Assistant** is a **Retrieval-Augmented Generation (RAG)** system that answers user questions **strictly from company policy documents** (Refund, Cancellation, Shipping, etc.).

It is designed to:

* 🔍 Retrieve only relevant policy text
* 📌 Ground answers in retrieved context
* 🚫 Avoid hallucinations
* 🧩 Use **iteratively improved prompts**
* 📊 Include a lightweight **evaluation framework**

Built as part of the **AI Engineer Intern – Take Home Assignment**.

---

## 🏗 Architecture

```
User Question
      │
      ▼
Retriever (FAISS + Sentence Transformers)
      │
      ▼
Top-K Relevant Policy Chunks
      │
      ▼
Prompt Template (PROMPT_V3)
      │
      ▼
LLM (Local via Ollama)
      │
      ▼
Final Answer
(Grounded • Structured • No Hallucination)
```

---

## 🛠 Tech Stack

* **Python**
* **Sentence Transformers** (`all-MiniLM-L6-v2`)
* **FAISS** (vector store)
* **LangChain** (document loading & splitting)
* **Ollama** (local LLM runtime – `llama3`)
* **PyPDF**
* **HuggingFace embeddings**

---

## 🚀 Setup Instructions

```bash
git clone https://github.com/GuptaRaj007/neura-rag-assistant.git
cd neura-rag-assistant
python -m venv neura_env
neura_env\Scripts\activate   # Windows
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run llama3
```

Run the assistant:

```bash
python src/qa.py
```

Run evaluation:

```bash
python src/evaluate.py
```

---

## 1️⃣ Data Preparation

### Document Loading

Policy documents are loaded using **LangChain loaders** from the `data/` folder.

### Chunking Strategy

* **Chunk size:** 500 characters
* **Overlap:** 100 characters

**Why?**

* Smaller chunks → better semantic matching
* Overlap preserves sentence continuity
* Prevents splitting policy rules mid-sentence

---

## 2️⃣ RAG Pipeline

| Step              | Implementation                           |
| ----------------- | ---------------------------------------- |
| Embeddings        | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store      | FAISS                                    |
| Retrieval         | Semantic similarity (Top-K)              |
| Context Injection | Prompt templates                         |
| LLM               | Ollama (`llama3`)                        |

---

## 3️⃣ Prompt Engineering (Core Focus)

We iterated through **three prompt versions**:

### 🟢 PROMPT_V1 – Basic

```text
Use the following context to answer the question.

Context:
{context}

Question:
{question}
```

---

### 🟡 PROMPT_V2 – Improved

```text
You are a policy assistant. Answer ONLY using the provided context.
If the answer is not present, say: "Not available in the provided documents."

Context:
{context}

Question:
{question}

Answer:
```

---

### 🔴 PROMPT_V3 – Final (Production)

```text
You are a strict policy assistant.

Rules:
1. Answer ONLY from the context below.
2. If not found, say: "The information is not available in the provided documents."
3. Quote the policy when possible.
4. Use a clear, structured format.

Context:
{context}

Question:
{question}

Output:
Quote:
- ...

Answer:
...
```

### Why PROMPT_V3 is Better

* 🚫 Eliminates hallucination
* 📌 Forces grounding
* 🧱 Structured output
* 🤝 Handles missing info safely

---

## 4️⃣ Evaluation

We created **6 test questions**:

| Question                                   | Expected      | Result |
| ------------------------------------------ | ------------- | ------ |
| Can I get a refund after 10 days?          | Not allowed   | ✅      |
| Can I cancel after shipping?               | Not allowed   | ✅      |
| How long does international shipping take? | 10–15 days    | ✅      |
| Do you offer free express delivery?        | Not mentioned | ⚠️     |
| Can I cancel my subscription mid-cycle?    | No refund     | ⚠️     |
| What is your office address?               | Not mentioned | ✅      |

### Example Output

```
Q: What is your office address?
Expected: Not mentioned
Model Answer:
The information is not available in the provided documents.
```

---

## 5️⃣ Edge Case Handling

| Scenario              | Behavior                |
| --------------------- | ----------------------- |
| No matching policy    | Graceful refusal        |
| Out-of-scope question | No hallucination        |
| Partial information   | Safe, grounded response |

---

## ⚖ Key Trade-offs

* No reranker → faster, but slightly less precise
* Local LLM → private, but lower fluency
* Small dataset → perfect for demo, not scale

---

## 🔮 Future Improvements

* Reranking layer
* JSON schema validation
* Streaming UI
* LangGraph agents
* Logging & tracing

---

## 💬 Reflection

**What I’m Most Proud Of:**
Building a fully grounded RAG system with **prompt iteration and evaluation**, not just a chatbot.

**What I’d Improve Next:**
Add reranking and automatic response scoring.

---

## 📁 Folder Structure

```
├── data/                 # policy documents
├── src/
│   ├── load_docs.py
│   ├── embed_store.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── qa.py
│   └── evaluate.py
```
