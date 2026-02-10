import time
from .clipboard import ClipboardManager
from .database import Database

def main():
  db = Database()
  db.init_db()
  print(f"LeoClip daemon started.")

  last_content = ClipboardManager.get_current_content()

  while True:
    try:
      current_content = ClipboardManager.get_current_content()

      if current_content != last_content and current_content.strip():
        db.save_clip(current_content, clip_type='text')
        last_content = current_content

    except Exception as e:
      print(f"Error in daemon loop: {e}")

    time.sleep(1.0)

if __name__ == "__main__":
  main()