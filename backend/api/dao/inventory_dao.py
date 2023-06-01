import cx_Oracle

class InventoryDao:
    def __init__(self, connection):
        self.nombre = "InventoryDao"
        self.connection = connection


    def get_inventory_for_country(self, country: str):
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'''
                    SELECT 
                    PRODUCTO.K_PRODUCTO AS ID,
                    PRODUCTO.T_NOMBRE AS NAME, 
                    PRODUCTO.T_DESCRIPCION AS DESCRIPTION,
                    PRODUCTO.N_PRECIO AS PRICE,
                    SUM(BODE_PROD.N_CANTIDAD) AS QUANTITY,
                    LISTAGG(BODEGA.K_BODEGA, ', ') WITHIN GROUP (ORDER BY BODEGA.K_BODEGA) AS WAREHOUSES,
                    (SELECT LISTAGG(K_REGION, ', ') WITHIN GROUP (ORDER BY K_REGION) FROM 
                        (SELECT DISTINCT K_REGION FROM BODEGA)) AS REGIONS
                    FROM 
                    PRODUCTO 
                    INNER JOIN BODE_PROD ON PRODUCTO.K_PRODUCTO = BODE_PROD.K_PRODUCTO 
                    INNER JOIN BODEGA ON BODE_PROD.K_BODEGA = BODEGA.K_BODEGA 
                    WHERE 
                    BODEGA.K_PAIS = '{country}' 
                    GROUP BY 
                    PRODUCTO.K_PRODUCTO, PRODUCTO.T_NOMBRE, PRODUCTO.T_DESCRIPCION, PRODUCTO.N_PRECIO
                ''')
                products = []
                for row in cursor: 
                    K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, PRECIO, QUANTITY, WAREHOUSES, REGIONS = row
                    products.append({
                        'id' : K_PRODUCTO,
                        'nombre' : T_NOMBRE,
                        'descripcion': T_DESCRIPCION,
                        'precio': PRECIO,
                        'cantidad' : QUANTITY,
                        'bodegas' : WAREHOUSES,
                        'regiones' : REGIONS,
                    })
            except Exception as e:
                return [False, str(e)]
            finally:
                cursor.close()
            return [True, products]
    
    def get_inventory_for_country_region(self, country: str, region: str):
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'''
                    SELECT 
                    PRODUCTO.K_PRODUCTO AS ID,
                    PRODUCTO.T_NOMBRE AS NAME, 
                    PRODUCTO.T_DESCRIPCION AS DESCRIPTION,
                    PRODUCTO.N_PRECIO AS PRICE,           
                    SUM(BODE_PROD.N_CANTIDAD) AS QUANTITY,
                    LISTAGG(BODEGA.K_BODEGA, ', ') WITHIN GROUP (ORDER BY BODEGA.K_BODEGA) AS WAREHOUSES,
                    (SELECT LISTAGG(K_CATEGORIA , ', ') WITHIN GROUP (ORDER BY K_CATEGORIA) FROM 
                        (SELECT DISTINCT K_CATEGORIA FROM PRODUCTO p)) AS CATEGORIES
                    FROM 
                    PRODUCTO 
                    INNER JOIN BODE_PROD ON PRODUCTO.K_PRODUCTO = BODE_PROD.K_PRODUCTO 
                    INNER JOIN BODEGA ON BODE_PROD.K_BODEGA = BODEGA.K_BODEGA 
                    WHERE 
                    BODEGA.K_PAIS = '{country}' AND BODEGA.K_REGION = '{region}'
                    GROUP BY 
                    PRODUCTO.K_PRODUCTO, PRODUCTO.T_NOMBRE, PRODUCTO.T_DESCRIPCION, PRODUCTO.N_PRECIO
                ''')
                products = []
                for row in cursor: 
                    K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, PRECIO, QUANTITY, WAREHOUSES, CATEGORIES = row
                    products.append({
                        'id' : K_PRODUCTO,
                        'nombre' : T_NOMBRE,
                        'descripcion': T_DESCRIPCION,
                        'precio': PRECIO,
                        'cantidad' : QUANTITY,
                        'bodegas' : WAREHOUSES,
                        'regiones' : CATEGORIES,
                    })
            except Exception as e:
                return [False, str(e)]
            finally:
                cursor.close()
            return [True, products]

    def get_inventory_for_country_region_warehouse(self, country: str, region: str, warehouse: int):
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'''
                    SELECT 
                    PRODUCTO.K_PRODUCTO AS ID,
                    PRODUCTO.T_NOMBRE AS NAME,
                    PRODUCTO.T_DESCRIPCION AS DESCRIPTION,
                    PRODUCTO.N_PRECIO AS PRICE, 
                    SUM(BODE_PROD.N_CANTIDAD) AS QUANTITY,
                    LISTAGG(BODEGA.K_BODEGA, ', ') WITHIN GROUP (ORDER BY BODEGA.K_BODEGA) AS WAREHOUSES,
                    (SELECT LISTAGG(K_CATEGORIA , ', ') WITHIN GROUP (ORDER BY K_CATEGORIA) FROM 
                        (SELECT DISTINCT K_CATEGORIA FROM PRODUCTO p)) AS CATEGORIES
                    FROM 
                    PRODUCTO 
                    INNER JOIN BODE_PROD ON PRODUCTO.K_PRODUCTO = BODE_PROD.K_PRODUCTO 
                    INNER JOIN BODEGA ON BODE_PROD.K_BODEGA = BODEGA.K_BODEGA 
                    WHERE 
                    BODEGA.K_PAIS = '{country}' 
                    AND BODEGA.K_REGION = '{region}'
                    AND BODEGA.K_BODEGA = {warehouse}
                    GROUP BY 
                    PRODUCTO.K_PRODUCTO, PRODUCTO.T_NOMBRE, PRODUCTO.T_DESCRIPCION, PRODUCTO.N_PRECIO
                ''')
                products = []
                for row in cursor: 
                    K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, PRECIO, QUANTITY, WAREHOUSES, CATEGORIES = row
                    products.append({
                        'id' : K_PRODUCTO,
                        'nombre' : T_NOMBRE,
                        'descripcion': T_DESCRIPCION,
                        'precio': PRECIO,
                        'cantidad' : QUANTITY,
                        'bodegas' : WAREHOUSES,
                        'categorias' : CATEGORIES,
                    })
            except Exception as e:
                return [False, str(e)]
            finally:
                cursor.close()
            return [True, products]

    