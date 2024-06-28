import os

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable  # noqa: F401
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    base_url = os.environ.get("BASE_URL")
    if not base_url:
        raise ValueError("Missing BASE_URL environment variable.")
    base_url = base_url+"/v1"
    max_tokens = os.environ.get("MAX_TOKENS", 768)
    model = ChatOpenAI(
        base_url=base_url,
        openai_api_key="None",
        max_tokens=max_tokens,
        streaming=True
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                ("You're a very knowledgeable AI Assistant who provides "
                 "accurate and eloquent answers to the user's questions."),
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)
    cl.user_session.set("history", [])


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable
    history = cl.user_session.get("history")  # type: list

    answer = cl.Message(content="")

    async for chunk in runnable.astream(
        {
            "question": message.content,
            "history": history
        },
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await answer.stream_token(chunk)

    history.append({"role": "human", "content": message.content})
    history.append({"role": "ai", "content": answer.content})

    await answer.send()
