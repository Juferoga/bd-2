from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.api.utils.conexiondb import open_connection
from app.user.models import User
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.


# PRODUCTS

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Capturar el JWT del encabezado de autorización
        jwt_token = request.headers.get('Authorization', '').split('Bearer ')[1]
        try:
            payload = AccessToken(jwt_token)
        except Exception as e:
            return Response({'error de Token': '%s' % e})
        user = payload['user']
        user_request = User.objects.filter(username=user).values('oracle_password').get()
        password = user_request['oracle_password']
        

        # Creación de la conexión con la BD
        print(f"usuario:{user} password:{password}")
        success, conn = open_connection(user,password) #Conexión a la base de datos
        if success:
            # SI HAY UN ERROR EN LA EJECUCIÓN DEL QUERY
            try:
                #--------------------------- CONTENT --------------------------------------------------------

                # k_pedido = request.data.get('k_pedido')
                f_creacion = request.data.get('f_creacion')
                n_direccione = request.data.get('n_direccione')
                i_estado = request.data.get('i_estado')
                k_region = request.data.get('k_region')
                k_pais = request.data.get('k_pais')
                k_cliente = request.data.get('k_cliente')
                productos = request.data.get('productos')
                
                # Insertar el registro del pedido en la tabla 'pedido'
                sql_pedido = f"INSERT INTO PEDIDO (f_creacion, n_direccione, i_estado, k_region, k_pais, k_cliente) VALUES ({f_creacion}, {n_direccione}, {i_estado}, {k_pais}, {k_cliente})"
                cursor = conn.cursor()
                cursor.execute(sql_pedido)

                # Recuperar el 'k_pedido' del pedido recién insertado
                cursor.execute("SELECT last_insert_rowid() FROM pedido")
                k_pedido = cursor.fetchone()[0]

                # Insertar registros en la tabla 'producto_pedido' para cada producto del pedido
                for producto in productos:
                    k_producto = producto['k_producto']
                    n_cantidad = producto['n_cantidad']
                    n_preciou = producto['n_preciou']
                    sql_pedi_item = f"INSERT INTO PEDI_ITEM (k_pedido, k_producto, n_cantidad, n_preciou) VALUES ({k_pedido}, {k_producto}, {n_cantidad}, {n_preciou})"
                    cursor.execute(sql_pedi_item)
                conn.commit()
                conn.close()

                return Response({
                    "status":"success",
                    "data":{
                        "k_pedido": f"{k_pedido}",
                    }
                })
            
                #--------------------------- END CONTENT --------------------------------------------------------
                
            except Exception as e:
                # Error presentado en la ejecución de un query
                return Response({"Error con DB": str(e)})
        else :
            # Cualquier error presentado en la conexión a la BD.
            data = {"Error DB": str(conn)}
            return Response(data)   

