import os
import time
import uuid
from .config import IMAGES_DIR
from .clipboard import ClipboardManager
from .database import Database
from .utils import calculate_hash

def main():
  db = Database()
  print(f"LeoClip Daemon v0.2.0 started.")

  last_hash = ""

  while True:
    try:
      targets = ClipboardManager.get_clipboard_targets()

      if 'image/png' in targets:
        image_data = ClipboardManager.get_image_binary()

        if image_data:
          current_hash = calculate_hash(image_data)

          if current_hash != last_hash:
            filename = f"img_{uuid.uuid4()}.png"
            filepath = os.path.join(IMAGES_DIR, filename)

            with open(filepath, "wb") as f:
              f.write(image_data)

            print(f"Image saved: {filename}")

            db.save_clip(filepath, clip_type='image')
            last_hash = current_hash
      
      elif 'UTF8_STRING' in targets or 'STRING' in targets:
        text = ClipboardManager.get_text_content()
        if text.strip():
          current_hash = calculate_hash(text.encode('utf-8'))

          if current_hash != last_hash:
            db.save_clip(text, clip_type='text')
            last_hash = current_hash
    
    except Exception as e:
      print(f"Error: {e}")
    
    time.sleep(1.5)

if __name__ == "__main__":
  main()