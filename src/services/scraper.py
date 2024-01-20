""" scraper module to get specilized data """
# Base
import datetime
# Repo
from src.utils.transform import create_dir, remove_existing_file
from src.config.config import load_config
from src.clients.github import process_directory


class Scraper(object):
    """
    Scraper class scrapes documentation files from specified GitHub repositories.
    """
    def __init__(self):
        self.config = load_config()
        self.current_date = datetime.date.today().strftime("%Y_%m_%d")
        self.jsonl_file_name = f"data/docs_en_{self.current_date}.jsonl"

    def run(self):
        """
        Executes scraper and saves documentation

        Raises:
            yaml.YAMLError: If the configuration file cannot be loaded.
            OSError: If there are errors creating directories or removing files.
            RuntimeError: If there are errors processing directories or downloading files.
        """
        create_dir("data/")
        remove_existing_file(self.jsonl_file_name)

        for repo_info in self.config["github"]["repos"]:
            process_directory(
                repo_info["path"],
                repo_info,
                self.jsonl_file_name
            )
