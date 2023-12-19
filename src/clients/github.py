"""github API client"""
import datetime
import json
import os
from typing import Dict

import requests
from termcolor import colored
from utils.transform import preprocess_text


def download_file(url: str, repo_info: dict, jsonl_file_name: str) -> None:
    """
    Downloads a file from a URL and saves it in a JSONL file.

    Args:
        url (str): URL from which the file is downloaded.
        repo_info (dict): Information about the repository from which the file is downloaded.
        jsonl_file_name (str): Name of the JSONL file where the downloaded file is saved.

    Returns:
        None.

    Raises:
        TypeError: If the `url` argument is not a string.
        TypeError: If the `repo_info` argument is not a dictionary.
        TypeError: If the `jsonl_file_name` argument is not a string.
        RuntimeError: If the file could not be downloaded.
    """
    response = requests.get(url)
    filename = url.split("/")[-1]
    text = response.text

    if text is not None and isinstance(text, str):
        text = preprocess_text(text)

        file_dict = {
            "title": filename,
            "repo_owner": repo_info["owner"],
            "repo_name": repo_info["repo"],
            "text": text,
        }

        with open(jsonl_file_name, "a") as jsonl_file:
            jsonl_file.write(json.dumps(file_dict) + "\n")
    else:
        print(f"Texto no esperado: {text}")


def process_directory(
    path: str,
    repo_info: Dict,
    headers: Dict,
    jsonl_file_name: str,
) -> None:
    """
    Processes a directory in a GitHub repository and downloads the files in it.

    Args:
        path (str): Path of the directory to process.
        repo_info (Dict): Information about the repository that contains the directory.
        headers (Dict): Headers for the request to the GitHub API.
        jsonl_file_name (str): Name of the JSONL file where the downloaded files will be saved.

    Returns:
        None.

    Raises:
        TypeError: If the `path` argument is not a string.
        TypeError: If the `repo_info` argument is not a dictionary.
        TypeError: If the `headers` argument is not a dictionary.
        TypeError: If the `jsonl_file_name` argument is not a string.
        RuntimeError: If the directory could not be processed.
    """
    # Si el nombre del directorio es 'zh', lo omite y retorna inmediatamente.
    # Esta característica está implementada para no descargar las traducciones en chino.
    if os.path.basename(path) == "zh":
        print(
            colored(
                f"Se omite el directorio 'zh' (traducciones en chino): {path}", "yellow"
            )
        )
        return

    base_url = f"https://api.github.com/repos/{repo_info['owner']}/{repo_info['repo']}/contents/"
    print(
        colored(f"Procesando directorio: {path} del repo: {repo_info['repo']}", "blue")
    )
    response = requests.get(base_url + path, headers=headers)

    if response.status_code == 200:
        files = response.json()
        for file in files:
            if file["type"] == "file" and (
                file["name"].endswith(".mdx") or file["name"].endswith(".md")
            ):
                print(colored(f"Descargando documento: {file['name']}", "green"))
                print(colored(f"Descarga URL: {file['download_url']}", "cyan"))
                download_file(
                    file["download_url"],
                    repo_info,
                    jsonl_file_name,
                )
            elif file["type"] == "dir":
                process_directory(
                    file["path"],
                    repo_info,
                    headers,
                    jsonl_file_name,
                )
        print(colored("Exito en extracción de documentos del directorio.", "green"))
    else:
        print(
            colored(
                "No se pudieron recuperar los archivos. Verifique su token de GitHub y los detalles del repositorio.",
                "red",
            )
        )
