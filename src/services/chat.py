""" chat service """

# Base
import logging
import time
import json
import os
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
    def __init__(
            self,
            user_id: str,
            chat_id: int = int(-1)
    ):
        self.offset = 0
        self.user_id = user_id
        self.chat_id = chat_id
        self.file = 'data/history.json'
        if not os.path.exists(self.file):
            json.dump({}, open(self.file, 'w'))

    def memory(self):
        """ memory chat """
        dict_history = json.load(open(self.file))
        if self.user_id in dict_history.keys():
            full_chat = dict_history[self.user_id][self.chat_id]['full_chat']
            memory = [(reply['role'], reply['content']) for reply in full_chat]
            return memory
        else:
            return []

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
