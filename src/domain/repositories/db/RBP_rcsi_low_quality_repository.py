from abc import ABC


class RBP_rcsi_low_quality_repository(ABC):

    def fetch_data(self, skip: int = 0, limit: int = 100):
        pass
