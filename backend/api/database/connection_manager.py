from cx_Oracle import connect, DatabaseError

class ConnectionManager:
    def __init__(self):
        self.connections = {}

    def create_connection(self, user: str, password: str):
        try:
            connection = connect(user=user, password=password, dsn='localhost:1521/XEPDB1', encoding='UTF-8')  # Actualiza los valores del host y service_name
            self.connections[user] = connection
            return connection
        except DatabaseError:
            return None

    def get_connection(self, user: str):
        return self.connections.get(user)

    def remove_connection(self, user: str):
        if user in self.connections:
            self.connections[user].close()
            del self.connections[user]


''' Funcion para comprobar si el usuario esta registrado en la db'''
def try_connect_to_db(username: str, password: str, dsn: str = "localhost:1521/XEPDB1"):
    try:
        with connect(username, password, dsn) as conn:
            pass
        return {"status" : True, "message": "Conexion exitosa"}
    except DatabaseError as e:
        error, = e.args
        return {"status" : False, "message": error.message}
    