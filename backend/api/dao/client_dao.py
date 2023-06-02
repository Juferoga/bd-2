from models.client import UserClient
import cx_Oracle


class ClientDao:
    def __init__(self):
        self.nombre = "ClientDao"
        self.connection = connection

    def create(self, cursor, cliente: UserClient, representante : int):
            sql = f"insert into cliente (K_CLIENTE,T_CIUDAD,K_REPRESENTANTE) values ({cliente.id}, '{cliente.ciudad}', {representante})"
            try:
                cursor.execute(sql)
                return [True, 'Cliente creado correctamente']
            except cx_Oracle.Error as error:
                print("ERROR user_dao.py/create_cliente", error)
                return [False, str(error)]
            
    def change_representante(self, cliente_id,representante_id: int):
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"UPDATE CLIENTE SET K_REPRESENTANTE = {representante_id} WHERE K_CLIENTE = {cliente_id}")
            except Exception as e:
                return [False, str(e)]
            finally:
                cursor.close()
            return [True, "Success"]