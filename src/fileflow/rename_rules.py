# TODO
import sqlite3
from typing import List, Dict

class DatabaseManager:
    """
    Stub database manager using SQLite.
    """

    def __init__(self, db_path: str = "qilife_db.sqlite"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._init_tables()

    def _init_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id TEXT PRIMARY KEY,
                original_name TEXT,
                suggested_name TEXT,
                status TEXT
            )
            """
        )
        self.conn.commit()

    def get_database_stats(self) -> Dict[str, int]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM reviews")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM reviews WHERE status='pending'")
        pending = cursor.fetchone()[0]
        # embeddings count stub
        return {
            "total_files": total,
            "pending_reviews": pending,
            "total_embeddings": 0
        }

    def get_pending_reviews(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, original_name, suggested_name FROM reviews WHERE status='pending'"
        )
        rows = cursor.fetchall()
        return [
            {"id": r[0], "original_name": r[1], "suggested_name": r[2]}
            for r in rows
        ]

    def approve_file_rename(self, file_id: str, new_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE reviews SET status='approved', suggested_name=? WHERE id=?",
            (new_name, file_id)
        )
        self.conn.commit()

    def reject_file_rename(self, file_id: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE reviews SET status='rejected' WHERE id=?",
            (file_id,)
        )
        self.conn.commit()

    def export_logs(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM reviews")
        rows = cursor.fetchall()
        return [
            {"id": r[0], "original_name": r[1], "suggested_name": r[2], "status": r[3]}
            for r in rows
        ]

    def clear_all_data(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM reviews")
        self.conn.commit()
