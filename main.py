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


if __name__ == "__main__":
    # chat = Chat('3193713784')
    # chat.start()
    message = Message(
        user_id='3003713784',
        role='user',
        content='saving the 2nd message',
        chat_id=2
    )
    message.update()
