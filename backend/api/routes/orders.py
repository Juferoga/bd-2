from fastapi import APIRouter, Depends, status, Response
from models.user import UserOfDB, get_current_user
from models.order import Order, OrderItem, ServiceRating, DeleteItem
from models.api import ApiResponse
from database.connection_manager import conn_manager
from services.crypto import desencriptar
from dao.order_dao import OrderDao
from dao.user_dao import UserDao
from dao.warehouse_dao import WarehouseDao

order_routes = APIRouter()

# crear pedido
@order_routes.post('/order/add', response_model=ApiResponse)
async def create_order(order: Order, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        user_dao = UserDao(conn.content)
        data_current_user = user_dao.get_by_username(current_user.username)
        if not data_current_user[0]:
            raise Exception(str(data_current_user[1]))
        order_dao = OrderDao(conn.content)
        conn.content.begin()
        order = order_dao.create_order(order, data_current_user[1].id)
        if not order[0]:
            raise Exception(str(order[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# agregar item a pedido
@order_routes.post('/order/add_item', response_model=ApiResponse)
async def create_order_item(order_item: OrderItem, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        warehouse_dao = WarehouseDao(conn.content)
        data_warehouse = warehouse_dao.get_id_warehouse_by_product(order_item.id_producto, order_item.cantidad)
        order_dao = OrderDao(conn.content)
        conn.content.begin()
        order = order_dao.create_order_item(order_item, data_warehouse[1])
        if not order[0]:
            raise Exception(str(order[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# calificar servicio
@order_routes.post('/order/rate_service', response_model=ApiResponse)
async def create_service_rating(service_rating: ServiceRating, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        conn.content.begin()
        order = order_dao.create_service_rating(service_rating)
        if not order[0]:
            raise Exception(str(order[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# obtener todos los pedidos
@order_routes.get('/order/get', response_model=ApiResponse)
async def get_all_orders(current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        orders = order_dao.get_all_orders()
        if not orders[0]:
            raise Exception(str(orders[1]))
        response.status = status.HTTP_200_OK
        response.data = orders[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# obtener items por id de pedido
@order_routes.get('/order/get_items/{id}', response_model=ApiResponse)
async def get_items_by_order_id(id: int, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        orders = order_dao.get_items_by_order_id(id)
        if not orders[0]:
            raise Exception(str(orders[1]))
        response.status = status.HTTP_200_OK
        response.data = orders[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# obtener calificaciones por id de pedido

@order_routes.get('/order/get_ratings/{id}', response_model=ApiResponse)
async def get_ratings_by_order_id(id: int, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        orders = order_dao.get_ratings_by_order_id(id)
        if not orders[0]:
            raise Exception(str(orders[1]))
        response.status = status.HTTP_200_OK
        response.data = orders[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# obtener pedido por id

@order_routes.get('/order/get_order/{id}', response_model=ApiResponse)
async def get_order_by_id(id: int, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        orders = order_dao.get_order_by_id(id)
        if not orders[0]:
            raise Exception(str(orders[1]))
        response.status = status.HTTP_200_OK
        response.data = orders[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# obtener pedidos por id de usuario

@order_routes.get('/order/get_orders_by_user', response_model=ApiResponse)
async def get_orders_by_user(current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")    
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        User_dao = UserDao(conn.content)
        data_current_user = User_dao.get_by_username(current_user.username)
        print(data_current_user[1])
        if not data_current_user[0]:
            raise Exception(str(data_current_user[1]))
        order_dao = OrderDao(conn.content)
        orders = order_dao.get_orders_by_user(data_current_user[1].id)
        if not orders[0]:
            raise Exception(str(orders[1]))
        response.status = status.HTTP_200_OK
        response.data = orders[1]
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response

# eliminar item de pedido
@order_routes.delete('/order/delete_item/', response_model=ApiResponse)
async def delete_items(item: DeleteItem, current_user: UserOfDB = Depends(get_current_user)):
    try:
        response = ApiResponse(status="", data=[], message="")
        conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))
        if not conn.success:
            raise Exception(str(conn.content))
        order_dao = OrderDao(conn.content)
        conn.content.begin()
        order = order_dao.delete_items(item)
        if not order[0]:
            raise Exception(str(order[1]))
        conn.content.commit()
        response.status = status.HTTP_200_OK
        response.data = []
        response.message = "Success"
    except Exception as e:
        response.status = status.HTTP_409_CONFLICT
        response.data = []
        response.message = str(e)
    finally:
        conn_manager.remove_connection(current_user.username)
    return response
