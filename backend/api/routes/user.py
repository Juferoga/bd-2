from fastapi import APIRouter, Depends, status, Response
from models.user import User, UserOfDB, get_current_user, UserClient
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
    if not isinstance(users, list) and    not all(isinstance(user, User) for user in users):
        del user_dao
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=users,message="error")
    del user_dao
    return ApiResponse(status=status.HTTP_200_OK,data=users,message="success")

# Crea un cliente
@user_routes.post('/user/add/client', response_model=ApiResponse)
async def create_client(user: UserClient, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    cur = conn.cursor()
    user_dao = UserDao(conn)
    response = ApiResponse(status="",data={},message="")
    try:
        cur.execute("create user {} identified by {}".format(user.username, user.password))
        cur.execute("grant connect to {}".format(user.username))
        #usuario modelo
        usuario = UserOfDB(
            id=user.id, 
            nombre=user.nombre, 
            apellido=user.apellido, 
            fecha_de_nacimiento=user.fecha_de_nacimiento, 
            genero=user.genero, 
            telefono=user.telefono, 
            direccion=user.direccion, 
            email=user.email, 
            estado=user.estado,
            username=user.username,
            password=user.password
            )
        resUser = user_dao.create_user(cur, usuario)
        if not resUser[0]:
            raise Exception(resUser[1])
        data_current_user = user_dao.get_by_username(current_user.username)
        resCli = user_dao.create_client(cur, user, data_current_user.id)
        if not resCli[0]:
            cur.execute(f"delete from usuario where k_usuario = {user.id}")
            raise Exception(resCli[1])
        response.message = resUser[1] + " -- " + resCli[1]
        response.status = 200
        response.data = user_dao.get_by_username(user.username)
        conn.commit()
    except Exception as e:
        print("EL ERROR", str(e))
        response.message = str(e)
        response.status = status.HTTP_400_BAD_REQUEST
        if response.message.find("ORA-01031") == -1:
            try:
                cur.execute("drop user {}".format(user.username))
            except Exception as e:
                response.status = status.HTTP_404_NOT_FOUND
                response.message = str(e)
                response.data = {}
                res.status_code = 404
        print(response.message)
    finally:
        cur.close()
        del user_dao
    return response

# Crear un representate
@user_routes.post('/user/add/represent', response_model=ApiResponse)
async def create_represent(user: UserClient, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    cur = conn.cursor()
    user_dao = UserDao(conn)
    response = ApiResponse(status="",data={},message="")
    try:
        cur.execute("create user {} identified by {}".format(user.username, user.password))
        cur.execute("grant connect to {}".format(user.username))
        #usuario modelo
        usuario = UserOfDB(
            id=user.id, 
            nombre=user.nombre, 
            apellido=user.apellido, 
            fecha_de_nacimiento=user.fecha_de_nacimiento, 
            genero=user.genero, 
            telefono=user.telefono, 
            direccion=user.direccion, 
            email=user.email, 
            estado=user.estado,
            username=user.username,
            password=user.password
            )
        resUser = user_dao.create_user(cur, usuario)
        if not resUser[0]:
            raise Exception(resUser[1])
        data_current_user = user_dao.get_by_username(current_user.username)
        resCli = user_dao.create_client(cur, user, data_current_user.id)
        if not resCli[0]:
            cur.execute(f"delete from usuario where k_usuario = {user.id}")
            raise Exception(resCli[1])
        response.message = resUser[1] + " -- " + resCli[1]
        response.status = 200
        response.data = user_dao.get_by_username(user.username)
        conn.commit()
    except Exception as e:
        print("EL ERROR", str(e))
        response.message = str(e)
        response.status = status.HTTP_400_BAD_REQUEST
        if response.message.find("ORA-01031") == -1:
            try:
                cur.execute("drop user {}".format(user.username))
            except Exception as e:
                response.status = status.HTTP_404_NOT_FOUND
                response.message = str(e)
                response.data = {}
                res.status_code = 404
        print(response.message)
    finally:
        cur.close()
        del user_dao
    return response

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