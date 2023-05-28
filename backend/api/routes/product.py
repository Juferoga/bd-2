from fastapi import APIRouter
from models.product import Product
from typing import List

product_routes = APIRouter()

@product_routes.post('/product/create')
def create(product: Product):
    print(product.dict())
    return "success"


@product_routes.post('/product/edit')
def edit(product: Product):
    print(product.dict())
    return "success"


@product_routes.post('/product/delete')
def edit(product: Product):
    print(product.dict())
    return "success"


@product_routes.get('/product/all', response_model=List[Product])
def get_users():
    return "success"