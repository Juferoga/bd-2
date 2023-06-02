from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from models.country import Country
from dao.classification_dao import ClassificationDao


classification_routes = APIRouter()

# retorna todos los paises registrado en el sistema
@classification_routes.get('/classification/get', response_model=ApiResponse)
async def get_classifications(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        classification_dao = ClassificationDao(conn.content)
        classifications = classification_dao.get_all()
        if not classifications[0]:
            raise Exception(str(classifications[1]))
        response.status = status.HTTP_200_OK
        response.data = classifications[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response