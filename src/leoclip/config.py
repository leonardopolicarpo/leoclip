import os

BASE_DIR = os.path.expanduser("~/.local/share/leoclip")
CACHE_DIR = os.path.expanduser("~/.cache/leoclip")

DB_PATH = os.path.join(BASE_DIR, "history.db")
IMAGES_DIR = os.path.join(CACHE_DIR, "images")

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)