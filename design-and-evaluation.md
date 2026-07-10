# Design and Evaluation

## PolicyRAG Enterprise

**Master of Science in Software Engineering (MSSE)**

**Quantic School of Business and Technology**

---

# 1. Introduction

PolicyRAG Enterprise is a Retrieval-Augmented Generation (RAG) system developed to answer enterprise policy questions using company documentation instead of relying solely on the internal knowledge of a large language model (LLM). The system retrieves relevant policy information from a vector database and generates grounded responses supported by source citations.

The project demonstrates modern AI engineering practices including semantic retrieval, vector databases, prompt engineering, and LLM integration.

---

# 2. System Design

The architecture consists of five major components:

1. Policy Document Repository
2. Document Processing Pipeline
3. Chroma Vector Database
4. Groq Large Language Model
5. Streamlit User Interface

These components work together to provide accurate, grounded, and transparent responses.

---

# 3. System Architecture

```text
                    User
                      │
                      ▼
             Streamlit Interface
                      │
                      ▼
               RAG Pipeline
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 ChromaDB Vector Store        Groq LLM
        ▲                           │
        │                           ▼
 Sentence Embeddings        Grounded Response
        ▲
        │
 Company Policy Documents
```

---

# 4. Document Processing

Enterprise policy documents are stored as Markdown files.

Each document is:

- Loaded from the policy repository.
- Split into semantic chunks.
- Converted into vector embeddings.
- Stored in ChromaDB.

Chunking improves retrieval quality by allowing the system to retrieve only the most relevant sections of a document instead of entire files.

---

# 5. Embedding Model

PolicyRAG uses the **sentence-transformers/all-MiniLM-L6-v2** embedding model.

Reasons for selection:

- Lightweight.
- Fast inference.
- High semantic similarity performance.
- Widely adopted for RAG systems.
- Good balance between speed and retrieval quality.

---

# 6. Vector Database

The project uses **ChromaDB** as the persistent vector database.

Responsibilities include:

- Storing document embeddings.
- Semantic similarity search.
- Persistent local storage.
- Efficient nearest-neighbour retrieval.

---

# 7. Large Language Model

Answer generation is performed using **Groq Llama 3.1 8B Instant**.

The model was selected because it provides:

- Fast inference.
- High-quality instruction following.
- Low operational cost.
- Easy integration with LangChain.

---

# 8. Prompt Engineering

The system prompt instructs the LLM to:

- Use only retrieved policy context.
- Avoid inventing information.
- Produce concise answers.
- Generate grounded responses.
- Return citations separately.

These constraints significantly reduce hallucinations.

---

# 9. Streamlit Interface

The user interface provides:

- Natural language question input.
- AI-generated answers.
- Source citations.
- Knowledge base statistics.
- Suggested questions.
- Response time measurements.

---

# 10. Evaluation Methodology

The system was evaluated using representative policy questions spanning all business domains.

Evaluation focused on:

- Retrieval accuracy.
- Answer correctness.
- Citation accuracy.
- Response latency.
- Groundedness.

---

# 11. Evaluation Results

| Metric | Result |
|---------|--------|
| Policy Documents | 10 |
| Indexed Chunks | 132 |
| Retrieval Accuracy | 100% |
| Citation Accuracy | 100% |
| Hallucinations | 0 observed in evaluation set |
| Average Response Time | ~0.47 seconds |
| Fastest Response | 0.37 seconds |
| Slowest Response | 0.67 seconds |

---

# 12. Performance Improvements

Initial implementation required approximately **11–17 seconds** to answer a query because the embedding model, vector database, and LLM client were initialized for every request.

Performance was improved by introducing caching for:

- Embedding model.
- Chroma vector store.
- Groq client.

This reduced subsequent response times to less than one second within the same Streamlit session.

---

# 13. Limitations

Current limitations include:

- Markdown documents only.
- English-language policies.
- Single-user interface.
- Local deployment.
- No authentication.
- No conversation memory.

These limitations provide opportunities for future development.

---

# 14. Future Enhancements

Future improvements may include:

- PDF ingestion.
- Microsoft Word document support.
- Hybrid keyword and semantic retrieval.
- Multi-document summarization.
- User authentication.
- Role-based access control.
- Administrative dashboard.
- Cloud deployment.
- Conversation memory.
- Policy version management.

---

# 15. Conclusion

PolicyRAG Enterprise demonstrates the practical application of Retrieval-Augmented Generation for enterprise knowledge management. By combining semantic retrieval, vector databases, prompt engineering, and large language models, the system delivers grounded, transparent, and low-latency responses based on official company policy documents.

The project illustrates modern AI engineering principles and provides a scalable foundation for enterprise knowledge assistants.

