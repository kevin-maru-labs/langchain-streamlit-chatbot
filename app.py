import uuid

import streamlit as st
from dotenv import load_dotenv

from agent import get_agent
from threads import add_thread, load_threads

load_dotenv()

st.set_page_config(page_title="Memory Chatbot", layout="wide")
st.divider()
st.caption("Built by Kevin Maru")
st.caption("[GitHub](https://github.com/kevin-maru-labs) · [LinkedIn](https://www.linkedin.com/in/kevin.maru)")

agent = get_agent()

# Pick active thread
if "thread_id" not in st.session_state:
    threads = load_threads()
    if threads:
        st.session_state.thread_id = threads[0]["id"]
    else:
        st.session_state.thread_id = str(uuid.uuid4())
        add_thread(st.session_state.thread_id)

st.title(f"Chatbot with Memory: {st.session_state.thread_id[:8]}")

# Sidebar: new chat + thread picker
with st.sidebar:
    st.header("Chats")
    if st.button("➕ New Chat", use_container_width=True):
        new_id = str(uuid.uuid4())
        add_thread(new_id)
        st.session_state.thread_id = new_id
        st.rerun()

    threads = load_threads()
    if threads:
        labels = [t["label"] for t in threads]
        ids = [t["id"] for t in threads]
        current_index = ids.index(st.session_state.thread_id)
        picked_label = st.selectbox("Previous chats", labels, index=current_index)
        picked_id = ids[labels.index(picked_label)]
        if picked_id != st.session_state.thread_id:
            st.session_state.thread_id = picked_id
            st.rerun()

    st.caption(f"Active thread:\n`{st.session_state.thread_id}`")

# Main chat area
config = {"configurable": {"thread_id": st.session_state.thread_id}}
snapshot = agent.get_state(config)

for msg in snapshot.values.get("messages", []):
    if msg.type == "human":
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif msg.type == "ai" and msg.content:
        with st.chat_message("assistant"):
            st.markdown(msg.content)

if prompt := st.chat_input("Say something..."):
    agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config,
    )
    st.rerun()