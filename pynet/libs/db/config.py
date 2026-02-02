from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    driver: str
    host: str | None = None
    port: int | None = None
    database: str | None = None
    user: str | None = None
    password: str | None = None
    dsn: str | None = None