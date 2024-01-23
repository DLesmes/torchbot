""" Message Model """

import json
import os
import uuid
import time


class Message:
    def __init__(
            self,
            user_id: str,
            chat_id: str,
            role: str = None,
            content: str = None,
            timestamp: str = int(time.time())
    ):
        self.user_id = user_id
        self.chat_id = chat_id
        # TODO: confirm hash method
        self.reply_id = str(uuid.uuid4())
        self.role = role
        self.content = content
        self.timestamp = timestamp
        self.file = 'data/history.json'
        if not os.path.exists(self.file):
            json.dump({}, open(self.file, 'w'))

    def reply(self):
        reply = {
            'reply_id': self.reply_id,
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp
        }
        return reply

    def save(self):
        dict_history = json.load(open(self.file))
        if self.user_id in dict_history:
            temp_dict = dict_history[self.user_id].copy()

            # Modify the copied dictionary
            if self.chat_id in temp_dict:
                temp_dict[self.chat_id].append(self.reply())

            # Update the original dictionary with the modified copy
            dict_history[self.user_id] = temp_dict
        else:
            dict_history[self.user_id] = {self.chat_id: [self.reply()]}
        json.dump(dict_history, open(self.file, 'w'))
