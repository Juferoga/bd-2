from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .utils.conexiondb import open_connection, close_connection

class UserLogin(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        success, connection = open_connection('DJANGO','nomelase123')
        if success :
            try :
                connection.close()
                data = {"message": "data base connection successfully and closed successfully"}
                return Response(data)
            except Exception as e :
                data = {"message": "Error closing connection"}
                return Response(data)
        else :
            data = {"message": str(connection)}
            return Response(data)
        

    