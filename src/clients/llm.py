""" LLM Client using langchain """

# langchain
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    PromptTemplate
)
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory

# repo
from settings import Settings
settings = Settings()
from src.config.config import YamlLoader
yamlloader = YamlLoader(settings.VERSION)


class Model:
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

    def chat(
        self,
        user_input: str,
        history: list
    ):
        """
        Use a LLM to generate an answer to the user

        :param user_input: user input
        :param history: memory
        :return: the object to interact with the LLM
        """
        if self.prompt['supplier'] == 'openai':
            llm = ChatOpenAI(
                model=self.prompt['model'],
                temperature=self.prompt['temperature'],
                max_tokens=self.prompt['max_tokens'],
                model_kwargs=self.kwars
            )
            system = f"""System: {history[0][1]}"""
            pre_template = """
{chat_history}
Human: {user_input}
AI:
            """
            template = system+pre_template
            prompt = PromptTemplate(
                input_variables=["chat_history", "user_input"], template=template
            )
            memory = ConversationBufferMemory(memory_key="chat_history", prompt_input_key="user_input")
            for reply in range(1, len(history),2):
                if len(history) > 0:
                    memory.save_context(
                    {"input": history[reply][1]},
                    {"output": history[reply+1][1]}
                    )
            chat = LLMChain(
                llm=llm,
                prompt=prompt,
                memory=memory,
                verbose=True
            )
            return chat.predict(user_input=user_input)
