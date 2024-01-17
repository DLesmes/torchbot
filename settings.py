"""Settings module"""
import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
