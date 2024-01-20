""" main file to start the chatbot """
# Base
import logging
# Repo
from src.clients.embeder import Embeder
embeder = Embeder(large=False)
from src.clients.telegram import print_new_messages
from src.models.message import Message
message = Message(
    user_id='1234567890',
    chat_id='qwertyuio',
    role='me',
    content='what about you?'
)
from src.services.scraper import Scraper
scraper = Scraper()


if __name__ == "__main__":
    scraper.run()
