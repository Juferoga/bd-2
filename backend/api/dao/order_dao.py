from models.order import Order, OrderItem, ServiceRating
import cx_Oracle

class OrderDao:
    def __init__(self, connection):
        self.connection = connection

    #Crear el carrito "pedido"
    def create_order(self, order: Order):
        try:
            cursor = self.connection.cursor()
            sql = f'''
            INSERT INTO PEDIDO 
            (K_PEDIDO, F_CREACION, T_DIRECCION, N_TOTAL, I_ESTADO, T_CIUDAD, K_REGION, K_PAIS, K_CLIENTE) 
            VALUES (s_pedido.nextval, TO_DATE('{order.fecha_creacion}', 'YYYY/MM/DD'), '{order.direccion}', {order.total}, '{order.estado}', '{order.ciudad}', '{order.region}', '{order.pais}', {order.id_cliente})'''
            cursor.execute(sql)
            return [True, 'Pedido creado correctamente']
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()

    # Añadir items al carrito
    def create_order_item(self, order_item: OrderItem):
        try:
            cursor = self.connection.cursor()
            sql = f'''
            INSERT INTO pedi_item
            (k_bodega, K_PRODUCTO, K_PEDIDO, N_CANTIDAD, N_PRECIOU) 
            VALUES (s_pediitem.nextval, {order_item.id_producto}, {order_item.id_pedido}, {order_item.cantidad}, {order_item.precio_unitario})'''
            cursor.execute(sql)
            return [True, 'Item añadido al pedido']
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()

    # Calificar el pedido
    def create_service_rating(self, service_rating: ServiceRating):
        try:
            cursor = self.connection.cursor()
            sql = f'''
            INSERT INTO CALISERVICIO 
            (K_CALIFICACION_SERVICIO, N_CALIFICACION, T_OBSERVACION, K_PEDIDO) 
            VALUES (s_caliservicio.nextval, {service_rating.calificacion}, '{service_rating.observacion}', {service_rating.id_pedido})'''
            cursor.execute(sql)
            return [True, 'Calificación de servicio creada correctamente']
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()

    # Retorna todos los pedidos
    def get_all_orders(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM PEDIDO')
            orders = []
            for row in cursor: 
                K_PEDIDO, F_FECHA_CREACION, T_DIRECCION, N_TOTAL, I_ESTADO, T_CIUDAD, K_REGION, K_PAIS, K_CLIENTE = row
                orders.append({
                    'pedido' : K_PEDIDO,
                    'fecha_creacion' : F_FECHA_CREACION,
                    'direccion' : T_DIRECCION,
                    'total' : N_TOTAL,
                    'estado' : I_ESTADO,
                    'ciudad' : T_CIUDAD,
                    'region' : K_REGION,
                    'pais' : K_PAIS,
                    'id_cliente' : K_CLIENTE,
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, orders]
    
    # devuelve los items de cada carrito
    def get_items_by_order_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""select p.t_nombre, pi.n_cantidad, pi.n_preciou 
            from pedi_item pi inner join producto p on pi.k_producto = p.k_producto 
            where pi.k_pedido = {id}""")
            order_items = []
            for row in cursor:
                t_nombre, n_cantidad, n_preciou = row
                order_items.append({
                    'nombre' : t_nombre,
                    'cantidad' : n_cantidad,
                    'precio_unitario' : n_preciou
                })
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, order_items]

    def get_order_by_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'SELECT * FROM PEDIDO WHERE K_PEDIDO = {id}')
            row = cursor.fetchone()
            K_PEDIDO, F_CREACION, T_DIRECCION, N_TOTAL, I_ESTADO, T_CIUDAD, K_REGION, K_PAIS, K_CLIENTE = row
            order = {
                'pedido' : K_PEDIDO,
                'fecha_creacion' : F_CREACION,
                'direccion' : T_DIRECCION,
                'total' : N_TOTAL,
                'estado' : I_ESTADO,
                'ciudad' : T_CIUDAD,
                'region' : K_REGION,
                'pais' : K_PAIS,
                'id_cliente' : K_CLIENTE,
            }
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, order]