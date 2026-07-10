# AI Tooling Report

## PolicyRAG Enterprise

**Master of Science in Software Engineering (MSSE)**

**Quantic School of Business and Technology**

---

# 1. Introduction

PolicyRAG Enterprise was developed using a combination of modern AI tools and human software engineering practices. AI tools were used to accelerate development, improve code quality, and support documentation while maintaining human oversight throughout the project lifecycle.

The final system design, implementation decisions, testing, and validation remained the responsibility of the developer.

---

# 2. AI Tools Used

| Tool | Purpose |
|------|---------|
| ChatGPT (GPT-5.5) | System design, code generation, debugging, documentation, prompt engineering |
| Groq API | Large Language Model inference for answer generation |
| Hugging Face | Sentence embedding model (all-MiniLM-L6-v2) |
| LangChain | RAG orchestration and prompt management |
| ChromaDB | Vector database for semantic retrieval |
| Streamlit | Interactive web application interface |
| Visual Studio Code | Development environment |
| Git & GitHub | Version control and project management |

---

# 3. How AI Was Used

AI assistance supported several development activities including:

- Designing the Retrieval-Augmented Generation (RAG) architecture.
- Generating initial Python code templates.
- Debugging runtime and dependency issues.
- Improving prompt engineering.
- Explaining technical concepts.
- Drafting technical documentation.
- Assisting with software refactoring.
- Reviewing implementation decisions.

AI was used as a development assistant rather than as an autonomous software developer.

---

# 4. Human Oversight

All AI-generated outputs were reviewed and validated before being incorporated into the project.

Human responsibilities included:

- Selecting the overall system architecture.
- Verifying generated code.
- Testing application functionality.
- Correcting implementation errors.
- Writing and reviewing policy documents.
- Evaluating retrieval quality.
- Measuring system performance.
- Making final engineering decisions.

No AI-generated code was accepted without review.

---

# 5. Prompt Engineering

Prompt engineering played an important role in improving answer quality.

The system prompt instructs the LLM to:

- Use only retrieved policy information.
- Avoid generating unsupported information.
- Produce concise responses.
- Return grounded answers.
- Separate citations from generated text.

These constraints reduce hallucinations and improve response reliability.

---

# 6. Responsible AI Practices

The project followed several responsible AI principles:

- Human oversight of AI-generated outputs.
- Grounded responses using retrieved documents.
- Transparent source citations.
- Hallucination reduction through RAG.
- Evaluation of retrieval accuracy and latency.
- Continuous testing during development.

These practices improve trustworthiness and explainability.

---

# 7. Limitations of AI Assistance

Although AI accelerated development, it has limitations.

Examples include:

- AI-generated code occasionally required debugging.
- Dependency changes required manual correction.
- Prompt wording required iterative refinement.
- AI cannot independently verify system correctness.
- Performance optimisation required empirical testing.

Human review remained essential throughout the project.

---

# 8. Lessons Learned

The project demonstrated that AI can significantly improve software development productivity when combined with human expertise.

Important lessons include:

- RAG substantially reduces hallucinations compared to standalone LLMs.
- Prompt engineering strongly influences answer quality.
- Semantic chunking improves retrieval accuracy.
- Caching greatly reduces response latency.
- Evaluation is essential for validating AI systems.

---

# 9. Conclusion

PolicyRAG Enterprise demonstrates the effective use of AI-assisted software engineering while maintaining human responsibility for design, implementation, testing, and evaluation.

AI served as an engineering assistant rather than a replacement for human decision-making, enabling faster development while preserving software quality, transparency, and accountability.

