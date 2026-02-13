import sqlite3
from typing import List, Tuple
from .config import DB_PATH

class Database:
  def __init__(self):
    self.db_path = DB_PATH
    self._init_db()

  def _get_connection(self):
    return sqlite3.connect(self.db_path)
  
  def _init_db(self):
    with self._get_connection() as conn:
      conn.execute(
        '''CREATE TABLE IF NOT EXISTS clipboard(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT UNIQUE NOT NULL,
            type TEXT DEFAULT 'text',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
          )'''
      )
      conn.execute("CREATE INDEX IF NOT EXISTS idx_timestamp ON clipboard(timestamp DESC)")

  def save_clip(self, content: str, clip_type: str = "text"):
    with self._get_connection() as conn:
      conn.execute(
        "DELETE FROM clipboard WHERE content = ? AND type = ?",
        (content, clip_type)
      )
      conn.execute(
        "INSERT INTO clipboard (content, type) VALUES (?, ?)",
        (content, clip_type)
      )

  def get_recent_clips(self, limit: int = 20) -> List[Tuple[str, str]]:
    with self._get_connection() as conn:
      return conn.execute(
        "SELECT content, type FROM clipboard ORDER BY timestamp DESC LIMIT ?",
        (limit,)
      ).fetchall()