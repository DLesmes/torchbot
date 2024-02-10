"""Settings module"""
import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LISTENER_AWAITING = 1
    VERSION = os.getenv("VERSION")
    DOCS_PATH = os.getenv("DOCS_PATH")
    CHUNK_SIZE = os.getenv("CHUNK_SIZE")
    LENGTH_FUNCTION = os.getenv("LENGTH_FUNCTION")
    CHUNK_OVERLAP = os.getenv("CHUNK_OVERLAP")
    K = os.getenv("K")
    CHROMA_NAME_INDEX = os.getenv("CHROMA_NAME_INDEX")
