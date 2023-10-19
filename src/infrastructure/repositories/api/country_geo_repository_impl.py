import requests
from src.domain.repositories.api.api_repository import ApiRepository
from src.infrastructure.models.dto.api_result import ApiResult


# Admin 1 level
class CountryGeoRepositoryImpl(ApiRepository):

    def __init__(self, country_geo_data_uri,):
        self.country_geo_data_uri = country_geo_data_uri

    def fetch_data(self, **kwargs) -> ApiResult:
        query_string = "&".join([f"{k}={v}" for k, v in kwargs.items()])
        url = f"{self.country_geo_data_uri}&{query_string}"

        try:
            response = requests.get(url)
            return ApiResult(response_data=response)
        except Exception as e:
            return ApiResult(error=e)
