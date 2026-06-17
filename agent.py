import sqlite3

import streamlit as st
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver

from config import CHECKPOINT_DB, MODEL_NAME, SYSTEM_PROMPT

@st.cache_resource
def get_agent():
    conn = sqlite3.connect(CHECKPOINT_DB, check_same_thread=False)
    checkpointer = SqliteSaver(conn=conn)
    checkpointer.setup()

    model = ChatOpenAI(model=MODEL_NAME, temperature=0)
    tavily_tool = TavilySearch(
        max_results=3,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=False,
        include_images=False,
    )
    return create_agent(
        model=model,
        tools=[tavily_tool],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )