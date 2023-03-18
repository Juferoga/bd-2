from django.http.response import JsonResponse
from django.views import View
from .utils.conexiondb import open_connection, close_connection

class UserView(View):
    
    def get(self, request):
        success, connection = open_connection('DJANGO','nomelase1234')
        if success :
            try :
                connection.close()
                return JsonResponse({"message": "data base connection successfully and closed successfully"})
            except Exception as e :
                return JsonResponse({"message": "Error closing connection"})
        else :
            return JsonResponse({"message": str(connection)} )
        
    def post(self, request):
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass
    