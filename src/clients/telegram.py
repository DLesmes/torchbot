""" Telegram API """
# base
import requests
import logging
# Repo imports
from settings import Settings
settings = Settings()


class Telegram:
    """ Telegram API """
    def __init__(self):
        self.url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}"

    def viewer(self, offset=None):
        """ Viewer API """
        try:
            url = self.url + "/getUpdates"
            params = {'offset': offset} if offset else {}
            res = requests.get(url, params=params)
            res.raise_for_status()  # Will raise an HTTPError if the status is 4xx or 5xx
            if res.status_code <= 201:
                return res.json()

        except Exception as e:
            default_error_message = f"Error getting updates: {e}"
            if 'res' in locals() and hasattr(res, 'status_code'):
                error_message = {
                    "status code": res.status_code,
                    "details": res.json() if res.status_code != 204 else 'No content'
                }
                logging.error(f"Response Error: {error_message}")
            return default_error_message

    def listener(self, offset):
        """ Listener API """
        try:
            updates = self.viewer(offset)
            if "result" in updates:
                if len(updates.get("result")) > 0:
                    for update in updates.get("result"):
                        message = update.get("message")
                        reply_id = update.get("update_id")
                        return {
                            "message": message,
                            "reply_id": reply_id
                        }
                else:
                    return None
        except Exception as e:
            default_error_message = f"Error getting listening the UI: {e}"
            logging.error(default_error_message)
            return default_error_message

    def replier(
            self,
            chat_id: str,
            content: str
    ):
        """ replier API """
        try:
            url = self.url + "/sendMessage"
            params = {"chat_id": chat_id, "text": content}
            res = requests.post(url, params=params)  # Will raise an HTTPError if the status is 4xx or 5xx
            if res.status_code <= 201:
                return res.json()
        except Exception as e:
            default_error_message = f"Error getting updates: {e}"
            if 'res' in locals() and hasattr(res, 'status_code'):
                error_message = {
                    "status code": res.status_code,
                    "details": res.json() if res.status_code != 204 else 'No content'
                }
                logging.error(f"Response Error: {error_message}")
            return default_error_message
