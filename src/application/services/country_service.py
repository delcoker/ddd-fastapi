from abc import ABC, abstractmethod


class CountryService(ABC):
    @abstractmethod
    def get_country_data(self, country_code, admcode):
        pass
