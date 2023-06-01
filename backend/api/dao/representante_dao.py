from models.representante import Representante
import cx_Oracle

class RepresentanteDao:
    def __init__(self):
        self.nombre = "UserDao"

    def get_all_representantes(self, cursor):
        try:
            cursor.execute('SELECT * FROM REPRESENTANTE')
            representantes = []
            for row in cursor: 
                K_REPRESENTANTE, F_CONTRATO, K_REGION, K_PAIS, K_CLASIFICACION, K_JEFE = row
                representantes.append({
                    'representante' : K_REPRESENTANTE,
                    'contrato' : F_CONTRATO,
                    'region' : K_REGION,
                    'pais' : K_PAIS,
                    'clasificacion' : K_CLASIFICACION,
                    'jefe' : K_JEFE
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, representantes]
    
    def create(self, cursor, represent: Representante, current_user_id):
        sql = f"INSERT INTO REPRESENTANTE (K_REPRESENTANTE, F_CONTRATO, K_REGION, K_PAIS, K_CLASIFICACION, K_JEFE) VALUES ({represent.id},to_date('{str(represent.contrato)}','YYYY-mm-dd'),'{represent.region}','{represent.pais}', '{represent.clasificacion}', {current_user_id})"
        try:
            cursor.execute(sql)
            return [True, 'Representante creado correctamente']
        except cx_Oracle.Error as error:
            print("ERROR [create_represent | DAO] \n", error)
            return [False, str(error)]
        
    def get_commision(self, username:str, *args, **kwargs):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                            SELECT 
                                U.T_NOMBRE AS NOMBRE_USUARIO, 
                                C.N_COMISION AS COMISION
                            FROM 
                                USUARIO U
                                INNER JOIN REPRESENTANTE R ON U.K_USUARIO = R.K_REPRESENTANTE
                                INNER JOIN CLASIFICACION C ON R.K_CLASIFICACION = C.K_CLASIFICACION
                            WHERE U.T_USERNAME = '{username}'
                            """)
            orders = []
            for row in cursor: 
                NOMBRE_USUARIO, COMISION= row
                orders.append({
                    'usuario'     :  NOMBRE_USUARIO,
                    'comision'    :  COMISION
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, orders]
        

