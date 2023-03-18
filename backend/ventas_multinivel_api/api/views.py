from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.conexiondb import open_connection, close_connection
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken



class UserLogin(APIView):
    
    def post(self, request):
        # Obtén las credenciales de la base de datos del cuerpo de la solicitud
        username = request.data.get('username')
        password = request.data.get('password')

        success, connection = open_connection(username,password)
        if success :
            try :
                user = authenticate(username=username, password=password)
                access_token = AccessToken.for_user(user=user)
                refresh_token = RefreshToken.for_user(user=user)

                connection.close()
                return Response(
                    {
                        'access': str(access_token),
                        'refresh': str(refresh_token)
                    }, status=200)
            except Exception as e :
                data = {"message": str(e)}
                return Response(data)
        else :
            data = {"message": str(connection)}
            return Response(data)
        

    