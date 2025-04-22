from config import settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Data Retrieval
# ----------------
# Responsible for splitting, embedding, and building a retriever.

def build_retriever(documents):
    """
    Split documents into chunks, embed them, and return a Retriever.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )
    text_chunks = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(
        openai_api_key=settings.OPENAI_API_KEY
    )
    vectorstore = FAISS.from_documents(text_chunks, embeddings)
    return vectorstore.as_retriever()