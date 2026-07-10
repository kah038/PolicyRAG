"""
Configuration settings for PolicyRAG.

Author: Lukas Kahare
Project: PolicyRAG
"""

from pathlib import Path

# -----------------------------
# Project Directories
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
POLICY_DIR = DATA_DIR / "policies"
VECTOR_DB_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "namtech_policies" 

# -----------------------------
# Embedding Model
# -----------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -----------------------------
# Chunking Configuration
# -----------------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# -----------------------------
# Retrieval Configuration
# -----------------------------

TOP_K_RESULTS = 1 