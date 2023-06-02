from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from models.country import Country
from dao.country_dao import CountryDao


country_routes = APIRouter()

# agrega un pais
@country_routes.post('/country/add', response_model=ApiResponse)
async def create_country(country: Country, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        country_dao = CountryDao(conn.content)
        conn.content.begin()
        res_country = country_dao.create(country)
        if not res_country[0]:
            raise Exception(str(res_country[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# retorna todos los paises registrado en el sistema
@country_routes.get('/country/get', response_model=ApiResponse)
async def get_country_all(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        country_dao = CountryDao(conn.content)
        countrys = country_dao.get_all()
        if not countrys[0]:
            raise Exception(str(countrys[1]))
        response.status = status.HTTP_200_OK
        response.data = countrys[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@country_routes.delete("/country/delete/{id}", response_model=ApiResponse)
def delete_country(id: str, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        conn.content.begin()
        country_dao = CountryDao(conn.content)
        res_country = country_dao.delete(id)
        if not res_country[0]:
            raise Exception(str(res_country[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = res_country[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response


        

