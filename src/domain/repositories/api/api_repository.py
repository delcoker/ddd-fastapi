from abc import ABC, abstractmethod

from src.infrastructure.models.dto.api_result import ApiResult


class ApiRepository(ABC):

    @abstractmethod
    def fetch_data(self, **kwargs) -> ApiResult:
        pass
