from config import settings
from langchain_community.document_loaders import TextLoader

# Data Ingestion
# ----------------
# Responsible for loading raw documents from disk or remote sources.

def ingest_data(file_path: str):
    """
    Load documents from the given file path.
    """
    loader = TextLoader(file_path, encoding="utf8")
    documents = loader.load()
    return documents