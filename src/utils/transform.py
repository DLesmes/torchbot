"""Method to help process"""
# base
import re
import emoji
import os
import yaml


def preprocess_text(text: str) -> str:
    """
        Preprocesses text by removing unwanted patterns and characters.

    Args:
        text (str): The text to preprocess.

    Returns:
        The preprocessed text.
    """
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"Copyright.*", "", text)
    text = text.replace("\n", " ")
    text = emoji.demojize(text)
    text = re.sub(r":[a-z_&+-]+:", "", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def create_dir(path: str) -> None:
    """
    Creates a directory if it doesn't already exist.

    Args:
        path (str): The path to the directory to create.

    Raises:
        OSError: If the directory couldn't be created for some reason.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def remove_existing_file(file_path: str) -> None:
    """
    Removes a file if it already exists.

    Args:
        file_path (str): The path to the file to remove.

    Raises:
        OSError: If the file couldn't be removed for some reason.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
