from fastapi import APIRouter, Depends, status, Response
from models.user import User, UserOfDB, get_current_user
from models.representante import Representante
from typing import List
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.representante_dao import RepresentanteDao

representantes_routes = APIRouter()

@representantes_routes.get('/representante/get', response_model=ApiResponse)
async def get_representante_all(current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
    representante_dao = RepresentanteDao(conn)
    representantes = representante_dao.get_all_representantes()
    if not isinstance(representantes, list) and not all(isinstance(representante, Representante) for representante in representantes):
        del representante_dao
        return ApiResponse(status=status.HTTP_404_NOT_FOUND,data=representantes,message="error")
    del representante_dao
    return ApiResponse(status=status.HTTP_200_OK,data=representantes,message="success")

