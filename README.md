<div align="center">
  <img src="assets/logo.png" alt="LeoClip Logo" width="150" height="auto" />
  <h1>LeoClip</h1>
  <p>
    <b>A minimalist, multimedia clipboard manager for i3wm built with Python & SQLite.</b>
  </p>
  
  <p>
    <a href="#-installation-arch-linux">Installation</a> •
    <a href="#-configuration-i3wm">Configuration</a> •
    <a href="#-usage">Usage</a> •
    <a href="#-roadmap">Roadmap</a>
  </p>
</div>

<br />

## 📦 Installation

LeoClip can be installed natively on Arch Linux or run via a Python virtual environment on any distribution.

### Option 1: Manual Build (Recommended)

This method installs LeoClip as a system package using `pacman`, managing all dependencies automatically.

1.  **Clone the repository:**
```bash
git clone https://github.com/leonardopolicarpo/leoclip.git
cd leoclip
```

2.  **Build and Install:**
```bash
makepkg -si
```

3.  **Done!** `leoclip-daemon` and `leoclip-menu` are now installed globally in `/usr/bin`.

*(Note: AUR package `leoclip` coming soon for `yay -S leoclip`)*

---

### Option 2: Development Mode (Virtual Environment)

If you want to contribute, modify the code, or run LeoClip on a non-Arch distro, use the editable install method.

1.  **Install system prerequisites:**
```bash
sudo pacman -S xclip rofi
```

2.  **Clone and create a virtual environment:**
```bash
git clone https://github.com/leonardopolicarpo/leoclip.git
cd leoclip
python -m venv .venv
source .venv/bin/activate
```

3.  **Install in editable mode:**
```bash
pip install -e .
```

---

## ⚙️ Configuration (i3wm)

Add the daemon and the menu shortcut to your i3 config file.

### 1. Open your config:
```bash
nano ~/.config/i3/config
```

### 2. Add the following lines:

**For Option 1 (Global Install - Recommended):**
```i3
# --- LeoClip Configuration ---

# Start the daemon in background (monitors clipboard)
exec_always --no-startup-id leoclip-daemon

# Keybinding to open the history menu (Mod + Shift + V)
bindsym $mod+Shift+v exec --no-startup-id leoclip-menu
```

> **Note for Option 2 (Dev Mode) users:** You must point to the absolute path of the venv binaries instead. Example:
> `exec_always --no-startup-id /home/user/leoclip/.venv/bin/leoclip-daemon`

### 3. Reload i3:
Press <kbd>Mod</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> to reload i3.

---

## 🏃‍♂️ Usage

1. Copy any text or image normally (<kbd>Ctrl</kbd> + <kbd>C</kbd> / Right Click > Copy Image).
2. Press <kbd>Mod</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> to open the menu.

### ⌨️ Menu Shortcuts

| Keybinding | Action | Description |
| :--- | :--- | :--- |
| <kbd>Enter</kbd> | **Restore** | Copies the selected text or image back to the clipboard. |
| <kbd>Ctrl</kbd> + <kbd>Delete</kbd> | **Delete** | Permanently removes the item from history (and disk). |
| <kbd>Ctrl</kbd> + <kbd>S</kbd> | **Save** | Saves the image to `~/Pictures/Screenshots` (Images only). |
| <kbd>Shift</kbd> + <kbd>Delete</kbd> | **Clear All** | **Nuclear Option:** Wipes the entire database and cache. |

> **Note:** The database is stored locally at `~/.local/share/leoclip/history.db`.

---

## 🗺️ Roadmap

- [x] Core Daemon (SQLite persistence)
- [x] Rofi Menu Integration
- [x] Image and Screenshot support 📸
- [x] History Management (Delete items, Clear all) 🧹
- [x] Arch Linux Package (`PKGBUILD`) 📦
- [ ] AUR Submission

---

<div align="center">
  Made with 🐍 and ❤️ by <a href="https://github.com/leonardopolicarpo">Leonardo Policarpo</a>
</div>