from typing import List
from fastapi import APIRouter, Depends, status, Response
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from models.user import UserOfDB, get_current_user
from models.api import ApiResponse
from models.payment import PaymentMethod
from dao.payment_method_dao import PaymentMethodDao


payment_routes = APIRouter()

# agrega un pais
@payment_routes.post('/payment/add', response_model=ApiResponse)
async def create_country(country: PaymentMethod, res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        PaymentMethod = PaymentMethodDao(conn.content)
        conn.content.begin()
        res_country = PaymentMethod.create(country)
        if not res_country[0]:
            raise Exception(str(res_country[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        if conn.success:
            conn.content.rollback()
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# retorna todos los paises registrado en el sistema
@payment_routes.get('/payment/get', response_model=ApiResponse)
async def get_country_all(res: Response = None, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        PaymentMethod = PaymentMethodDao(conn.content)
        payment = PaymentMethod.get_all()
        if not payment[0]:
            raise Exception(str(payment[1]))
        response.status = status.HTTP_200_OK
        response.data = payment[1]
        response.message = "Success"
    except Exception as e:
        res.status_code = status.HTTP_409_CONFLICT
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

        

