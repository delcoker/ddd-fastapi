import requests

from src.domain.repositories.api.api_repository import ApiRepository
from src.infrastructure.models.dto.api_result import ApiResult


# Admin 0 level
class GlobalGeoRepositoryImpl(ApiRepository):

    def __init__(self, global_geo_data_uri):
        self.global_geo_data_uri = f'{global_geo_data_uri}'

    def fetch_data(self) -> ApiResult:
        try:
            response = requests.get(self.global_geo_data_uri)
            return ApiResult(response_data=response)
        except Exception as e:
            return ApiResult(error=e)
