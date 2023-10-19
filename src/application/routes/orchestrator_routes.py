from typing import Annotated
from fastapi import APIRouter, Depends

from container import get_orchestrator_service
from src.application.services.orchestrator_service import OrchestratorService
from src.infrastructure.models.dto.user_dto import UserDto

orchestrator_router = APIRouter(prefix='/orchestrator')

OrchestratorServiceDependency = Annotated[OrchestratorService, Depends(get_orchestrator_service)]


@orchestrator_router.get('/functional', response_model=None)
def get_orchestrator_functional(orchestrator_service: OrchestratorServiceDependency):
    return orchestrator_service.get_functional_data()


@orchestrator_router.get('/api')
def get_orchestrator_api(orchestrator_service: OrchestratorServiceDependency):
    return orchestrator_service.get_api_data()


@orchestrator_router.get('/db', response_model=list[UserDto])
def get_orchestrator_db(orchestrator_service: OrchestratorServiceDependency):
    return orchestrator_service.get_db_data()
