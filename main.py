""" main file to start the chatbot """
# Base
import logging
import time
# Repo imports
from settings import Settings
settings = Settings()
from src.clients.embeder import Embeder
embeder = Embeder(large=False)
from src.models.message import Message
message = Message(
    user_id='1234567890',
    chat_id='qwertyuio',
    role='me',
    content='what about you?'
)
from src.services.scraper import Scraper
scraper = Scraper()
from src.clients.telegram import Telegram
telegram = Telegram()


if __name__ == "__main__":
    offset = 0
    while True:
        reply = telegram.listener(offset)
        if reply is not None:
            offset = reply["reply_id"] + 1
            print(reply)
        time.sleep(int(settings.LISTENER_AWAITING))
