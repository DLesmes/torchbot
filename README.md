# AI Torchbot

Code for a Telegram bot 📠 specialiced on Pytorch LLM powered

## 🤖 Overview
This project aims to simulate a text mesagge chatbot to chat about Pytorch

### 🧡 Explanation of the architecture flow:

1. **User Input**: The user types an input message in the Chatbot UI.
2. **Chatbot UI to Chatbot History**: This message is sent to the Chatbot History where it is stored.
3. **Chatbot UI to Retriever**: The same message is also sent from the Chatbot UI to the Retriever.
4. **Retriever**: The Retriever processes the input message and augments it with information by querying the Vector Database.
5. **Augmented Message**: The Retriever sends this augmented message to the Prompt Storage.
6. **Prompt Storage**: The Prompt Storage receives the augmented message and includes the historical context from the Chatbot History to generate an augmented prompt.
7. **Augmented Prompt to LLM**: This augmented prompt is then sent to the Large Language Model (LLM).
8. **LLM to Chatbot History**: After the LLM generates a response, the full response body is sent back to the Chatbot History.
9. **Response to UI**: The Chatbot History then sends the appropriate part of the LLM's response to the Chatbot UI.
10. **Display to User**: The Chatbot UI displays the answer to the user.

In this streamlined architecture, the Chatbot History serves as the central repository of the interaction history, supporting both the retrieval of historical context and the logging of new interactions, including full responses from the LLM. The Chatbot UI, Retriever, Vector Database, Prompt Storage, and LLM all play roles in a fluid conversation loop, providing the user a seamless chat experience.

## 👌 Features
- **LLM Usage:** Integration with a Large Language Model (LLM) into the conversation
- **Langchaing:** It use lanchain framework to back and forth with differents LLMs
- **Telegram Chatbot API:** It is powered by the Telegram API Interface
- **Open Source Vectorial Database:** The chatbot specialised experience use a vector database to augment the precision of the answers
- **Open Source embeddings:** It use embedding from open source models

### ✍️ Prerequisites
Before you begin, make sure you have the following prerequisites:
- Python 3.9 or later installed
- Docker installed
- Do not forget to set the `.env` file it is not ignored on the repo

## 🧤 Getting Started
Follow these steps to set up and run the project:

1. **Clone the Repository:**
   ```
   git clone git@github.com:DLesmes/torchbot.git
   cd torchbot
   ```
   
2. Set Up Python Virtual Environment with the [requirements.txt](https://github.com/DLesmes/torchbot/blob/main/requirements.txt):

    ```
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```
3. Run the Server:

    ```
    python3 main.py
    ```
You can also debug it in your preferred IDE.


## 🤝 Contributing

Feel free to contribute and make this chatbot project even better!
We welcome contributions from the community! If you'd like to contribute, please follow these steps:

* Fork this repository
* Create a new branch: `git checkout -b feature/YourFeatureName`
* Make your changes and commit them: `git commit -am 'Add some feature'`
* Push to the branch: `git push origin feature/YourFeatureName`
* Create a pull request
We look forward to your contributions!

## 💬 Contact

For any questions or suggestions, feel free to reach out here is [my profile](https://github.com/DLesmes)
