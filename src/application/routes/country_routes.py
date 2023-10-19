from typing import Annotated

from fastapi import APIRouter, Depends

from container import get_country_data_service
from src.application.services.country_service import CountryService

country_router = APIRouter(prefix='/country')

CountryDataServiceDependency = Annotated[CountryService, Depends(get_country_data_service)]


@country_router.get('', response_model=None)
def get_country_data(country_data_service: CountryDataServiceDependency,
                     adm0: str = None,
                     admcode: str = None):
    return country_data_service.get_country_data(adm0, admcode)

# @country_router.get('/population')
# def get_population(country_data_service: CountryDataServiceDependency):
#     return country_data_service.get_population_data()
