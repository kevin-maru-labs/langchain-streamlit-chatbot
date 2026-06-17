CHECKPOINT_DB = "checkpoints.sqlite"
THREADS_FILE = "chat_threads.json"
MODEL_NAME = "gpt-4o-mini"
SYSTEM_PROMPT = (
    "You are a helpful assistant with access to web search. "
    "Use web search when the user asks about current events, recent news, "
    "live data, or anything that needs up-to-date information from the internet. "
    "For personal facts the user told you earlier in the same chat, use memory; "
    "do not search the web."
)