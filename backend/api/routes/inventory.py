from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.product import Product
from models.representante import Representante
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.inventory_dao import InventoryDao


inventory_routes = APIRouter()

# retorna productos de un pais y region en especifico
@inventory_routes.get('/inventory/c/', response_model=ApiResponse)
async def products_for_country(country: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        inventory_dao = InventoryDao(conn.content)
        products = inventory_dao.get_inventory_for_country(country)
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
@inventory_routes.get('/inventory/cr/', response_model=ApiResponse)
async def products_for_country_region(country: str, region: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        inventory_dao = InventoryDao(conn.content)
        products = inventory_dao.get_inventory_for_country_region(country, region)
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
@inventory_routes.get('/inventory/crh/', response_model=ApiResponse)
async def products_for_country_region_warehouse(country: str, region: str, warehouse:int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        inventory_dao = InventoryDao(conn.content)
        products = inventory_dao.get_inventory_for_country_region_warehouse(country, region, warehouse)
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