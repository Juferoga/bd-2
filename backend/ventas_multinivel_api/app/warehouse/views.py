from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.api.utils.conexiondb import open_connection
from app.user.models import User
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.


# PRODUCTS

class AllProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

                # Creación de la consulta
                sql = "SELECT * FROM producto"
                # cursor de la base de datos
                cursor = conn.cursor()
                cursor.execute(sql)
                # Recorrer los resultados de la consulta y almacenarlos en una lista
                productos = []
                for row in cursor:
                    if row[0] not in productos:
                        productos[row[0]] = {
                            "k_producto": row[0],
                            "t_nombre": row[1],
                            "t_descripcion": row[2],
                            "i_estado": row[3],
                            "categorias": []
                        }
                    # Agregar la categoría a la lista correspondiente
                    categoria = {
                        "k_categoria": row[4],
                        "t_nombre": row[6],
                        "t_descripcion": row[7],
                        "i_estado": row[8]
                    }
                    productos[row[0]]["categorias"].append(categoria)

                cursor.close()
                conn.close()

                return Response({
                    "status":"success",
                    "data":{
                        "productos": productos
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

class SaveProductView(APIView):
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

                k_producto = request.data.get('k_producto')
                t_nombre = request.data.get('t_nombre')
                t_description = request.data.get('t_description')
                i_estado = request.data.get('i_estado')
                k_categoria = request.data.get('k_categoria')
                
                # TODO: Convertir a método
                # Creación de la consulta
                sql = [ 
                        f"INSERT INTO PRODUCTO (k_producto, t_nombre, t_description, i_estado, k_categoria) VALUES ({k_producto}, {t_nombre}, {t_description}, {i_estado}, {k_categoria})"
                    ]
                # cursor de la base de datos
                cursor = conn.cursor()
                for i in range(sql.__len__()):
                    cursor.execute(sql[i])
                    db_log += f"SENTENCE {i} : {sql[i]}\n"
                    for row in cursor:
                        db_log += str(row)
                print(f"{db_log}")
                conn.close()
                return Response({
                    "status":"success",
                    "data":{
                        "k_producto":f"{k_producto}",
                        "t_nombre":f"{t_nombre}",
                        "t_description":f"{t_description}",
                        "i_estado": f"{i_estado}",
                        "k_categoria": f"{k_categoria}",
                        "db_log":f"{db_log}"
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

# CATEGORYS

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

                # Creación de la consulta
                sql = "SELECT * FROM categoria"
                # cursor de la base de datos
                cursor = conn.cursor()
                cursor.execute(sql)
                # Recorrer los resultados de la consulta y almacenarlos en una lista
                categorias = []
                for row in cursor:
                    categoria = {
                        "k_categoria": row[0],
                        "t_nombre": row[1],
                        "t_descripcion": row[2]
                    }
                    categorias.append(categoria)
                conn.close()

                return Response({
                    "status":"success",
                    "data":{
                        "categorias": categorias
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