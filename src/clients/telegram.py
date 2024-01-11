""" Telegram API """
# base
import requests
import time
# Repo imports
from settings import Settings
settings = Settings()


def get_updates(offset=None):
    """
    Get the latest updates from Telegram API

    :param offset:
    :return: telegram bot API response
    """
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/getUpdates"
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
            print(f"Response Error: {error_message}")
        return default_error_message


def send_messages(chat_id, text):
    """
    Send messages to Telegram API
    :param chat_id: The id of the chat with which to send messages
    :param text: The message to be sent
    :return:
    """
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
        params = {"chat_id": chat_id, "text": text}
        res = requests.post(url, params=params)
        return res
    except Exception as e:
        default_error_message = f"Error getting updates: {e}"
        if 'res' in locals() and hasattr(res, 'status_code'):
            error_message = {
                "status code": res.status_code,
                "details": res.json() if res.status_code != 204 else 'No content'
            }
            print(f"Response Error: {error_message}")
        return default_error_message


def print_new_messages():
    """
    Print new messages
    :return: Print on console the last message received
    """
    try:
        offset = None
        while True:
            updates = get_updates(offset)
            if "result" in updates:
                for update in updates["result"]:
                    message = update["message"]
                    id = message["from"]["id"]
                    username = message["from"]["first_name"]
                    text = message.get("text")
                    print(f"User: {username} ({id})")
                    print(f"Message: {text}")
                    print("-"*20)
                    offset = update["update_id"] + 1
            time.sleep(1)  # wait a sec before return an answer

    except Exception as e:
        default_error_message = f"Error getting updates: {e}"
        return default_error_message
