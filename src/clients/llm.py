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
from src.config.config import YamlLoader
yamlloader = YamlLoader('0.0.0')


class Brain:
    """
    Brain class
    """
    def __init__(self):
        """
        Import all necessary prompt parameters needed to query the LLM, set on config prompt yaml file
        """
        self.prompt = yamlloader.prompts()

    def chat(self):
        """
        Use a LLM to generate an answer to the user
        :return: the object to interact with the LLM
        """
        if self.prompt['supplier'] == 'openai':
            llm = ChatOpenAI(
                model=self.prompt['model'],
                temperature=self.prompt['temperature'],
                max_length=self.prompt['max_length'],
                max_tokens=self.prompt['max_tokens'],
                top_p=self.prompt['top_p']
            )
            prompt = ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(self.prompt['system']),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{user_input}")
                ]
            )
            memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=3)
            chat = LLMChain(llm=llm, prompt=prompt, memory=memory)
            return chat
