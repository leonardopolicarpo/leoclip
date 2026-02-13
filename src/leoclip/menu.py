import os
import subprocess
from .clipboard import ClipboardManager
from .database import Database
from .config import ROFI_THEME
from .ui import format_item

def show_menu():
  db = Database()
  clips = db.get_recent_clips(limit=20)

  if not clips:
    return

  options = [format_item(c[0], c[1]) for c in clips]
  rofi_input = "\n".join(options)

  rofi_command = [
    'rofi', '-dmenu', '-i',
    '-p', '📋 LeoClip',
    '-format', 'i',
    '-show-icons',
    '-theme-str', ROFI_THEME
  ]
  
  rofi_proc = subprocess.Popen(
    rofi_command,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    encoding='utf-8'
  )
  
  selected_index_str, _ = rofi_proc.communicate(input=rofi_input)

  if not selected_index_str.strip():
    return
  
  try:
    index = int(selected_index_str.strip())
    content, clip_type = clips[index]

    if clip_type == "image":
      if os.path.exists(content):
        success = ClipboardManager.set_image_from_path(content)
        print(f"Image restored!" if success else "Failed to restore image")
    else:
      ClipboardManager.set_text_content(content)

  except Exception as e:
    print(f"Error restoring clip: {e}")

if __name__ == "__main__":
  show_menu()