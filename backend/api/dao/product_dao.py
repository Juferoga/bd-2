from models.product import Product, FilterRegionCounty, CreateProduct
import cx_Oracle

class ProductDao:
    def __init__(self, connection):
        self.nombre = "UserDao"
        self.connection = connection

    def create_product(self, producto: CreateProduct):
        try:
            cursor = self.connection.cursor()
            sql = f'''INSERT INTO PRODUCTO 
            (K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, N_PRECIO, I_ESTADO, K_CATEGORIA) 
            VALUES (s_producto.nextval, '{producto.nombre}', '{producto.descripcion}', {producto.precio}, '{producto.estado}', '{producto.categoria}')'''
            cursor.execute(sql)
            return [True, 'Producto creado correctamente']
        except cx_Oracle.Error as error:
            return [False, str(error)]

        return products

    def get_all_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM PRODUCTO')
            products = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, N_PRECIO, I_ESTADO, K_CATEGORIA = row
                if I_ESTADO == "A":
                    products.append({
                        'producto' : K_PRODUCTO,
                        'nombre' : T_NOMBRE,
                        'descripcion' : T_DESCRIPCION,
                        'precio' : N_PRECIO,
                        'estado' : I_ESTADO,
                        'categoria' : K_CATEGORIA,
                    })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, products]
    
    def get_filter_products(self, filter: FilterRegionCounty):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                SELECT p.K_PRODUCTO, p.T_NOMBRE, p.T_DESCRIPCION, p.N_PRECIO, p.I_ESTADO, p.K_CATEGORIA FROM PRODUCTO p
                INNER JOIN INVENTARIO i ON p.k_producto = i.k_producto
                INNER JOIN bodega b ON i.k_bodega = b.k_bodega
                WHERE b.k_region = '{filter.region}' AND b.k_pais = '{filter.country}'
            ''')
            products = []
            for row in cursor: 
                K_PRODUCTO, T_NOMBRE, T_DESCRIPCION, N_PRECIO, I_ESTADO, K_CATEGORIA = row
                products.append({
                    'producto' : K_PRODUCTO,
                    'nombre' : T_NOMBRE,
                    'descripcion' : T_DESCRIPCION,
                    'precio' : N_PRECIO,
                    'estado' : I_ESTADO,
                    'categoria' : K_CATEGORIA,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, products]
    
    def disable (self, product_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE PRODUCTO SET I_ESTADO = 'I' WHERE K_PRODUCTO = {product_id}")
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, product_id]
    
    def activate (self, product_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE PRODUCTO SET I_ESTADO = 'A' WHERE K_PRODUCTO = {product_id}")
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, product_id]
    
    


