import cx_Oracle
from models.region import Region

class RegionDao:
    def __init__(self, connection):
        self.nombre = "RegionDao"
        self.connection = connection

    def get_for_country(self, country_id: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT r.K_REGION, r.T_NOMBRE  FROM REGION r WHERE r.K_PAIS = '{country_id}'")
            regions = []
            for row in cursor: 
                K_REGION, T_NOMBRE = row
                regions.append({
                    'id' : K_REGION,
                    'nombre' : T_NOMBRE,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, regions]
    
    def disable (self, region_id: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE REGION SET I_ESTADO = 'I' WHERE K_REGION = {region_id}")
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, region_id]
    
    def activate (self, region_id: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE REGION SET I_ESTADO = 'A' WHERE K_REGION = {region_id}")
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, region_id]