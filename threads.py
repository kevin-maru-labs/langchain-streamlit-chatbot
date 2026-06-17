import json
import os

from config import THREADS_FILE

def load_threads():
    if os.path.exists(THREADS_FILE):
        with open(THREADS_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []

def save_threads(threads):
    with open(THREADS_FILE, "w", encoding="utf-8") as f:
        json.dump(threads, f)

def add_thread(thread_id):
    threads = load_threads()
    if any(t["id"] == thread_id for t in threads):
        return
    threads.insert(0, {"id": thread_id, "label": f"Chat {thread_id[:8]}"})
    save_threads(threads)