""" LLM Client using langchain """

# langchain
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory

# repo
from settings import Settings
settings = Settings()
from src.config.config import YamlLoader
yamlloader = YamlLoader(settings.VERSION)


class Brain:
    """
    Brain class
    """
    def __init__(self):
        """
        Import all necessary prompt parameters needed to query the LLM, set on config prompt yaml file
        """
        self.prompt = yamlloader.prompts()
        self.kwars = {
            # "max_lenght": self.prompt['max_length'],
            "top_p": self.prompt['top_p']
        }

    def chat(self, user_input: str):
        """
        Use a LLM to generate an answer to the user

        :param user_input: user input
        :return: the object to interact with the LLM
        """
        if self.prompt['supplier'] == 'openai':
            llm = ChatOpenAI(
                model=self.prompt['model'],
                temperature=self.prompt['temperature'],
                max_tokens=self.prompt['max_tokens'],
                model_kwargs=self.kwars
            )
            prompt = ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(self.prompt['system']),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template(f"{user_input}")
                ]
            )
            memory = ConversationBufferWindowMemory(
                memory_key="chat_history",
                return_messages=True,
                k=4
            )
            chat = LLMChain(
                llm=llm,
                prompt=prompt,
                memory=memory,
                verbose=True
            )
            return chat.predict(input=user_input)
