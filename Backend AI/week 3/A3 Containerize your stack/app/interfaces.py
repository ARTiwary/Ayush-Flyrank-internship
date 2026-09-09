from abc import ABC, abstractmethod
from typing import List, Optional

class ItemRepositoryInterface(ABC):
    @abstractmethod
    def add(self, name: str, description: Optional[str]) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> List[dict]:
        pass