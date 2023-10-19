from fastapi import APIRouter

from src.application.routes.country_routes import country_router
from src.application.routes.global_routes import global_router
from src.application.routes.hello_routes import hello_router
from src.application.routes.orchestrator_routes import orchestrator_router
from src.application.routes.product_routes import product_router

router = APIRouter()

router.include_router(orchestrator_router)
router.include_router(hello_router)
router.include_router(product_router)
router.include_router(global_router)
router.include_router(country_router)
