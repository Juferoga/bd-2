import cx_Oracle
from models.payment import PaymentMethod

class PaymentMethodDao:
    def __init__(self, connection):
        self.nombre = "PaymentMethodDao"
        self.connection = connection

    def create(self, paymentMehotd : PaymentMethod):
        try:
            sql = f"INSERT INTO METODOPAGO (K_METPAGO,T_DESCRIPCION,I_ESTADO) VALUES ('{paymentMehotd.id}', '{paymentMehotd.descripcion}', '{paymentMehotd.estado}')"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Método de pago agregado creado correctamente']

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM METODOPAGO')
            payMeth = []
            for row in cursor: 
                K_METPAGO,T_DESCRIPCION,I_ESTADO = row
                payMeth.append({
                    'nombre' : K_METPAGO,
                    'descripcion' : T_DESCRIPCION,
                    'estado': I_ESTADO
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, payMeth]
