""" main file to start the chatbot """
# Base
import logging
import time
# Repo imports
from settings import Settings
settings = Settings()
from src.clients.embeder import Embeder
embeder = Embeder(large=False)
from src.services.scraper import Scraper
scraper = Scraper()
from src.services.chat import Chat
from src.models.message import Message
from src.services.retriever import Retriever
retriever = Retriever()

if __name__ == "__main__":
    res = retriever.query('What is a tensor')
    print(res)
