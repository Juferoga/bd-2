from fastapi import APIRouter
from routes.models.auth import AuthModel

auth_routes = APIRouter()

@auth_routes.post('/login')
def login(user: AuthModel):
    print(user.dict())
    return "success"