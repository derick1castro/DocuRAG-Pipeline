import os
from dotenv import load_dotenv

load_dotenv()  # lê .env na raiz

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))
    MODEL: str = os.getenv("MODEL", 'gpt-4o')

settings = Settings()
