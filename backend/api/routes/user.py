from fastapi import APIRouter, Depends
from models.user import User, UserOfDB, get_current_user
from typing import List
from database.connection_manager import conn_manager
from services.crypto import desencriptar

user_routes = APIRouter()

@user_routes.post('/user/create')
def create(user: User):
    print(user.dict())
    return "success"


@user_routes.post('/user/edit')
def edit(user: User):
    print(user.dict())
    return "success"


@user_routes.get('/user/all')
async def get_users(current_user: UserOfDB = Depends(get_current_user)):
    conn = conn_manager.create_connection(current_user.username, desencriptar(current_user.password))

    # aqui los DAOS, no olvidar cerrar los cursores :)
    conn_manager.get_len_connections()
    # Crear un cursor
    cur = conn.cursor()
    # Ejecutar una consulta
    cur.execute('SELECT * FROM pais')
    # Imprimir los resultados

    countrys = []

    for row in cur:
        K_PAIS, T_NOMBRE = row
        countrys.append({
            'codigo': K_PAIS,
            'nombre': T_NOMBRE,
        })

    # No olvides cerrar la conexión
    cur.close()



    conn_manager.remove_connection(current_user.username)
    
            
    return countrys