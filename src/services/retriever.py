""" retriever module to get the embeddings """
# base

# repo imports
from settings import Settings
settings = Settings()
from src.clients.embeder import Embeder
embeder = Embeder()
from src.utils.loader import DocsJSONLLoader
# langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


class Retriever:
    """ retriever
    Retrieves the embeddings from a vectorial database
    """
    def __init__(self):
        """ initialize the retriever
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=int(settings.CHUNK_SIZE),
            length_function=len,
            chunk_overlap=int(settings.CHUNK_OVERLAP)
        )
        self.index_name = settings.CHROMA_NAME_INDEX

    def set(self, path: str = settings.DOCS_PATH):
        """
         update the vectorial database
        """
        loader = DocsJSONLLoader(path)
        data = loader.load()
        splitter = self.text_splitter
        documents = splitter.split_documents(data)
        instructor = embeder.instructor()
        vector_db = Chroma.from_documents(
            documents=documents,
            embedding=instructor,
            persist_directory=self.index_name
        )
        vector_db.persist()

    def query(
            self,
            message: str,
            k: int = int(settings.K)
    ):
        """ retrieve the 2 more similar text chunks based on the message given
        """
        vectorial_db = Chroma(
            embedding_function=embeder.instructor(),
            persist_directory=self.index_name
        )
        res = vectorial_db.similarity_search_with_score(message, k=k)
        return [vector[0].page_content for vector in res if vector[1] < 0.25]
