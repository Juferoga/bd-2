from models.representante import Representante
import cx_Oracle

class RepresentanteDao:
    def __init__(self, connection):
        self.nombre = "UserDao"
        self.connection = connection
        self.cursor = None

    def get_all_representantes(self):
        cursor = self.connection.cursor()
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

        return representantes
    
    def create_represent(self, cursor, represent: Representante):
        sql = f"INSERT INTO REPRESENTANTE (K_REPRESENTANTE, F_CONTRATO, K_REGION, K_PAIS, K_CLASIFICACION, K_JEFE) VALUES ({represent.id},to_date({represent.contrato},'YYYY-mm-dd'),'{represent.region}','{represent.pais}', '{represent.clasificacion}', {represent.jefe})"
        try:
            cursor.execute(sql)
            return [True, 'Representante creado correctamente']
        except cx_Oracle.Error as error:
            print("ERROR [create_represent | DAO] \n", error)
            return [False, str(error)]
        

