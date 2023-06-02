from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from dao.statics_dao import StaticsDao


statics_routes = APIRouter()

# retorna listado de los mejores vendedores
@statics_routes.get('/statics/best/sellers/{fecha_inicio}/{fecha_final}', response_model=ApiResponse)
async def get_statics_all(fecha_inicio:str, fecha_final:str,res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        statics_dao = StaticsDao(conn.content)
        stats = statics_dao.get_statics_best_sellers(fecha_inicio,fecha_final)
        if not stats[0]:
            raise Exception(str(stats[1]))
        response.status = status.HTTP_200_OK
        response.data = stats[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# retorna listado de los mejores regiones
@statics_routes.get('/statics/best/regions/{fecha_inicio}/{fecha_final}', response_model=ApiResponse)
async def get_statics_all(fecha_inicio:str, fecha_final:str,res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        statics_dao = StaticsDao(conn.content)
        stats = statics_dao.get_statics_best_regions(fecha_inicio,fecha_final)
        if not stats[0]:
            raise Exception(str(stats[1]))
        response.status = status.HTTP_200_OK
        response.data = stats[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# retorna listado de los mejores productos
@statics_routes.get('/statics/best/products/{fecha_inicio}/{fecha_final}', response_model=ApiResponse)
async def get_statics_all(fecha_inicio:str, fecha_final:str,res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        statics_dao = StaticsDao(conn.content)
        stats = statics_dao.get_statics_best_products(fecha_inicio,fecha_final)
        if not stats[0]:
            raise Exception(str(stats[1]))
        response.status = status.HTTP_200_OK
        response.data = stats[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response