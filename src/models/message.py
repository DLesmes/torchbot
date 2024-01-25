""" Message Model """

import json
import os
import uuid
import time


class Message:
    def __init__(
            self,
            user_id: str,
            chat_id: int = -1,
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
        return {
            'reply_id': self.reply_id,
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp
        }

    def system_reply(self):
        return {
            'reply_id': self.reply_id,
            'role': 'system',
            'content': 'prompt system',
            'timestamp': self.timestamp
        }

    def new_user(self):
        dict_history = json.load(open(self.file))
        if self.user_id not in dict_history.keys():
            dict_history[self.user_id] = [{'full_chat': [self.system_reply()]}]
            dict_history[self.user_id][self.chat_id]['full_chat'].append(self.reply())
            json.dump(dict_history, open(self.file, 'w'))
        else:
            self.new_chat()

    def new_chat(self):
        dict_history = json.load(open(self.file))
        if self.user_id in dict_history.keys():
            dict_history[self.user_id].append({'full_chat': [self.system_reply()]})
            dict_history[self.user_id][self.chat_id]['full_chat'].append(self.reply())
            json.dump(dict_history, open(self.file, 'w'))
        else:
            self.new_user()

    def update(self):
        dict_history = json.load(open(self.file))
        if self.user_id in dict_history.keys():
            dict_history[self.user_id][int(self.chat_id)]['full_chat'].append(self.reply())
            json.dump(dict_history, open(self.file, 'w'))
        else:
            self.new_user()
