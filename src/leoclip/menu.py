import subprocess
from .database import Database
from .config import ROFI_THEME
from .ui import format_item
from .actions import ActionHandler

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
    '-kb-delete-entry', 'Control+Alt+Shift+z',
    '-kb-custom-3', 'Shift+Delete',
    '-kb-custom-1', 'Control+Delete',
    '-kb-custom-2', 'Control+s',
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
  exit_code = rofi_proc.returncode

  if exit_code == 12:
    ActionHandler.execute(exit_code, "", "")
    return

  if not selected_index_str.strip():
    return
  
  try:
    index = int(selected_index_str.strip())
    content, clip_type = clips[index]
    ActionHandler.execute(exit_code, content, clip_type)

  except Exception as e:
    print(f"Menu Error: {e}")

if __name__ == "__main__":
  show_menu()