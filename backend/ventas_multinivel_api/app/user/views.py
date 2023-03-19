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
        # Capturar el JWT del encabezado de autorización
        jwt_token = request.headers.get('Authorization', '').split('Bearer ')[1]

        try:
            payload = AccessToken(jwt_token)
        except Exception as e:
            return Response({'error': '%s' % e})

        user = payload['user']
        # username = request.data.get('username')
        # password = request.data.get('password')
        oracle_password = User.objects.filter(username=user).values('oracle_password').get()
        print(oracle_password['oracle_password'])
        
        return Response(oracle_password);
