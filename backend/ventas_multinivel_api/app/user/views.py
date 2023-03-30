from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.api.utils.conexiondb import open_connection
from app.user.models import User
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.


# /api/user/register
class createUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Captura de request el usuario y contraseña para el nuevo usuario.
        new_username = request.data.get('username')
        new_password = request.data.get('password')
        new_role = request.data.get("role")
        t_nombre = request.data.get("t_nombre")
        t_apellido = request.data.get("t_apellido")
        f_nacimiento = request.data.get("f_nacimiento")
        i_genero = request.data.get("i_genero")
        n_telefono = request.data.get("n_telefono")
        t_direccion = request.data.get("t_direccion")
        t_email = request.data.get("t_email")
        # Representante
        f_contrato = request.data.get("f_contrato")
        ## forenkeyusuario
        k_region = request.data.get("k_region")
        k_pais = request.data.get("k_pais")
        k_clasificacion = request.data.get("k_clasificacion")
        k_jefe = request.data.get("k_jefe")
        # Cliente
        t_cuidad = request.data.get("t_cuidad")
        k_representante = request.data.get("k_representante")
        
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

                k_usuario = 0
                # TODO: Convertir a método
                # Creación de la consulta
                sql = [ 
                        f"create user {new_username} identified by {new_password} default tablespace USERSDEF temporary tablespace USERSTMP quota 1m on USERSDEF",
                        f"grant connect to {new_username}",
                        f"INSERT INTO usuario (t_nombre, t_apellido, f_nacimiento, i_genero, n_telefono, t_direccion, t_email, i_estado) VALUES {t_nombre},{t_apellido},{f_nacimiento},{i_genero},{n_telefono},{t_direccion},{t_email},'A'"
                    ]
                # cursor de la base de datos
                cursor = conn.cursor()
                for i in range(sql.__len__()):
                    cursor.execute(sql[i])
                    db_log += f"SENTENCE {i} : {sql[i]}\n"
                    for row in cursor:
                        db_log += str(row)
                print(f"{db_log}")
                cursor.execute("SELECT last_insert_rowid() FROM usuario")
                k_usuario = cursor.fetchone()[0]


                if (new_role == "cliente"):
                    sql_create_cliente = f"INSERT INTO cliente (t_ciudad,k_usuario,k_representante) VALUES ({t_apellido},{k_usuario},{user})"
                    conn.execute(sql_create_cliente)
                else:
                    sql_create_representante = f"INSERT INTO representante (f_contrato, k_usuario, k_region, k_pais, k_clasificacion, k_jefe) VALUES ({f_contrato}, {k_usuario}, {k_region}, {k_pais}, {k_clasificacion}, {k_jefe})"
                    conn.execute(sql_create_representante)

                conn.close()


                # Crear usuario en django TODO: Crearlo
                new_user = User.objects.create(username=new_username,password=new_password,oracle_password=new_password,role=new_role, k_usuario=k_usuario)
                print(f"{new_user}")
                new_user.save()

                #--------------------------- END CONTENT --------------------------------------------------------
                
                return Response({
                    "status":"success",
                    "data":{
                        "user":f"{new_username}",
                        "password":f"{new_password}",
                        "role":f"{new_role}",
                        "db_log":f"{db_log}"
                    }
                })
            except Exception as e:
                # Error presentado en la ejecución de un query
                return Response({"Error con DB": str(e)})
        else :
            # Cualquier error presentado en la conexión a la BD.
            data = {"Error DB": str(conn)}
            return Response(data)   
        
        
