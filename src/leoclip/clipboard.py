import subprocess

class ClipboardManager:
  @staticmethod
  def get_clipboard_targets() -> (list[str] | list):
    try:
      result = subprocess.run(
        ['xclip', '-selection', 'clipboard', '-t', 'TARGETS', '-o'],
        capture_output=True, text=True, timeout=1
      )
      return result.stdout.splitlines()
    except Exception:
      return []

  @staticmethod
  def get_image_binary() -> (bytes | None):
    try:
      return subprocess.check_output(
        ['xclip', '-selection', 'clipboard', '-t', 'image/png', '-o'],
        stderr=subprocess.DEVNULL
      )
    except subprocess.CalledProcessError:
      return None

  @staticmethod
  def set_image_from_path(filepath) -> bool:
    try:
      subprocess.run(
        f"xclip -selection clipboard -t image/png -i '{filepath}'",
        shell=True, check=True
      )
      return True
    except subprocess.CalledProcessError:
      return False

  @staticmethod
  def get_text_content() -> str:
    try:
      return subprocess.check_output(
        ['xclip', '-selection', 'clipboard', '-o'],
        stderr=subprocess.DEVNULL, text=True
      )
    except subprocess.CalledProcessError:
      return ""

  @staticmethod
  def set_text_content(text: str) -> None:
    p = subprocess.Popen(
      ['xclip', '-selection', 'clipboard'],
      stdin=subprocess.PIPE, text=True
    )
    p.communicate(input=text)