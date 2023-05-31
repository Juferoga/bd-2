import cx_Oracle
from models.country import Country

class CountryDao:
    def __init__(self, connection):
        self.nombre = "CountryDao"
        self.connection = connection

    def create(self, country: Country):
        try:
            sql = f"INSERT INTO PAIS (K_PAIS, T_NOMBRE) VALUES ('{country.id}', '{country.nombre}')"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Producto creado correctamente']

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM PAIS')
            countrys = []
            for row in cursor: 
                K_PAIS, T_NOMBRE = row
                countrys.append({
                    'id' : K_PAIS,
                    'nombre' : T_NOMBRE,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, countrys]
    
    def delete(self, country_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM PAIS WHERE K_PAIS = '{country_id}'")
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, country_id]