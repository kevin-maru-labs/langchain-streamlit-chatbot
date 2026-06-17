# LangChain Streamlit Chatbot

A ChatGPT-style chatbot with persistent conversations and live web search, built on LangChain and LangGraph with a Streamlit interface.

**Live demo:** https://kevin-maru-langchain-chatbot.streamlit.app/

## What it does

A multi-conversation chat assistant. Each conversation is a separate thread with its own memory, so you can switch between chats from the sidebar and pick up where you left off. When a question needs current information, the assistant searches the web; for things you told it earlier in the same conversation, it answers from memory.

## Features

- Multi-thread conversations with a ChatGPT-style sidebar: start a new chat, switch between past chats
- Per-thread short-term memory, so each conversation keeps its own history
- Web search as an agent tool, used automatically when a question needs up-to-date information
- Clean separation between the agent, storage, and UI layers

## How it works

- **Agent:** built with LangChain's `create_agent`, running on the LangGraph runtime
- **Memory:** LangGraph's SQLite checkpointer persists each conversation by `thread_id`
- **Model:** OpenAI `gpt-5.4-mini`
- **Web search:** Tavily, wired in as an agent tool
- **Interface:** Streamlit

## Project structure

```
app.py             Streamlit UI: layout, sidebar, chat rendering, input handling
agent.py           Builds the LangGraph agent (model, tools, checkpointer), cached
threads.py         Conversation-thread persistence (create, list, save)
config.py          Constants: file paths, model name, system prompt
requirements.txt   Dependencies
```
## Notes

Memory is scoped to each conversation thread and intended as short-term, session-level context. On the hosted demo, history is held in the app's local storage and stays available while the app is running.

## Author

Built by Kevin Maru ([GitHub](https://github.com/kevin-maru-labs), [LinkedIn](https://www.linkedin.com/in/kevinmaru))