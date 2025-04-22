# 🧠 LLM Retrieval RAG Prototype

**Ask natural language questions. Get fast, precise, and contextual answers using FAISS and GPT-4o.**

---

## Overview

This is a simple and functional prototype for _LLM RAG Retrieval_ that:

✅ Accepts natural language questions  
✅ Searches for the most relevant answer using FAISS (vector search)  
✅ Uses GPT-4o to generate an answer based on the retrieved context

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/derick1castro/DocuRAG-Pipeline
cd DocuRAG-Pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

> ⚠️ **Make sure you're using Python 3.11.9**

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API Key

Create a `.env` file in the project root with the following content:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the application

```bash
python main.py
```

### 6. Ask questions like:

```
How is the United States supporting Ukraine economically and militarily?
```

---

## How It Works

- Uses OpenAI's `text-embedding-3-small` model to convert texts into vectors
- Indexes vectors using **FAISS** for fast similarity search
- Retrieves the most relevant context snippets
- Uses GPT-4 to generate an answer **only** from that context
- Logs operations using **loguru**

---

## What I'd Do Next With More Time

- Add support for PDF and text file ingestion (using LangChain or PyMuPDF).
- Implement a web interface (e.g., Flask or Streamlit).
- Switch to a local embedding model for offline use.
- Improve retrieval with metadata filtering or hybrid search (keyword + vector).
- Add a caching layer for repeated queries and faster responses.

---

---
