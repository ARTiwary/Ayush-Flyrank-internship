import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Optional
from app.interfaces import ItemRepositoryInterface

class PostgresItemRepository(ItemRepositoryInterface):
    def __init__(self, connection_url: str):
        self.conn_url = connection_url

    def _get_connection(self):
        return psycopg2.connect(self.conn_url, cursor_factory=RealDictCursor)

    def add(self, name: str, description: Optional[str]) -> dict:
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id, name, description, created_at;",
                    (name, description)
                )
                return dict(cursor.fetchone())

    def get_all(self) -> List[dict]:
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, description, created_at FROM items;")
                return [dict(row) for row in cursor.fetchall()]