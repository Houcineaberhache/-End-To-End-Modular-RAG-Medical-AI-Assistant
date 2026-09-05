# 🩺 MediBot — AI Medical Assistant (RAG-based Chatbot)

A Retrieval-Augmented Generation (RAG) chatbot that answers medical questions grounded in documents you upload — PDFs, textbooks, clinical notes, or reports. Instead of relying on the LLM's raw memory (and risking hallucinated medical facts), the system retrieves the most relevant chunks from your own documents first, then generates an answer strictly from that context.


---

## 🧠 What is RAG?

**Retrieval-Augmented Generation** combines a search step with a generation step:

1. Your question is embedded into a vector
2. That vector is used to search a vector database for the most semantically similar document chunks
3. Those chunks are injected into the LLM's prompt as context
4. The LLM answers *using that context*, instead of guessing from its training data

This matters a lot in medicine — a model confidently making up a drug interaction or symptom is a real risk. Grounding answers in retrieved source material reduces hallucination and keeps responses traceable back to an actual document.

---

## 🔄 Architecture

```
PDF Upload
    ↓
PDF Loader → Chunking → Embedding (Google Generative AI)
    ↓
Pinecone Vector DB (stores embedded chunks)

User Question
    ↓
Query Embedding
    ↓
Similarity Search → Pinecone → Retrieved Chunks
    ↓
RAG Chain (LangChain LCEL + Groq LLaMA3-70B)
    ↓
Grounded Answer + Source Documents
```

---

## ⚙️ Tech Stack

| Component        | Technology                          |
|-------------------|--------------------------------------|
| LLM               | Groq API — LLaMA3-70B                |
| Embeddings        | Google Generative AI (`embedding-001`) |
| Vector Database   | Pinecone                             |
| Orchestration     | LangChain (LCEL)                     |
| Backend           | FastAPI                              |
| Deployment        | Render                               |

---

## 📚 Features

- 📤 Upload one or more medical PDFs (notes, textbooks, reports)
- ✂️ Automatic text extraction and semantic chunking
- 🧬 Embedding generation via Google Generative AI
- 🗂️ Vector storage and similarity search via Pinecone
- 🤖 Context-grounded answers via Groq's LLaMA3-70B
- 🔗 Source document tracking — every answer links back to its retrieved chunks
- 🌐 FastAPI backend with clean, documented REST endpoints

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/MedicalAIAssistant.git
cd MedicalAIAssistant
```

### 2. Set up the environment

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management.

```bash
uv init .
uv pip install -r server/requirements.txt
```

### 3. Configure environment variables

Create a `.env` file inside `server/`:

```dotenv
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
```

| Variable | Where to get it |
|---|---|
| `GOOGLE_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) |
| `GROQ_API_KEY` | [Groq Console](https://console.groq.com/keys) |
| `PINECONE_API_KEY` | [Pinecone Dashboard](https://app.pinecone.io) |

> ⚠️ Never commit `.env` — it's already excluded via `.gitignore`.

### 4. Run the server

```bash
cd server
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`. Interactive docs available at `http://127.0.0.1:8000/docs`.

---

## 📡 API Endpoints

### `POST /upload_pdfs/`
Upload one or more PDF documents to be chunked, embedded, and stored in Pinecone.

**Form field:** `files` (multipart, supports multiple files)

### `POST /ask/`
Ask a question grounded in the uploaded documents.

**Form field:** `question` (string)

**Response:**
```json
{
  "response": "Answer generated from retrieved context...",
  "sources": ["source_chunk_1", "source_chunk_2"]
}
```

---

## 📁 Project Structure

```
├── assets/                    # Architecture diagrams and sample PDFs
├── client/                    # Frontend (Streamlit-style client)
│   ├── components/
│   │   ├── chatUI.py
│   │   ├── history_download.py
│   │   └── upload.py
│   ├── utils/
│   │   └── api.py
│   ├── app.py
│   └── config.py
└── server/                    # FastAPI backend
    ├── middlewares/
    │   └── exception_handlers.py
    ├── modules/
    │   ├── llm.py              # RAG chain construction (LCEL)
    │   ├── load_vectorstore.py # Pinecone + embedding setup
    │   ├── pdf_handlers.py     # PDF loading and chunking
    │   └── query_handlers.py   # Chain invocation logic
    ├── routes/
    │   ├── ask_question.py
    │   └── upload_pdfs.py
    ├── logger.py
    ├── main.py
    └── requirements.txt
```

---

## 🛠️ Notes on Implementation

- Built on **LangChain 1.x**, using **LCEL (LangChain Expression Language)** pipelines rather than the deprecated `RetrievalQA` chain — retrieval, prompting, generation, and output parsing are each explicit, composable steps.
- All API keys and secrets are loaded via `.env` and never hardcoded.
- Logging is handled through a centralized logger (`loguru`-style formatting) across all modules for easier debugging of the retrieval and generation pipeline.

---

## 🗺️ Roadmap / Possible Improvements

- [ ] Add conversation memory for multi-turn follow-up questions
- [ ] Support additional file types (DOCX, TXT)
- [ ] Add citation highlighting in the UI (show exact source passage)
- [ ] Deploy client + server together with a live demo link
- [ ] Add automated tests for the retrieval and generation pipeline

---

## ⚠️ Disclaimer

This project is a **learning/portfolio application** and is **not intended for real medical advice or diagnosis**. It does not replace professional medical consultation.

---

## 👤 Author

Built by **Houcine** as part of a hands-on AI/RAG engineering portfolio.
Follow the build process: **[@houcine.dev](https://instagram.com/houcine.ai)** — *Decode Data*
