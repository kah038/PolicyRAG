from langchain_community.document_loaders import TextLoader
from src.config import POLICY_DIR


def load_policy_documents():
    """Load non-empty Markdown policy documents from the policy directory."""
    documents = []

    for file_path in POLICY_DIR.glob("*.md"):
        if file_path.stat().st_size == 0:
            print(f"Skipping empty file: {file_path.name}")
            continue

        loader = TextLoader(str(file_path), encoding="utf-8")
        loaded_docs = loader.load()

        for doc in loaded_docs:
            doc.metadata["source"] = file_path.name
            doc.metadata["file_path"] = str(file_path)

        documents.extend(loaded_docs)

    return documents


