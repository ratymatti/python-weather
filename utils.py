import json
import os

HISTORY_FILE = "history.json"

def load_history():
    """Load search history from JSON file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    """Save search history to JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)
