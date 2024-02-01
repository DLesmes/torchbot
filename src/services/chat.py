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
from src.services.retriever import Retriever
retriever = Retriever()

class Chat:
    """ chat service """
    def __init__(self, user_id: str):
        self.offset = 0
        self.user_id = user_id

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
                        user_id=self.user_id,
                        role='user',
                        content=reply['message']['text'],
                        timestamp=reply['message']['date']
                    )
                    message.update()
                    res = retriever.query(reply['message']['text'])
                    print(res)
                time.sleep(int(settings.LISTENER_AWAITING))
        except Exception as e:
            default_error_message = f"Error chatting: {e}"
            logging.error(default_error_message)
            return default_error_message
