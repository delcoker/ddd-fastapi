from fastapi import APIRouter
from config import ENVIRONMENT

hello_router = APIRouter()


@hello_router.get('/')
def hello_world():
    return {'Hello': 'FastAPI!',
            "Environment": ENVIRONMENT}


@hello_router.get('/hello/{name}')
def hello_name(name: str):
    return f'Hello {name}!'


@hello_router.get('/hello/{number}')
def hello_number(number: float):
    return f'Hello {number}!'
