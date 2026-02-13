<div align="center">
  <img src="assets/logo.png" alt="LeoClip Logo" width="150" height="auto" />
  <h1>LeoClip</h1>
  <p>
    <b>A minimalist clipboard manager for i3wm built with Python & SQLite.</b>
  </p>
  
  <p>
    <a href="#-prerequisites">Prerequisites</a> •
    <a href="#-installation-dev-mode">Installation</a> •
    <a href="#-configuration-i3wm">Configuration</a> •
    <a href="#-usage">Usage</a> •
    <a href="#-roadmap">Roadmap</a>
  </p>
</div>

<br />

## 🛠️ Prerequisites

Before installing LeoClip, ensure you have the necessary system dependencies.
LeoClip relies on **xclip** for clipboard interaction and **rofi** for the UI.

**Arch Linux:**

```bash
sudo pacman -S xclip rofi
```

## 📥 Installation (Dev Mode)

Since LeoClip is currently in development, the best way to install it is by cloning the repository and using `pip` in editable mode. This allows you to modify the code and see changes immediately.

### 1. Clone the repository:

```bash
git clone https://github.com/leonardopolicarpo/leoclip.git
cd leoclip
```

### 2. Create a virtual environment (Recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the package:

```bash
pip install -e .
```

*This command installs dependencies and creates the `leoclip-daemon` and `leoclip-menu` binaries in your local environment.*

## ⚙️ Configuration (i3wm)

To make LeoClip part of your workflow, add the daemon and the menu shortcut to your i3 config file.

### 1. Open your i3 config:

```bash
nano ~/.config/i3/config
```

### 2. Add the following lines:

**Important:** Replace `/path/to/leoclip` below with the actual directory where you cloned the repository.
*(Tip: Run `pwd` inside the folder to get the full path)*.

```i3
# --- LeoClip Configuration ---

# Start the daemon in background (monitors clipboard)
# Point strictly to the binary inside the .venv
exec_always --no-startup-id /path/to/leoclip/.venv/bin/leoclip-daemon

# Keybinding to open the history menu (Mod + Shift + V)
bindsym $mod+Shift+v exec --no-startup-id /path/to/leoclip/.venv/bin/leoclip-menu
```

### 3. Reload i3:
Press <kbd>Mod</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> to reload i3 and start the daemon.

## 🏃‍♂️ Usage

1. Copy any text normally (<kbd>Ctrl</kbd> + <kbd>C</kbd>).

2. Press <kbd>Mod</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> (or your configured keybinding).

3. Select an item from the **Rofi** list.
  - The selected text is copied back to your clipboard.

4. Paste it where you want (<kbd>Ctrl</kbd> + <kbd>V</kbd>).

> **Note:** The database is stored locally at `~/.local/share/leoclip/history.db`.

---

## 🗺️ Roadmap

- [x] Core Daemon (SQLite persistence)
- [x] Rofi Menu Integration
- [x] Image and Screenshot support 📸
- [ ] History Management (Delete items, Clear all)
- [ ] **v0.2.0:** AUR Package (`PKGBUILD`)

---

<div align="center">
  Made with 🐍 and ❤️ by <a href="https://github.com/leonardopolicarpo">Leonardo Policarpo</a>
</div>
