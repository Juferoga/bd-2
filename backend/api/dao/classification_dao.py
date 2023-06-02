import cx_Oracle

class ClassificationDao:
    def __init__(self, connection):
        self.nombre = "ClassificationDao"
        self.connection = connection

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT K_CLASIFICACION, T_DESCRIPCION FROM clasificacion')
            classifications = []
            for row in cursor: 
                K_CLASIFICACION, T_DESCRIPCION = row
                classifications.append({
                    'id' : K_CLASIFICACION,
                    'nombre' : T_DESCRIPCION,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, classifications]