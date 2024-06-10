<div align="center">

<h1><code>simple-chat</code>

A simple, transparent, and extensible web client to chat with your LLM

</div>

### 🤔 Why? 

There are lots of ever more powerful open LLMs ([HF hub](https://huggingface.co/models)), wonderful frameworks to build (train or merge) your own models ([trl](https://huggingface.co/docs/trl/en/index), [axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)), as well as reliable and efficient solutions to serve your models ([vllm](https://docs.vllm.ai/en/stable/), [tgi](https://huggingface.co/docs/text-generation-inference/index)). But, or so I find, there are relatively few simple local chat clients that work well with custom (self-hosted) LLMs and allow you to use your models in a straightforward way.

### 🎉 What?

`simple-chat` is a minimalistic chat client that runs locally (in your browser) and connects to a local or remote LLM. It works out of the box, but can also be used as a boilerplate to build more sophisticated agents.

### 🔢 How?

1. Clone the repository.

    ```bash
    git clone https://github.com/debatelab/simple-chat.git
    cd simple-chat
    ```

2. Set base URL. Create a text file named `.env` (e.g. with text editor) that contains the following line:

    ```
    BASE_URL="<insert-your-inference-server-url-here>"
    ```

3. [Install poetry](https://python-poetry.org/docs/#installation) (python package manager) and its [dotenv pluging](https://pypi.org/project/poetry-dotenv/).

4. Install the dependencies.

    ```bash
    poetry install
    ```

5. Run the app.

    ```bash
    poetry run chainlit run src/simple_chat/app.py
    ```

### 🙏 Cudos

Built with

* [Chainlit](https://github.com/Chainlit/chainlit)
* [LangChain](https://github.com/langchain-ai/langchain)
