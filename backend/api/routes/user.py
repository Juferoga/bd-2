from fastapi import APIRouter, Depends, status
from models.user import User, UserOfDB, get_current_user
from models.api import ApiResponse
from typing import List
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.user_dao import UserDao

user_routes = APIRouter()

# Devuelve el usuario actual
@user_routes.get('/user/me', response_model=ApiResponse)
async def get_user_me(current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    user = user_dao.get_by_username(current_user.username)
    if not isinstance(user, User):
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=user,message="fail")
    del user_dao
    return ApiResponse(status=status.HTTP_200_OK,data=user,message="success")

# Devuelve todos los usuarios
@user_routes.get('/user/get', response_model=ApiResponse)
async def get_user_all(current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    users = user_dao.get_all_users()
    if not isinstance(users, list) and not all(isinstance(user, User) for user in users):
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=users,message="error")
    del user_dao
    return ApiResponse(status=status.HTTP_200_OK,data=users,message="success")

# Crea un usuario
@user_routes.post('/user/add')
async def create(user: UserOfDB, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    user = user_dao.create(user)
    del user_dao
    return user

# Modifica un usuario
@user_routes.post('/user/set')
async def edit(user: User, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    user = user_dao.edit(user)
    del user_dao
    return user

# Elimina un usuario
@user_routes.post('/user/del')
async def delete(user: User, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    user = user_dao.edit(user)
    del user_dao
    return user

# Devuelve un usuario especifico
@user_routes.get('/user/{username}', response_model=ApiResponse)
async def get_user_me(username:str, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    user_dao = UserDao(conn)
    user = user_dao.get_by_username(username)
    if not isinstance(user, User):
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=user,message="fail")
    del user_dao
    return ApiResponse(status=status.HTTP_200_OK,data=user,message="success")