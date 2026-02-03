import sqlite3
import subprocess
import pyperclip
from .config import DB_PATH

def get_clips():
  with sqlite3.connect(DB_PATH) as conn:
    return conn.execute("SELECT content FROM clipboard ORDER BY timestamp DESC LIMIT 20").fetchall()

def show_menu():
  items = get_clips()
  if not items:
    return

  options = "\n".join([item[0].replace("\n", "  ")[:100] for item in items])
  
  rofi_proc = subprocess.Popen(
    ['rofi', '-dmenu', '-i', '-p', '📋 History', '-format', 'i', '-l', '15'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    encoding='utf-8'
  )
  
  selected_index_str, _ = rofi_proc.communicate(input=options)

  if not selected_index_str.strip():
    return
  
  try:
    index = int(selected_index_str.strip())
    full_content = items[index][0]
    pyperclip.copy(full_content)
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
  show_menu()