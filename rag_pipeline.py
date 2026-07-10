from functools import lru_cache

from langchain_core.prompts import ChatPromptTemplate

from src.config import TOP_K_RESULTS
from src.embeddings import get_embedding_model
from src.llm import get_llm
from src.vector_store import load_vector_store


@lru_cache(maxsize=1)
def get_cached_embedding_model():
    """Load the embedding model once and reuse it."""
    return get_embedding_model()


@lru_cache(maxsize=1)
def get_cached_vector_store():
    """Load the Chroma vector store once and reuse it."""
    embedding_model = get_cached_embedding_model()
    return load_vector_store(embedding_model)


@lru_cache(maxsize=1)
def get_cached_llm():
    """Load the Groq client once and reuse it."""
    return get_llm()


def retrieve_relevant_chunks(question: str):
    """Retrieve the most relevant policy chunks."""
    vector_store = get_cached_vector_store()

    return vector_store.similarity_search(
        question,
        k=TOP_K_RESULTS,
    )


def format_context(retrieved_docs):
    """Format retrieved chunks for the LLM prompt."""
    context_parts = []

    for index, doc in enumerate(retrieved_docs, start=1):
        source = doc.metadata.get("source", "Unknown source")
        chunk_id = doc.metadata.get("chunk_id", "Unknown chunk")

        context_parts.append(
            f"[Source {index}: {source}, Chunk {chunk_id}]\n"
            f"{doc.page_content}"
        )

    return "\n\n".join(context_parts)


def generate_grounded_answer(question: str):
    """Generate a grounded policy answer with citations."""
    question = question.strip()

    if not question:
        return {
            "answer": "Please enter a policy-related question.",
            "citations": [],
        }

    retrieved_docs = retrieve_relevant_chunks(question)

    if not retrieved_docs:
        return {
            "answer": (
                "I can only answer based on the available "
                "NamTech Solutions Ltd policy documents."
            ),
            "citations": [],
        }

    context = format_context(retrieved_docs)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are PolicyRAG, the policy assistant for NamTech Solutions Ltd.

Use only the supplied policy context.

Rules:
- Do not invent facts.
- Answer the user's question directly.
- Keep the answer concise and professional.
- Do not mention chunk numbers in the answer.
- Do not cite filenames inside the answer because citations are displayed separately.
- If the answer is not supported by the context, say:
  "I can only answer based on the available NamTech Solutions Ltd policy documents."
""",
            ),
            (
                "human",
                """
Question:
{question}

Policy context:
{context}
""",
            ),
        ]
    )

    chain = prompt | get_cached_llm()

    result = chain.invoke(
        {
            "question": question,
            "context": context,
        }
    )

    citations = []
    seen = set()

    for doc in retrieved_docs:
        source = doc.metadata.get("source", "Unknown source")
        chunk_id = doc.metadata.get("chunk_id", "Unknown chunk")
        key = (source, chunk_id)

        if key in seen:
            continue

        seen.add(key)

        citations.append(
            {
                "source": source,
                "chunk_id": chunk_id,
                "snippet": doc.page_content[:300],
            }
        )

    return {
        "answer": result.content,
        "citations": citations,
    }


if __name__ == "__main__":
    test_question = "How many annual leave days do employees receive?"
    response = generate_grounded_answer(test_question)

    print(f"\nQuestion: {test_question}\n")
    print("Answer:\n")
    print(response["answer"])

    print("\nCitations:\n")
    for citation in response["citations"]:
        print(citation)
        
        