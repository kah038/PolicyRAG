# 📘 PolicyRAG Enterprise

**A Retrieval-Augmented Generation (RAG) AI Assistant for Enterprise Policy Management**

PolicyRAG Enterprise is an AI-powered assistant that answers employee questions using official company policy documents. Instead of relying on a large language model's internal knowledge, the system retrieves relevant policy documents from a vector database and generates grounded responses with source citations.

This project was developed as part of the **AI Engineering Project** for the **Master of Science in Software Engineering (MSSE)** program at **Quantic School of Business and Technology**.

---

## Project Objectives

The objectives of this project are to:

- Build a Retrieval-Augmented Generation (RAG) system.
- Implement semantic search using vector embeddings.
- Reduce hallucinations by grounding responses in company policies.
- Provide transparent answers with source citations.
- Deliver a responsive web-based interface for enterprise users.

---

## Key Features

- Enterprise AI policy assistant
- Retrieval-Augmented Generation (RAG)
- Semantic document search
- ChromaDB vector database
- Hugging Face sentence embeddings
- Groq Llama 3.1 large language model
- Source citations for every answer
- Streamlit web interface
- Fast response times through model caching

---

## Knowledge Base

The system indexes ten enterprise policy documents:

1. Employee Handbook
2. Leave Policy
3. Remote Work Policy
4. Information Security Policy
5. Acceptable Use Policy
6. Expense Reimbursement Policy
7. Code of Conduct
8. Data Privacy Policy
9. Health and Safety Policy
10. Business Travel Policy

Current knowledge base statistics:

- **Policy documents:** 10
- **Indexed chunks:** 132
- **Embedding model:** all-MiniLM-L6-v2
- **Vector database:** ChromaDB

---

## System Architecture

```text
                 User
                   │
                   ▼
          Streamlit Web Interface
                   │
                   ▼
            RAG Pipeline
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 ChromaDB Vector Store     Groq LLM
        ▲                     │
        │                     ▼
 Hugging Face Embeddings   Grounded Answer
        ▲
        │
 Company Policy Documents
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.11 |
| Web Framework | Streamlit |
| RAG Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | all-MiniLM-L6-v2 |
| Large Language Model | Groq Llama 3.1 |
| Environment Management | Python Virtual Environment |

---

## Project Structure

```text
PolicyRAG/
│
├── app.py
├── ingest.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── llm.py
│
├── data/
│   └── policies/
│
├── chroma_db/
│
├── evaluation/
│
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PolicyRAG.git
cd PolicyRAG
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

Build the vector database:

```bash
python ingest.py
```

Run the application:

```bash
streamlit run app.py
```

---

## Example Questions

- How many annual leave days do employees receive?
- Can employees use public Wi-Fi?
- Can I install software on my work laptop?
- What is considered a conflict of interest?
- Who should I report a phishing email to?
- Is PPE mandatory?
- Can the company sell my personal information?
- Are meals reimbursed during business travel?

---

## Performance

Evaluation results demonstrated:

- **10 policy documents indexed**
- **132 searchable chunks**
- **100% retrieval accuracy** (evaluation set)
- **100% citation accuracy** (evaluation set)
- **Grounded responses using retrieved context**
- **Average response time:** ~0.47 seconds after caching

---

## Future Enhancements

Potential future improvements include:

- Multi-document summarization
- User authentication and role-based access
- PDF and Microsoft Word document ingestion
- Hybrid search (semantic + keyword)
- Conversation history
- Administrative dashboard
- Policy version control
- Support for additional enterprise knowledge bases

---

## Author

**Lukas Kahare**

Master of Science in Software Engineering (MSSE)

Quantic School of Business and Technology

AI Engineering Project

---

## License

This project was developed for academic purposes as part of the MSSE AI Engineering course.

