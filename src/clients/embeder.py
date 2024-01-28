""" embeddings generator """

from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.embeddings import HuggingFaceInstructEmbeddings


class Embeder:
    """
    Creates embeddings (numerical representations) of text documents for various tasks like semantic search and
    similarity comparison. Provides flexibility to choose between a large model for more comprehensive
    embeddings or a smaller, faster model.

    Attributes:

    large (bool): Flag indicating whether to use the large embedding model (default: True).
    model (str): Name of the embedding model to use.
    device (str): Device to use for computations (default: "cpu").
    """
    def __init__(
            self,
            large: bool = True
    ):
        """
        init(self, large: bool = True) -> None
            Initializes the class with the specified model size preference.
        """
        self.large = large
        if self.large:
            self.model = "hkunlp/instructor-large"
            self.device: str = "cpu"
        else:
            self.model = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    def instructor(self):
        if self.large:
            embed = HuggingFaceInstructEmbeddings(
                model_name=self.model,
                model_kwargs={"device": self.device}
            )
        else:
            embed = SentenceTransformerEmbeddings(
                model_name=self.model
            )
        return embed

    def run(
            self,
            docs_list: list,
    ):
        """
        run(self, docs_list: list) -> List[List[float]]:
            Generates embeddings for the provided list of documents.
            Returns a list of lists, where each inner list represents the embedding vector for a document.
        """
        if docs_list is None:
            docs_list = ['']
        embed = self.instructor()

        return embed.embed_documents(docs_list)
