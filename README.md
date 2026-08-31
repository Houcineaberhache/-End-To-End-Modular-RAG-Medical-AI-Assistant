📅 AI Medical Assistant Chatbot — RAG-based Application

🗂️ Architecture PDF: View Architecture

🧠 Project Overview
This application is a Medical Domain Chatbot built using Retrieval-Augmented Generation (RAG). It allows users to upload their own medical documents (e.g., textbooks, reports), and the system intelligently answers queries by retrieving the most relevant content before generating a final response.

🎓 What is RAG?
RAG (Retrieval-Augmented Generation) enhances language models by supplying relevant external context from a knowledge base, preventing hallucinations and improving accuracy, especially for factual or specialized domains like medicine.

🔄 Architecture
User Input
   ↓
Query Embedding → Pinecone Vector DB ← Embedded Chunks ← Chunking ← PDF Loader
   ↓
Retrieved Docs
   ↓
     RAG Chain (Groq + LangChain)
   ↓
LLM-generated Answer
For a detailed view, refer to the MedicalAssistant.pdf

📚 Features
Upload medical PDFs (notes, books, etc.)
Auto-extracts text and splits into semantic chunks
Embeds using Google/BGE embeddings
Stores vectors in Pinecone DB
Uses Groq's LLaMA3-70B via LangChain
FastAPI backend with endpoints for file upload and Q&A
🌐 Tech Stack
Component	Tech Used
LLM	Groq API (LLaMA3-70B)
Embeddings	Google Generative AI / BGE
Vector DB	Pinecone
Framework	LangChain
Backend	FastAPI
Deployment	Render
📚 API Endpoints
POST /upload_pdfs/ --- Upload one or more PDF files

POST /ask/ --- Ask a question --- Form field: `question`
📁 Folder Structure
└── 📁assets
    ├── DIABETES.pdf
    ├── MedicalAssistant.pdf
    └── medicalAssistant.png
└── 📁client
    └── 📁__pycache__
        ├── config.cpython-311.pyc
    └── 📁components
        └── 📁__pycache__
            ├── chatUI.cpython-311.pyc
            ├── history_download.cpython-311.pyc
            ├── upload.cpython-311.pyc
        ├── chatUI.py
        ├── history_download.py
        ├── upload.py
    └── 📁utils
        └── 📁__pycache__
            ├── api.cpython-311.pyc
        ├── api.py
    ├── app.py
    ├── config.py
    └── requirements.txt
└── 📁server
    └── 📁__pycache__
        ├── logger.cpython-311.pyc
        ├── main.cpython-311.pyc
        ├── test.cpython-311.pyc
    └── 📁middlewares
        └── 📁__pycache__
            ├── exception_handlers.cpython-311.pyc
        ├── exception_handlers.py
    └── 📁modules
        └── 📁__pycache__
            ├── llm.cpython-311.pyc
            ├── load_vectorstore.cpython-311.pyc
            ├── query_handlers.cpython-311.pyc
        ├── llm.py
        ├── load_vectorstore.py
        ├── pdf_handlers.py
        ├── query_handlers.py
    └── 📁routes
        └── 📁__pycache__
            ├── ask_question.cpython-311.pyc
            ├── upload_pdfs.cpython-311.pyc
        ├── ask_question.py
        ├── upload_pdfs.py
    └── 📁uploaded_docs
        ├── DIABETES.pdf
        ├── Supratim Nag - LOR.pdf
    ├── .env
    ├── logger.py
    ├── main.py
    ├── requirements.txt
    └── test.py

