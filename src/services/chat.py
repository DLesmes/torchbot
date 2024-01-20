""" chat service """

# Base
import logging
import time
# Repo imports
from settings import Settings
settings = Settings()
from src.models.message import Message
from src.clients.telegram import Telegram
telegram = Telegram()


class Chat:
    """ chat service """
    def __init__(self):
        self.offset = 0

    def start(self):
        """ start the chat
        """
        try:
            while True:
                reply = telegram.listener(self.offset)
                if reply is not None:
                    self.offset = reply["reply_id"] + 1
                    logging.info(reply)
                    print(reply)
                    message = Message(
                        user_id=reply['message']['from']['id'],
                        chat_id=reply['message']['chat']['id'],
                        role='user',
                        content=reply['message']['text'],
                        timestamp=reply['message']['date']
                    )
                    message.save()
                time.sleep(int(settings.LISTENER_AWAITING))
        except Exception as e:
            default_error_message = f"Error chatting: {e}"
            logging.error(default_error_message)
            return default_error_message
