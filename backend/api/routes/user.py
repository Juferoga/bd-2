from fastapi import APIRouter, Depends, status, Response
from models.user import User, UserOfDB, get_current_user
from models.api import ApiResponse
from typing import List
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.user_dao import UserDao
from dao.client_dao import ClientDao
from dao.representante_dao import RepresentanteDao


user_routes = APIRouter()

# Devuelve el usuario actual
@user_routes.get('/user/me', response_model=ApiResponse)
async def get_user_me(current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        user_dao = UserDao(conn.content)
        user = user_dao.get_by_username(current_user.username)
        if not user[0]:
            raise Exception(str(user[1]))
        response.status = status.HTTP_200_OK
        response.data = user[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response
# Devuelve todos los usuarios
@user_routes.get('/user/get', response_model=ApiResponse)
async def get_user_all(current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        user_dao = UserDao(conn.content)
        users = user_dao.get_all_users()
        if not users[0]:
            raise Exception(str(users[1]))
        response.status = status.HTTP_200_OK
        response.data = users[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# Modifica un usuario
@user_routes.post('/user/set')
async def edit(user: User, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="",data={},message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(conn.content)
        user_dao = UserDao(conn.content)
        conn.content.begin()
        res = user_dao.edit(user)
        if not res[0]:
            raise Exception(res[1])
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = user_dao.get_by_id(user.id)
        response.message = "Success"
    except Exception as e:
        conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# Elimina un usuario
@user_routes.post('/user/del', response_model=ApiResponse)
async def delete(user: User, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="",data={},message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(conn.content)
        conn.content.begin()
        user_dao = UserDao(conn.content)
        user = user_dao.edit(user)
        if not user[0]:
            raise Exception(user[1])
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = user[1]
        response.message = "Success"
    except Exception as e:
        conn.content.rollback()
        response.status = status.HTTP_400_BAD_REQUEST
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# Devuelve un usuario especifico
@user_routes.get('/user/{username}', response_model=ApiResponse)
async def get_user_me(username:str, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response =  ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(response.content))
        user_dao = UserDao(conn.content)
        user = user_dao.get_by_username(username)
        if not user[0]:
            raise Exception(str(user[1]))
        response.status = status.HTTP_200_OK
        response.data = user[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# Devuelve un usuario especifico
@user_routes.get('/user/id/{id}', response_model=ApiResponse)
async def get_user_for_id(id:int, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response =  ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(response.content))
        user_dao = UserDao(conn.content)
        user = user_dao.get_by_id(id)
        if not user[0]:
            raise Exception(str(user[1]))
        response.status = status.HTTP_200_OK
        response.data = user[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response