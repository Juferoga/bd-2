from fastapi import APIRouter, Depends, status, Response
from models.user import  UserOfDB, get_current_user
from models.client import UserClient
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.user_dao import UserDao
from dao.client_dao import ClientDao

client_routes = APIRouter()

# Crea un cliente
@client_routes.post('/client/create', response_model=ApiResponse)
async def create_client(user: UserClient, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        cur = conn.content.cursor()
        user_dao = UserDao(conn)
        client_dao = ClientDao()
        response = ApiResponse(status="",data={},message="")
        conn.content.begin()
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

        resCli = client_dao.create(cur, user, data_current_user.id)
        if not resCli[0]:
            cur.execute(f"delete from usuario where k_usuario = {user.id}")
            raise Exception(resCli[1])
        conn.content.commit()
        response.message = resUser[1] + " -- " + resCli[1]
        response.status = 200
        response.data = user_dao.get_by_username(user.username)
    except Exception as e:
        conn.content.rollback()
        response.status = status.HTTP_400_BAD_REQUEST
        response.data = []
        response.message = str(e)
    finally:
        cur.close()
        conn_manager.remove_connection(current_user.username)
    return response
    
