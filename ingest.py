from src.chunker import chunk_documents
from src.document_loader import load_policy_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store, reset_vector_store


def main():
    print("Resetting existing vector collection...")
    reset_vector_store()

    print("Loading policy documents...")
    documents = load_policy_documents()
    print(f"Loaded {len(documents)} documents.")

    if not documents:
        raise RuntimeError("No non-empty policy documents were found.")

    print("Splitting documents into chunks...")
    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    print("Creating Chroma vector database...")
    vector_store = create_vector_store(chunks, embedding_model)

    stored_count = vector_store._collection.count()

    print("Vector database created successfully.")
    print(f"Stored vectors: {stored_count}")
    print("PolicyRAG ingestion completed.")


if __name__ == "__main__":
    main()
    
    