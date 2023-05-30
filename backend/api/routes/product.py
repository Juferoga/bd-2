from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.product import Product
from models.representante import Representante
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.product_dao import ProductDao
from models.product import FilterRegionCounty


product_routes = APIRouter()


@product_routes.get('/product/get', response_model=ApiResponse)
async def get_product_all(current_user: UserOfDB = Depends(get_current_user)):
    response = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    if response.success:
        product_dao = ProductDao(response.content)
        products = product_dao.get_all_products()
        if not isinstance(products, list) and not all(isinstance(product, Product) for product in products):
            del product_dao
            return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=products,message="error")
        del product_dao
        return ApiResponse(status=status.HTTP_200_OK,data=products,message="success")
    else:
        return ApiResponse(status=status.HTTP_200_OK,data="error",message=response.content)

@product_routes.get('/product/filter', response_model=ApiResponse)
async def filter_products(region: str, country: str, current_user: UserOfDB = Depends(get_current_user)):
    response = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    if response.success:
        product_dao = ProductDao(response.content)
        products = product_dao.get_filter_products(FilterRegionCounty(region=region, country=country))
        if not isinstance(products, list) and not all(isinstance(product, Product) for product in products):
            del product_dao
            return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=products,message="error")
        del product_dao
        return ApiResponse(status=status.HTTP_200_OK,data=products,message="success")
    else:
        return ApiResponse(status=status.HTTP_200_OK,data="error",message=response.content)


