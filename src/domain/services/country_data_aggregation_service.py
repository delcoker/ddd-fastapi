from abc import ABC, abstractmethod


class CountryDataAggregationService(ABC):

    @abstractmethod
    def get_country_geo_data(self, country_code: str, admcode: str):  # admin 1 level data
        pass
