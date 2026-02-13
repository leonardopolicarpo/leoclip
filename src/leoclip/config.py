import os

BASE_DIR = os.path.expanduser("~/.local/share/leoclip")
CACHE_DIR = os.path.expanduser("~/.cache/leoclip")

DB_PATH = os.path.join(BASE_DIR, "history.db")
IMAGES_DIR = os.path.join(CACHE_DIR, "images")

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

ROFI_THEME = """
* {
  bg:      #1a1b26;
  bg-alt:  #24283b;
  fg:      #c0caf5;
  accent:  #7aa2f7;
  select:  #33467c;
  text-select: #ffffff;
  
  background-color: transparent;
  text-color: @fg;
  font: "JetBrainsMono Nerd Font 10";
}

window {
  width: 50%;
  background-color: @bg;
  border: 2px;
  border-color: @accent;
  border-radius: 10px;
}

mainbox {
  padding: 12px;
  background-color: @bg;
}

inputbar {
  children: [prompt, entry];
  background-color: @bg-alt;
  border-radius: 6px;
  padding: 10px;
  margin: 0 0 10px 0;
}

prompt {
  background-color: @accent;
  text-color: @bg;
  padding: 4px 10px;
  border-radius: 4px;
  margin: 0 10px 0 0;
}

entry {
  placeholder: "Search clips...";
  placeholder-color: #565f89;
  vertical-align: 0.5;
}

listview {
  lines: 12;
  columns: 1;
  fixed-height: true;
  scrollbar: false;
  spacing: 5px;
  background-color: @bg;
}

element {
  padding: 10px;
  border-radius: 6px;
  spacing: 12px;
  background-color: @bg;
}

element selected.normal, element selected.active {
  background-color: @select;
  text-color: @text-select;
}

element-icon {
  size: 4ch;
  vertical-align: 0.5;
  background-color: transparent;
}

element-text {
  vertical-align: 0.5;
  width: 100%;
  background-color: transparent;
  text-color: inherit;
}
"""
