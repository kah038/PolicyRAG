from pathlib import Path

from src.config import POLICY_DIR


def test_policy_directory_exists():
    assert POLICY_DIR.exists()
    assert POLICY_DIR.is_dir()


def test_policy_corpus_contains_ten_documents():
    policy_files = list(Path(POLICY_DIR).glob("*.md"))
    assert len(policy_files) == 10


def test_policy_documents_are_not_empty():
    for policy_file in Path(POLICY_DIR).glob("*.md"):
        assert policy_file.stat().st_size > 0
        
        