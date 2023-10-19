from loguru import logger

from src.domain.repositories.api.api_repository import ApiRepository
from src.domain.services.country_data_aggregation_service import CountryDataAggregationService


class CountryDataAggregationServiceImpl(CountryDataAggregationService):

    def __init__(self, country_geo_data_repository: ApiRepository):
        self.country_geo_data_repository = country_geo_data_repository

    def get_country_geo_data(self, country_code: str, admcode: str):  # admin 1 level data
        api_result = self.country_geo_data_repository.fetch_data(adm0=country_code, admcode=admcode)
        if api_result.is_successful:
            return api_result.response_data.json()
        else:
            logger.error(f'global geo data retrieval was unsuccessful. Error: {api_result.error}')
            print(f'global geo data retrieval was unsuccessful. Error: {api_result.error}')
            pass  # TODO should app crash if it can't find api data
