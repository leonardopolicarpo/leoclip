import os

DATA_DIR = os.path.expanduser("~/.local/share/leoclip")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "history.db")