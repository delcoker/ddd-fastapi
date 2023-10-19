from src.application.services.country_service import CountryService
from src.domain.services.country_data_aggregation_service import CountryDataAggregationService


class CountryServiceImpl(CountryService):  # country page
    def __init__(self, country_data_aggregation_service: CountryDataAggregationService):
        self.country_data_aggregation_service = country_data_aggregation_service

    def get_country_data(self, country_code, admcode):
        return self.country_data_aggregation_service.get_country_geo_data(country_code, admcode)

