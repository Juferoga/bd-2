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