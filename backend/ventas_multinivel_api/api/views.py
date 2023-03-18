from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.conexiondb import open_connection, close_connection
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken


# clase del endpoint /api/login 
class UserLogin(APIView):
    
    # Metodo post de /api/login
    def post(self, request):
        # Obtén las credenciales de la base de datos del cuerpo de la solicitud
        username = request.data.get('username')
        password = request.data.get('password')

        # Se autentica el usuario ante ORACLE.
        success, connection = open_connection(username,password)
        connection.close()
        # Si se realiza la conexion exitosamente el usuario es un usuario de la base de datos.
        if success :
            try :
                # Se autentica el usuario ante DJANGO.
                user = authenticate(username=username, password=password)
                # Se verifica si el usuario esta autenticado
                if(user.is_authenticated):
                    # Se generan los JWT.
                    access_token = AccessToken.for_user(user=user)
                    refresh_token = RefreshToken.for_user(user=user)
                else:
                    # En caso de que no este autenticado envia un mensaje.
                    return Response(
                    {
                        {"message": "user is not authenticate in DJANGO: %s" % username}
                    }, status=200)
                
                
                # Si finalmente todo es correcto, devuelve el JWT access y refresh.
                return Response(
                    {
                        'access': str(access_token),
                        'refresh': str(refresh_token)
                    }, status=200)
            except Exception as e :
                # Si algo sale mal en la autenticacion, generacion de tokens o en la respuesta se captura el error para su interpretacion.
                data = {"message": str(e)}
                return Response(data)
        else :
            # Cualquier error presentado en la conexion a la BD sale de la siguiente linea.
            data = {"message": str(connection)}
            return Response(data)
        

    