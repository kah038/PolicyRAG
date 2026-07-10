import chromadb
from langchain_chroma import Chroma

from src.config import COLLECTION_NAME, VECTOR_DB_DIR


def reset_vector_store():
    """Delete the existing policy collection without deleting the database folder."""
    client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))

    existing_collections = {
        collection.name for collection in client.list_collections()
    }

    if COLLECTION_NAME in existing_collections:
        client.delete_collection(name=COLLECTION_NAME)
        print(f"Deleted existing collection: {COLLECTION_NAME}")


def create_vector_store(chunks, embedding_model):
    """Create and persist a fresh Chroma vector collection."""
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name=COLLECTION_NAME,
        persist_directory=str(VECTOR_DB_DIR),
    )


def load_vector_store(embedding_model):
    """Load the existing Chroma vector collection."""
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embedding_model,
    )
    
    