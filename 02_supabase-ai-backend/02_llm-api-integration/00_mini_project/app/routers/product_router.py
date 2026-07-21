
from fastapi import APIRouter
from app.schemes.product_scheme import ProductPublic
from app.services.product_service import (
    product_create as create_product_service,
    product_get as get_product_service,
    product_get_all as get_all_products_service,
)

product_router = APIRouter()

@product_router.post("/product/create")
def product_create(product:ProductPublic)-> ProductPublic:
    return create_product_service(product)

@product_router.get("/product/get/{product_id}")
def product_get(product_id:int)-> ProductPublic:
    return get_product_service(product_id)

@product_router.get("/product/getall")
def product_all()-> list[ProductPublic]:
    return get_all_products_service()
