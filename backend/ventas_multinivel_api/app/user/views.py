from rest_framework.response import Response
from rest_framework.views import APIView
from app.api.utils.conexiondb import open_connection
from django.contrib.auth.models import User
import jwt
# Create your views here.


# /api/user/register
class createUserView(APIView):

    def post(self, request):
        # Capturar el JWT del encabezado de autorización
        jwt_token = request.headers.get('Authorization', '').split('Bearer ')[1]

        try:
            payload = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
        except jwt.InvalidTokenError:
            return Response({'error': 'Token inválido'})


        user_request = request.data.get('user_request')
        username = request.data.get('username')
        password = request.data.get('password')
        oracle_password = User.objects.filter(username=user_request).values('oracle_password').get()
        return Response({
            "oracle_password": oracle_password
        });
