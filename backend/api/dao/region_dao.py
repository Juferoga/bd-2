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
    
    def get_inventory(self, username: str):
        try:
            sql = f"""SELECT P.K_PRODUCTO, P.T_NOMBRE, P.T_DESCRIPCION, SUM(BP.N_CANTIDAD) AS TOTAL_CANTIDAD,
                                LISTAGG(B.K_BODEGA, ', ') WITHIN GROUP (ORDER BY B.K_BODEGA) AS BODEGAS
                                FROM USUARIO U
                                JOIN REPRESENTANTE R ON U.K_USUARIO = R.K_REPRESENTANTE 
                                JOIN REGION RG ON R.K_REGION = RG.K_REGION
                                JOIN BODEGA B ON RG.K_REGION = B.K_REGION
                                JOIN BODE_PROD BP ON B.K_BODEGA = BP.K_BODEGA
                                JOIN PRODUCTO P ON BP.K_PRODUCTO = P.K_PRODUCTO
                                WHERE U.T_USERNAME = '{username}'
                                GROUP BY P.K_PRODUCTO, P.T_NOMBRE, P.T_DESCRIPCION
                              """
            cursor = self.connection.cursor()
            cursor.execute(sql)
            pruducts = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, TOTAL_CANTIDAD, BODEGAS = row
                pruducts.append({
                  'id'    :  K_PRODUCTO,
                  'nombre' :  T_NOMBRE,
                  'descripcion'  :  T_DESCRIPCION,
                  'cantidad'    :  TOTAL_CANTIDAD,
                  'bodegas' : BODEGAS,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, pruducts]
        