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
from src.clients.llm import Model
model = Model()

if __name__ == "__main__":
    chatbot = Chat(
        user_id='3003713784',
        chat_id=0
    )
    memory = chatbot.memory()
    print(memory)
    res = model.chat(
        user_input='why did you save me?',
        history=memory
    )
    print(res)
