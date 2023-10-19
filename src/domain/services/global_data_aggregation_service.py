from abc import ABC, abstractmethod


class GlobalDataAggregationService(ABC):
    @abstractmethod
    def get_global_data(self):  # admin 0 level data
        pass

