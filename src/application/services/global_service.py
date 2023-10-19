from abc import ABC, abstractmethod


class GlobalService(ABC):
    @abstractmethod
    def get_global_data(self):
        pass
