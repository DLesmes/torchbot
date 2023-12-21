""" main file to start the chatbot """
# Base
import datetime
import logging
# Repo
from src.utils.transform import create_dir, remove_existing_file
from src.config.config import load_config
from src.clients.github import process_directory


def scraper():
    """
    """
    config = load_config()

    current_date = datetime.date.today().strftime("%Y_%m_%d")
    jsonl_file_name = f"data/docs_en_{current_date}.jsonl"

    create_dir("data/")
    remove_existing_file(jsonl_file_name)

    for repo_info in config["github"]["repos"]:
        process_directory(
            repo_info["path"],
            repo_info,
            jsonl_file_name
        )


if __name__ == "__main__":
    scraper()


