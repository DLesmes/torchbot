""" main file to start the chatbot """
# Base
import logging
import time
# Repo imports
from settings import Settings
settings = Settings()
from src.clients.embeder import Embeder
embeder = Embeder(large=False)
from src.services.scraper import Scraper
scraper = Scraper()
from src.services.chat import Chat
from src.models.message import Message
from src.services.retriever import Retriever
retriever = Retriever()
from src.clients.llm import Model
model = Model()

if __name__ == "__main__":
    chatbot = Chat(
        user_id='3013713784',
        chat_id=0
    )
    memory = chatbot.memory()
    print(memory)
    docs = retriever.query(""" python import torch import torch.nn as nn import torch.nn.functional as F import torch.optim as optim import os from torchvision import datasets, transforms from torch.optim.lr_scheduler import StepLR import torch._lazy import torch._lazy.ts_backend import torch._lazy.metrics torch._lazy.ts_backend.init() if __name__ == '__main__': bsz = 64 device = 'lazy' epochs = 14 log_interval = 10 lr = 1 gamma = 0.7 train_kwargs = {'batch_size': bsz} # if we want to use CUDA if """)
    res = model.chat(
        user_input='what are its main parameters??',
        history=memory,
        technical_documentation=docs
    )
    print(res)
