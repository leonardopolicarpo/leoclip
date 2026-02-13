# ui.py
import os

def format_item(content: str, clip_type: str) -> str:
  if clip_type == "text":
    display_text = content.replace("\n", " ").replace("\r", " ").strip()
    return f"{display_text}\0icon\x1fedit-copy"
  
  elif clip_type == "image":
    filename = os.path.basename(content)
    return f" {filename}\0icon\x1f{content}"
  
  return "❓ Unknown"