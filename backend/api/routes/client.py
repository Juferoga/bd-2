from fastapi import APIRouter, Depends, status, Response
from models.user import  UserOfDB, get_current_user
from models.client import UserClient
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.user_dao import UserDao
from dao.client_dao import ClientDao
from colorama import init, Fore, Back, Style

client_routes = APIRouter()


# Crea un cliente
@client_routes.post('/client/create', response_model=ApiResponse)
async def create_client(user: UserClient, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        cur = conn.content.cursor()
        user_dao = UserDao(conn.content)
        client_dao = ClientDao(conn.content)
        response = ApiResponse(status="",data={},message="")
        conn.content.begin()
        cur.execute("create user {} identified by {}".format(user.username, user.password))
        cur.execute("grant connect, cliente to {}".format(user.username))  ## REVISAR SI PUEDE ASIGNAR ROLES
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
        if not data_current_user[0]:
            raise Exception(str(data_current_user[1]))
        resCli = client_dao.create(cur, user, data_current_user[1].id)
        if not resCli[0]:
            cur.execute(f"delete from usuario where k_usuario = {user.id}")
            raise Exception(resCli[1])
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = user_dao.get_by_username(user.username)[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        conn.content.rollback()
        response.status = status.HTTP_400_BAD_REQUEST
        response.data = []
        response.message = str(e)

        #PARTE DE ELMINAR USUARIO DE BD
        try:
            if response["message"].find("ORA-01031") == -1:
                cur.execute("drop user {}".format(user.t_nombre))
        except Exception as e:
            print(Back.RED + f":::   [ERROR|client.py]: {str(e)}      :::" + Style.RESET_ALL)
            response.message = str(e)
        # ----------------------------------------------------------------
        
    finally:
        cur.close()
        conn_manager.remove_connection(current_user.username)
    return response

# desactivar producto
@client_routes.post('/client/change_represent', response_model=ApiResponse)
async def change_represent(represent_id: int, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        client_dao = ClientDao(conn.content)
        user_dao = UserDao(conn.content)
        conn.content.begin()
        data_current_user = user_dao.get_by_username(current_user.username)
        if not data_current_user[0]:
            raise Exception(str(data_current_user[1]))
        client = client_dao.change_representante(data_current_user.id, represent_id)
        if not client[0]:
            raise Exception(str(client[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = client[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response
    
