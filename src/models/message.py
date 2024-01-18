""" Message Model """

import json
import uuid


class Message:
    def __init__(
            self,
            role: str = None,
            content: str = None,
            timestamp: str = None
    ):
        # TODO: confirm method to make the hash
        self.reply_id = str(uuid.uuid4())
        self.role = role
        self.content = content
        self.timestamp = timestamp
        self.file = 'config/history.json'

    def save(self):
        dict_results = json.load( open( self.file ) )
