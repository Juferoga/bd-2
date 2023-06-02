from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.class_sellers_dao import ClassSellers

class_sellers_route = APIRouter()

@class_sellers_route.get("/classSellers/top_sellers", response_model=ApiResponse)
async def topSellers(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        qualification_dao = ClassSellers(conn.content)
        top = qualification_dao.topSellers()
        if not top[0]:
            raise Exception(str(top[1]))
        response.status = status.HTTP_200_OK
        response.data = top[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

@class_sellers_route.get("/classSellers/monthlySells", response_model=ApiResponse)
async def monthlySells(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        qualification_dao = ClassSellers(conn.content)
        top = qualification_dao.monthlySells()
        if not top[0]:
            raise Exception(str(top[1]))
        response.status = status.HTTP_200_OK
        response.data = top[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response
