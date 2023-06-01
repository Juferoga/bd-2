from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from models.warehouse import WarehouseProduct, WarehouseProductDelete
from dao.warehouse_dao import WarehouseDao


warehouse_routes = APIRouter()


@warehouse_routes.get('/warehouse/get', response_model=ApiResponse)
async def get_ware_houses(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        ware_house_dao = WarehouseDao(conn.content)
        ware_houses = ware_house_dao.get_all_warehouse(current_user.username)
        if not ware_houses[0]:
            raise Exception(str(ware_houses[1]))
        response.status = status.HTTP_200_OK
        response.data = ware_houses[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@warehouse_routes.post('/warehouse/add_product', response_model=ApiResponse)
async def add_product(wa_ho: WarehouseProduct, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        conn.content.begin()
        ware_house_dao = WarehouseDao(conn.content)
        ware_houses = ware_house_dao.add_product(wa_ho)
        if not ware_houses[0]:
            raise Exception(str(ware_houses[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = ware_houses[1]
        response.message = "Success"
    except Exception as e:
        conn.content.rollback()
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@warehouse_routes.post('/warehouse/edit_product', response_model=ApiResponse)
async def edit_product(wa_ho: WarehouseProduct, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        conn.content.begin()
        ware_house_dao = WarehouseDao(conn.content)
        ware_houses = ware_house_dao.edit_product(wa_ho)
        if not ware_houses[0]:
            raise Exception(str(ware_houses[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = ware_houses[1]
        response.message = "Success"
    except Exception as e:
        conn.content.rollback()
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@warehouse_routes.delete('/warehouse/delete_product', response_model=ApiResponse)
async def delete_product(wa_ho: WarehouseProductDelete, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        conn.content.begin()
        ware_house_dao = WarehouseDao(conn.content)
        ware_houses = ware_house_dao.delete_product(wa_ho)
        if not ware_houses[0]:
            raise Exception(str(ware_houses[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = ware_houses[1]
        response.message = "Success"
    except Exception as e:
        conn.content.rollback()
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@warehouse_routes.get('/warehouse/{id}/inventory', response_model=ApiResponse)
async def get_inventory(id:int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        ware_house_dao = WarehouseDao(conn.content)
        products = ware_house_dao.get_inventory(id)
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

@warehouse_routes.get('/warehouse/inventory/', response_model=ApiResponse)
async def get_inventory(country: str, region: str, warehouse: int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        ware_house_dao = WarehouseDao(conn.content)
        products = ware_house_dao.get_inventory(id)
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


