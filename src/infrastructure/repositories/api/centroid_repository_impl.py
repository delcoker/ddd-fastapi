import requests

from src.domain.repositories.api.api_repository import ApiRepository
from src.infrastructure.models.dto.api_result import ApiResult


class CentroidRepositoryImpl(ApiRepository):

    def __init__(self, centroid_uri, ):
        self.centroid_uri = centroid_uri

    def fetch_data(self) -> ApiResult:
        url = self.centroid_uri

        try:
            response = requests.get(url)
            return ApiResult(response_data=response)
        except Exception as e:
            return ApiResult(error=e)
