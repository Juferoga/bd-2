from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.product import Product
from models.representante import Representante
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.product_dao import ProductDao
from models.product import FilterRegionCounty, CreateProduct


product_routes = APIRouter()

# agrega un producto
@product_routes.post('/product/add', response_model=ApiResponse)
async def create_product(product: CreateProduct, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        conn.content.begin()
        product = product_dao.create_product(product)
        if not product[0]:
            raise Exception(str(product[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# desactivar producto
@product_routes.delete('/product/disable/{id}', response_model=ApiResponse)
async def disable_product(id: int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        conn.content.begin()
        product = product_dao.disable(id)
        if not product[0]:
            raise Exception(str(product[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = product[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@product_routes.get('/product/activate/{id}', response_model=ApiResponse)
async def activate_product(id: int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        conn.content.begin()
        product = product_dao.activate(id)
        if not product[0]:
            raise Exception(str(product[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = product[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response


# retorna todos los productos registrado en el sistema
@product_routes.get('/product/get', response_model=ApiResponse)
async def get_product_all(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        products = product_dao.get_all_products()
        if not products[0]:
            raise Exception(str(products[1]))
        response.status = status.HTTP_200_OK
        response.data = products[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response


# retorna productos de un pais y region en especifico
@product_routes.get('/product/filter/', response_model=ApiResponse)
async def products_for_country(country: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        products = product_dao.get_filter_products(FilterRegionCounty(region=region, country=country))
        if not products[0]:
            raise Exception(str(products[1]))
        response.status = status.HTTP_200_OK
        response.data = products[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# retorna productos de un pais y region en especifico
@product_routes.get('/product/filter', response_model=ApiResponse)
async def filter_products(region: str, country: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        product_dao = ProductDao(conn.content)
        products = product_dao.get_filter_products(FilterRegionCounty(region=region, country=country))
        if not products[0]:
            raise Exception(str(products[1]))
        response.status = status.HTTP_200_OK
        response.data = products[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response
        

