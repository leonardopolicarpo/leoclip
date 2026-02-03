import sqlite3
import os
import time
import pyperclip

from .config import DB_PATH

def init_db():
  os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
  
  conn = sqlite3.connect(DB_PATH)
  conn.execute('''CREATE TABLE IF NOT EXISTS clipboard 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  content TEXT UNIQUE, 
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
  conn.commit()
  conn.close()

def save_clip(text):
  text = text.strip()
  if not text: return

  try:
    with sqlite3.connect(DB_PATH) as conn:
      conn.execute("INSERT OR REPLACE INTO clipboard (content) VALUES (?)", (text,))
      conn.execute("DELETE FROM clipboard WHERE id NOT IN (SELECT id FROM clipboard ORDER BY timestamp DESC LIMIT 20)")
      conn.commit()
  except Exception as e:
    print(f"Error saving clip: {e}")

def main():
  init_db()
  print(f"LeoClip daemon started... Database: {DB_PATH}")

  last_clip = ""
  while True:
    try:
      current_clip = pyperclip.paste()
      if current_clip != last_clip:
        save_clip(current_clip)
        last_clip = current_clip
    except Exception as e:
      print(f"Error: {e}")
    time.sleep(1.5)

if __name__ == "__main__":
  main()