import pyperclip

class ClipboardManager:
  @staticmethod
  def get_current_content() -> str:
    return pyperclip.paste()
  
  @staticmethod
  def set_content(content: str):
    pyperclip.copy(content)