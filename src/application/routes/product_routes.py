from fastapi import APIRouter

product_router = APIRouter()


@product_router.get("/products")
def list_products():
    products = [
        {"id": 1, "name": "Product A"},
        {"id": 2, "name": "Product B"}
    ]
    return products
