from models.user import UserClient
import cx_Oracle


class ClientDao:
    def __init__(self, connection):
        self.nombre = "ClientDao"

    def create_client(self, cursor, cliente: UserClient, representante : int):
            sql = f"insert into cliente (K_CLIENTE,T_CIUDAD,K_REPRESENTANTE) values ({cliente.id}, '{cliente.ciudad}', {representante})"
            try:
                cursor.execute(sql)
                return [True, 'Cliente creado correctamente']
            except cx_Oracle.Error as error:
                print("ERROR user_dao.py/create_cliente", error)
                return [False, str(error)]