from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from models.country import Country
from dao.region_dao import RegionDao


region_routes = APIRouter()


@region_routes.get('/region/inventory', response_model=ApiResponse)
async def get_inventory_of_region(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        region_dao = RegionDao(conn.content)
        products = region_dao.get_inventory(current_user.username)
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

# retorna todos los paises registrado en el sistema
@region_routes.get('/region/{country_id}', response_model=ApiResponse)
async def get_regions_for_country(country_id: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        region_dao = RegionDao(conn.content)
        regions = region_dao.get_for_country(country_id)
        if not regions[0]:
            raise Exception(str(regions[1]))
        response.status = status.HTTP_200_OK
        response.data = regions[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response


