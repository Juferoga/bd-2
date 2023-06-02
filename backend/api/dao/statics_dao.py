from models.user import User, UserOfDB
from models.client import UserClient
import cx_Oracle

class StaticsDao:
    def __init__(self, connection):
        self.nombre = "StaticsDao"
        self.connection = connection
        self.cursor = None
    
    def get_statics_best_sellers(self, fecha_inicio: str, fecha_final: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                    SELECT U.T_USERNAME, SUM(PED.N_TOTAL) AS VENTAS_TOTAL
                    FROM USUARIO U
                    JOIN REPRESENTANTE REP ON U.K_USUARIO = REP.K_REPRESENTANTE
                    JOIN CLIENTE C ON REP.K_REPRESENTANTE = C.K_REPRESENTANTE
                    JOIN PEDIDO PED ON C.K_CLIENTE = PED.K_CLIENTE
                    WHERE PED.F_CREACION BETWEEN TO_DATE('{fecha_inicio}', 'YYYY-MM-DD') AND TO_DATE('{fecha_final}', 'YYYY-MM-DD')
                    GROUP BY U.T_USERNAME
                    ORDER BY VENTAS_TOTAL DESC
            ''')
            stats = []
            for row in cursor: 
                T_USERNAME, VENTAS_TOTAL = row
                stats.append({
                    'nombre' : T_USERNAME,
                    'ventas_total' : VENTAS_TOTAL,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, stats]
    
    def get_statics_best_regions(self, fecha_inicio: str, fecha_final: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                    SELECT R.K_REGION, SUM(PED.N_TOTAL) AS VENTAS_TOTAL
                    FROM REGION R
                    JOIN PEDIDO PED ON R.K_REGION = PED.K_REGION AND R.K_PAIS = PED.K_PAIS
                    WHERE PED.F_CREACION BETWEEN TO_DATE('{fecha_inicio}', 'YYYY-MM-DD') AND TO_DATE('{fecha_final}', 'YYYY-MM-DD')
                    GROUP BY R.K_REGION
                    ORDER BY VENTAS_TOTAL DESC
            ''')
            stats = []
            for row in cursor: 
                K_REGION, VENTAS_TOTAL = row
                stats.append({
                    'region'        : K_REGION,
                    'ventas_total'  : VENTAS_TOTAL,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, stats]
    
    def get_statics_best_products(self, fecha_inicio: str, fecha_final: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                    SELECT P.K_PRODUCTO, P.T_NOMBRE, SUM(PI.N_CANTIDAD) AS CANTIDAD_VENDIDA
                    FROM PRODUCTO P
                    JOIN PEDI_ITEM PI ON P.K_PRODUCTO = PI.K_PRODUCTO
                    JOIN PEDIDO PED ON PI.K_PEDIDO = PED.K_PEDIDO
                    WHERE PED.F_CREACION BETWEEN TO_DATE('{fecha_inicio}', 'YYYY-MM-DD') AND TO_DATE('{fecha_final}', 'YYYY-MM-DD')
                    GROUP BY P.K_PRODUCTO, P.T_NOMBRE
                    ORDER BY CANTIDAD_VENDIDA DESC
            ''')
            stats = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, CANTIDAD_VENDIDA = row
                stats.append({
                    'producto'          : K_PRODUCTO, 
                    'nombre_producto'   : T_NOMBRE,
                    'cantidad_vendida'  : CANTIDAD_VENDIDA,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, stats]