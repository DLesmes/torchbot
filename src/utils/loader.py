""" Python module for loading class"""
import jsonlines
from langchain.schema import Document


class DocsJSONLLoader:
    """
     Class for loading documentation documents from a JSON Lines (JSONL) file.

    Attributes:
        file_path (str): Path to the JSONL file to be loaded.

    Raises:
        FileNotFoundError: If the specified file path is not found.
        JSONDecodeError: If the JSONL file is invalid.

    Returns:
        A list of Document objects containing page content and metadata.
    """

    def __init__(self, file_path: str):
        """
        __init__(self, file_path: str) -> None:
            Initializes the loader with the file path.
        """
        self.file_path = file_path

    def load(self):
        """
        load(self) -> List[Document]:

        Loads documents from the initialized file path and returns them as a list of Document objects.
        """
        with jsonlines.open(self.file_path) as reader:
            documents = []
            for obj in reader:
                page_content = obj.get("text", "")
                metadata = {
                    "title": obj.get("title", ""),
                    "repo_owner": obj.get("repo_owner", ""),
                    "repo_name": obj.get("repo_name", ""),
                }
                documents.append(Document(page_content=page_content, metadata=metadata))
        return documents
