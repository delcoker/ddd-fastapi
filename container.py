from fastapi import Depends

import config
from src.application.services.country_service import CountryService
from src.application.services.country_service_impl import CountryServiceImpl
from src.application.services.global_service import GlobalService
from src.application.services.global_service_impl import GlobalServiceImpl
from src.application.services.orchestrator_service import OrchestratorService
from src.application.services.orchestrator_service_impl import OrchestratorServiceImpl
from src.domain.repositories.api.api_repository import ApiRepository
from src.domain.repositories.db.user_repository import UserRepository
from src.domain.services.country_data_aggregation_service import CountryDataAggregationService
from src.domain.services.country_data_aggregation_service_impl import CountryDataAggregationServiceImpl
from src.domain.services.global_data_aggregation_service import GlobalDataAggregationService
from src.domain.services.global_data_aggregation_service_impl import GlobalDataAggregationServiceImpl
from src.infrastructure.repositories.api.api_repository_impl import ApiRepositoryImpl
from src.infrastructure.repositories.api.centroid_repository_impl import CentroidRepositoryImpl
from src.infrastructure.repositories.api.country_geo_repository_impl import CountryGeoRepositoryImpl
from src.infrastructure.repositories.api.global_geo_repository_impl import GlobalGeoRepositoryImpl
from src.infrastructure.repositories.db.user_repository_impl import UserRepositoryImpl
from src.infrastructure.services.db_service import DatabaseService
from src.infrastructure.services.db_service_impl import DatabaseServiceImpl

GLOBAL_GEO_DATA_URI = "https://api.vam.wfp.org/geodata/WorldCountries?vamds=0"
COUNTRY_GEO_DATA_URI = "https://api.vam.wfp.org/geodata/GetGeoAdmins?vamds=0"
CENTROID_DATA_URI = "https://api.vam.wfp.org/geodata/GetGeoAdmins?wrongEndpoint=0"


# infrastructure
def get_db_service() -> DatabaseService:
    return DatabaseServiceImpl(config.DB_HOST, config.DB_INSTANCE,
                               config.DB_USER, config.DB_PASSWORD,
                               config.DB_NAME, config.DB_PORT,
                               config.DB_DRIVER, config.DB_TLS)


def get_global_geo_repository() -> ApiRepository:
    return GlobalGeoRepositoryImpl(GLOBAL_GEO_DATA_URI)


def get_centroid_repository() -> ApiRepository:
    return CentroidRepositoryImpl(CENTROID_DATA_URI)


def get_user_repository(db_service=Depends(get_db_service)) -> UserRepository:
    return UserRepositoryImpl(db_service)


def get_country_geo_data_repository() -> ApiRepository:
    return CountryGeoRepositoryImpl(COUNTRY_GEO_DATA_URI)


def get_api_repository() -> ApiRepository:
    return ApiRepositoryImpl()


# domain
def get_global_data_aggregation_service(global_geo_data_repository=Depends(get_global_geo_repository),
                                        centroid_repository=Depends(get_centroid_repository)
                                        ) -> GlobalDataAggregationService:
    return GlobalDataAggregationServiceImpl(global_geo_data_repository, centroid_repository,
                                            )


def get_country_data_aggregation_service(country_geo_data_repository=Depends(get_country_geo_data_repository)
                                         ) -> CountryDataAggregationService:
    return CountryDataAggregationServiceImpl(country_geo_data_repository)


# application

def get_orchestrator_service(api_repository=Depends(get_api_repository),
                             user_repository=Depends(get_user_repository)) -> OrchestratorService:
    return OrchestratorServiceImpl(api_repository, user_repository)


def get_global_data_service(global_data_aggregation_service=Depends(get_global_data_aggregation_service)
                            ) -> GlobalService:
    return GlobalServiceImpl(global_data_aggregation_service)


def get_country_data_service(country_data_aggregation_service=Depends(get_country_data_aggregation_service)
                             ) -> CountryService:
    return CountryServiceImpl(country_data_aggregation_service)
