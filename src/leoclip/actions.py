import os
import shutil
from datetime import datetime
from .clipboard import ClipboardManager
from .database import Database
from .config import SCREENSHOT_DIR

class ActionHandler:
  @staticmethod
  def restore(content: str, clip_type: str):
    if clip_type == "image":
      if os.path.exists(content):
        ClipboardManager.set_image_from_path(content)
    else:
      ClipboardManager.set_text_content(content)

  @staticmethod
  def delete(content: str, clip_type: str):
    db = Database()
    db.delete_clip(content)

    if clip_type == "image" and os.path.exists(content):
      try:
        os.remove(content)
        print("✅ Cache file removed.")
      except OSError as e:
        print(f"❌ Error deleting file: {e}")

  @staticmethod
  def save_screenshot(content: str, clip_type: str):
    if clip_type != "image" or not os.path.exists(content):
      print("⚠️ Only valid images can be saved to gallery.")
      return
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Screenshot_{timestamp}.png"
    dest_path = os.path.join(SCREENSHOT_DIR, filename)
    
    try:
      shutil.copy2(content, dest_path)
      ClipboardManager.set_image_from_path(dest_path)
      print(f"💾 Saved to: {dest_path}")
    except Exception as e:
      print(f"❌ Error saving screenshot: {e}")

  @staticmethod
  def execute(exit_code: int, content: str, clip_type: str):
    ACTIONS = {
      0: ActionHandler.restore,
      10: ActionHandler.delete,
      11: ActionHandler.save_screenshot
    }

    action = ACTIONS.get(exit_code)
    if action:
      action(content, clip_type)
    else:
      print(f"❓ Unknown action code: {exit_code}")