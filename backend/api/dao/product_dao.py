from models.product import Product
import cx_Oracle

class ProductDao:
    def __init__(self, connection):
        self.nombre = "UserDao"
        self.connection = connection
        self.cursor = None

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM PRODUCTO')
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
        return products
    
    def create_product(self, cursor, producto: Product):
        sql = f"INSERT INTO PRODUCTO () VALUES ()"
        try:
            cursor.execute(sql)
            return [True, 'Producto creado correctamente']
        except cx_Oracle.Error as error:
            print("ERROR [create_product | DAO] \n", error)
            return [False, str(error)]

        return products

