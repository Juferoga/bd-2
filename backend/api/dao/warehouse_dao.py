import cx_Oracle
from models.warehouse import WarehouseProduct, WarehouseProductDelete

class WarehouseDao:
    def __init__(self, connection):
        self.nombre = "CountryDao"
        self.connection = connection

    def add(self):
        try:
            sql = f"INSERT INTO PAIS (K_PAIS, T_NOMBRE) VALUES ('{country.id}', '{country.nombre}')"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Producto creado correctamente']

    def add_product(self, data: WarehouseProduct):
        try:
            sql = f"insert into inventario (K_BODEGA, K_PRODUCTO, N_CANTIDAD) values ({data.id_warehouse}, {data.id_product}, {data.cantidad})"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Producto creado correctamente']
    
    def edit_product(self, data: WarehouseProduct):
        try:
            sql = f"UPDATE inventario SET N_CANTIDAD = {data.cantidad} WHERE K_BODEGA = {data.id_warehouse} AND K_PRODUCTO = {data.id_product}"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Producto creado correctamente']
    
    def delete_product(self, data: WarehouseProductDelete):
        try:
            sql = f"DELETE FROM inventario WHERE K_BODEGA = {data.id_warehouse} AND K_PRODUCTO = {data.id_product}"
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except cx_Oracle.Error as error:
            return [False, str(error)]
        finally:
            cursor.close()
        return [True, 'Producto creado correctamente']

    
    def get_all_warehouse(self, username:str, *args, **kwargs):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""SELECT B.*
                              FROM BODEGA B
                              JOIN REGION R ON B.K_REGION = R.K_REGION AND B.K_PAIS = R.K_PAIS
                              JOIN REPRESENTANTE REP ON R.K_REGION = REP.K_REGION AND R.K_PAIS = REP.K_PAIS
                              JOIN USUARIO U ON REP.K_REPRESENTANTE = U.K_USUARIO
                              WHERE U.T_USERNAME = '{username}'
                              """)
            orders = []
            for row in cursor: 
                K_BODEGA, T_DIRECCION, N_TELEFONO, T_CIUDAD, I_ESTADO, K_REGION, K_PAIS = row
                orders.append({
                  'bodega'    :  K_BODEGA,
                  'direccion' :  T_DIRECCION,
                  'telefono'  :  N_TELEFONO,
                  'ciudad'    :  T_CIUDAD,
                  'estado'    :  I_ESTADO,
                  'region'    :  K_REGION,
                  'pais'      :  K_PAIS,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, orders]

    def get_products(self, pais: str, region: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""select p.K_PRODUCTO, p.t_nombre, p.n_precio, sum(bp.n_cantidad) as quantity , p.t_descripcion from bode_prod bp 
                                join producto p on bp.k_producto = p.k_producto 
                                join bodega b on bp.k_bodega = b.k_bodega 
                                join region r on b.k_region = r.k_region 
                                where r.k_region = '{region}' and r.k_pais = '{pais}' 
                                group by p.t_nombre, p.t_descripcion, p.n_precio, p.K_PRODUCTO;
                              """)
            pruducts = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, N_PRECIO, QUANTITY, T_DESCRIPTION = row
                pruducts.append({
                  'id'    :  K_PRODUCTO,
                  'nombre' :  T_NOMBRE,
                  'precio'  :  N_PRECIO,
                  'cantidad'    :  QUANTITY,
                  'descripcion'    :  T_DESCRIPTION,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, pruducts]



    def get_inventory(self, warehouse_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""SELECT P.K_PRODUCTO, P.T_NOMBRE, N_PRECIO, P.T_DESCRIPCION,BP.N_CANTIDAD
                                FROM PRODUCTO P
                                JOIN BODE_PROD BP ON P.K_PRODUCTO = BP.K_PRODUCTO
                                WHERE BP.K_BODEGA = {warehouse_id}
                              """)
            pruducts = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, N_PRECIO, T_DESCRIPTION, N_CANTIDAD = row
                pruducts.append({
                  'id'    :  K_PRODUCTO,
                  'nombre' :  T_NOMBRE,
                  'precio' : N_PRECIO,
                  'descripcion'  :  T_DESCRIPTION,
                  'cantidad'    :  N_CANTIDAD,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, pruducts]

    def get_id_warehouse_by_product(self, product_id: int, quantity: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""select k_bodega from bode_prod where k_producto = {product_id} and n_cantidad >= {quantity}""")
            warehouse = cursor.fetchone()
            id_warehouse = warehouse[0]
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, id_warehouse]
        



    