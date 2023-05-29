from fastapi import APIRouter, Depends, status, Response
from models.user import User, UserOfDB, get_current_user
from models.product import Product
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.product_dao import ProductDao

product_routes = APIRouter()

@product_routes.get('/product/get', response_model=ApiResponse)
async def get_product_all(current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    product_dao = ProductDao(conn)
    products = product_dao.get_all_products()
    if not isinstance(products, list) and not all(isinstance(product, Product) for product in products):
        del product_dao
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=products,message="error")
    del product_dao
    return ApiResponse(status=status.HTTP_200_OK,data=products,message="success")

# @product_routes.post('/product/add')
# def create_product(product: Product):
#     print(product.dict())
#     return "success"


# @product_routes.post('/product/set')
# def edit_product(product: Product):
#     print(product.dict())
#     return "success"


# @product_routes.post('/product/del')
# def edit_product(product: Product):
#     print(product.dict())
#     return "success"