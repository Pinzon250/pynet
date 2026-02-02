import pyodbc
from pynet.libs.db.base import DatabaseClient

class SQLServerClient(DatabaseClient):
    
    def connect(self) -> None:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.config['host']};"
            f"DATABASE={self.config['database']}"
            f"UID={self.config['user']}"
            f"PWD={self.config['password']}"
        )
        self.connection = pyodbc.connect(conn_str)
        
    def close(self) -> None:
        if self.connection:
            self.connection.close()
    
    def execute(self, query: str, params: dict | None = None) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query, params or {})
        self.connection.commit()
        
    def fetch_all(self, query: str, params: dict | None = None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or {})
        return cursor.fetchall()