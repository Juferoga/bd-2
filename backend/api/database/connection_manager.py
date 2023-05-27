from cx_Oracle import connect, DatabaseError
from services.conexion import is_connection_active
from os import getenv

class ConnectionManager:
    def __init__(self):
        self.connections = {}

    def create_connection(self, user: str, password: str):
        if is_connection_active(self.get_connection(user)):
            print ("LA CONEXION ESTA ACTIVA, RETORNANDO:", user , " CONEXION;")
            return self.connections[user]
        else:
            try:
                connection = connect(user=user, password=password, dsn="redflox.com:1521/VENTAS_MULTINIVEL", encoding='UTF-8')  # Actualiza los valores del host y service_name
                self.connections[user] = connection
                print("LA CONEXION NO ESTA ACTIVA, CREATE:", user , " CONEXION;")
                return connection
            except DatabaseError as e:
                print("Error al crear la conexión:", str(e))
                return None

    def get_connection(self, user: str):
        return self.connections.get(user)

    def remove_connection(self, user: str):
        if user in self.connections:
            self.connections[user].close()
            del self.connections[user]

    def get_all_connections(self):
        return self.connections
    
    def get_len_connections(self):
        print(self.connections)

conn_manager = ConnectionManager()


''' Funcion para comprobar si el usuario esta registrado en la db'''
def try_connect_to_db(username: str, password: str, dsn: str = "redflox.com:1521/VENTAS_MULTINIVEL"):
    try:
        with connect(username, password, dsn) as conn:
            pass
        return {"status" : True, "message": "Conexion exitosa"}
    except DatabaseError as e:
        error, = e.args
        return {"status" : False, "message": error.message}
    

# class Connect:
#     def __init__(self, user, password):
#         self.user = user
#         self.password = password
#         self.connection = None
#         self.cursor = None
    
#     def open_connection(self):
#         try:
#             self.connection = cx_Oracle.connect(user=self.user, password=self.password, dsn='redflox.com:1521/VENTAS_MULTINIVEL', encoding="UTF-8")
#             self.cursor = self.connection.cursor()
#             return [True,'Conectado']
#         except cx_Oracle.Error as error:
#             return [False, str(error)]
#     def execute_query(self, query, params):
#         try:
#             self.cursor.execute(query, params)
#             if self.cursor.description != None:
#                 return [True, self.cursor.fetchall()]
#             else:
#                 return [True, None]
#         except cx_Oracle.Error as error:
#             print(error)
#             print(query)
#             return [False, str(error)]
#     def commit(self):
#         self.connection.commit()
#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()
#     def get_cursor(self):
#         return self.cursor