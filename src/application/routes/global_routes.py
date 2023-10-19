from typing import Annotated

from fastapi import APIRouter, Depends

from container import get_global_data_service
from src.application.services.global_service import GlobalService

global_router = APIRouter(prefix='/global')

GlobalDataServiceDependency = Annotated[GlobalService, Depends(get_global_data_service)]


@global_router.get('', response_model=None)
def get_global_data(global_data_service: GlobalDataServiceDependency):
    return global_data_service.get_global_data()


# @global_router.get('/conflict')
# def get_conflict_data(global_data_service: GlobalDataServiceDependency):
#     return global_data_service.get_conflict_data()
#
#
# @global_router.get('/hazards')
# def get_hazards(global_data_service: GlobalDataServiceDependency):
#     return global_data_service.get_hazard_data()
