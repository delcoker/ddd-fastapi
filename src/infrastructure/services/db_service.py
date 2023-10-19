from abc import ABC, abstractmethod
from typing import Optional, Dict


class DatabaseService(ABC):

    @abstractmethod
    def get_orm(self):
        """Retrieve the initialized db instance."""
        pass

    @abstractmethod
    def execute_raw_query(self, query: str) -> bool:
        pass

    @abstractmethod
    def execute_sql_scripts_from_directory(self, directory_path: str,
                                           replacements: Optional[Dict[str, str]] = None) -> None:
        pass
