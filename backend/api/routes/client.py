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
    response = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    if response.success:
        conn = response.content
        cur = conn.cursor()
        user_dao = UserDao(conn)
        client_dao = ClientDao()
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

            resCli = client_dao.create(cur, user, data_current_user.id)
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
    else:
        return ApiResponse(status=status.HTTP_200_OK,data="error",message=response.content)
