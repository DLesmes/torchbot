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
from src.clients.llm import Model
model = Model()


class Agent:
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
            if len(memory) > int(settings.MAX_MEMORY):
                memory = [memory[0]] + memory[-10:]
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
                    # RAG process
                    technical_documentation = retriever.query(reply['message']['text'])
                    print(technical_documentation)
                    if len(technical_documentation) > 0:
                        docs = """. Take into account technical documentation from the different libraries and published papers:
                        {technical_documentation}"""
                        technical_documentation = ', '.join(technical_documentation)
                        docs = docs.format(technical_documentation=technical_documentation)
                        augmented_reply = f"""{reply['message']['text']}{docs}"""
                    else:
                        print('There is no technical documentation')
                        augmented_reply = reply['message']['text']
                    # saving the conversation
                    message = Message(
                        user_id=self.user_id,
                        role='user',
                        content=augmented_reply,
                        timestamp=reply['message']['date']
                    )
                    message.update()
                    # Ask the model to get the answer
                    memory = self.memory()
                    print(memory)
                    model_answer = model.chat(
                        user_input=augmented_reply,
                        history=memory
                    )
                    message = Message(
                        user_id=self.user_id,
                        role='assistant',
                        content=model_answer
                    )
                    message.update()
                    print(model_answer)
                    telegram.replier(
                        chat_id=reply['message']['chat']['id'],
                        content=model_answer
                    )
                time.sleep(int(settings.LISTENER_AWAITING))
        except Exception as e:
            default_error_message = f"Error starting the agent: {e}"
            logging.error(default_error_message)
            return default_error_message
