from abc import ABC, abstractmethod
from typing import Any, Iterable

class DatabaseClient(ABC):
    
    def __init__(self, config: dict):
        self.config = config
        self.connection = None
        
    @abstractmethod
    def connect(self) -> None:
        ...
        
    @abstractmethod
    def close(self) -> None:
        ...
        
    @abstractmethod
    def execute(self, query: str, params: dict | None = None) -> None:
        ...
        
    @abstractmethod
    def fetch_all(self, query: str, params: dict | None = None) -> Iterable[Any]:
        ...    
        