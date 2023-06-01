from colorama import init, Fore, Back, Style
from cx_Oracle import connect, DatabaseError
from services.conexion import is_connection_active
from models.api import InternalResponse
from os import getenv

# adminmulven - adminmulven

class ConnectionManager:
    def __init__(self):
        self.connections = {}

    def create_connection(self, user: str, password: str):
        if is_connection_active(self.get_connection(user)):
            print(Back.GREEN + f":::   [RETURN|connection]: {user} :::" + Style.RESET_ALL)
            return InternalResponse(success=True, content=self.connections[user]) 
        else:
            try:
                connection = connect(user=user, password=password, dsn="34.125.35.46:1521/XEPDB1", encoding='UTF-8')  # Actualiza los valores del host y service_name
                self.connections[user] = connection
                print(Back.GREEN + f":::   [ OPEN |connection]: {user}     :::" + Style.RESET_ALL)
                return InternalResponse(success=True, content=connection)
            except DatabaseError as e:
                print(Back.RED +"[ERROR|connection_manager]:", str(e) + Style.RESET_ALL)
                return InternalResponse(success=False, content=str(e))

    def get_connection(self, user: str):
        try:
            conn = self.connections.get(user)
        except Exception as e:
            return InternalResponse(success=False, content=str(e))
        return InternalResponse(success=True, content=conn)

    def remove_connection(self, user: str):
        try:
            if user in self.connections:
                self.connections[user].close()
                del self.connections[user]
            print(Back.RED + f":::   [CLOSE|connection]: {user}      :::" + Style.RESET_ALL)
        except Exception as e:
            return InternalResponse(success=False, content=str(e))
        return InternalResponse(success=True, content=user)

    def get_all_connections(self):
        try:
            conns = self.connections
        except Exception as e:
            return InternalResponse(success=False, content=str(e))
        return InternalResponse(success=True, content=conns)

conn_manager = ConnectionManager()


''' Funcion para comprobar si el usuario esta registrado en la db'''
def try_connect_to_db(username: str, password: str, dsn: str = "34.125.35.46:1521/XEPDB1"):
    try:
        with connect(username, password, dsn) as conn:
            pass
        return {"status" : True, "message": "Conexion exitosa"}
    except DatabaseError as e:
        error, = e.args
        return {"status" : False, "message": error.message}