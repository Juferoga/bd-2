from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.representante import Representante
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.representante_dao import RepresentanteDao
from dao.user_dao import UserDao
from dao.representante_dao import RepresentanteDao

representantes_routes = APIRouter()


# Crear un representate
@representantes_routes.post('/represent/create', response_model=ApiResponse)
async def create_represent(user: Representante, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        conn.content.begin()
        cur = conn.content.cursor()
        user_dao = UserDao(conn)
        represent_dao = RepresentanteDao()
        response = ApiResponse(status="",data={},message="")
        # crear usuario en la base de datos
        cur.execute("create user {} identified by {}".format(user.username, user.password))
        cur.execute("grant connect, representante to {}".format(user.username))
        # usuario modelo
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
        resCli = represent_dao.create(cur, user, data_current_user.id)
        if not resCli[0]:
            cur.execute(f"delete from usuario where k_usuario = {user.id}")
            raise Exception(resCli[1])
        conn.content.commit()
        response.message = "Success"
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
    
# retorna todos los representantes
@representantes_routes.get('/representante/get', response_model=ApiResponse)
async def get_representante_all(current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        representante_dao = RepresentanteDao()
        representantes = representante_dao.get_all_representantes(conn.content.cursor())
        if not representantes[0]:
            raise Exception(str(representantes[1]))
        response.status = status.HTTP_200_OK
        response.data = representantes[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response