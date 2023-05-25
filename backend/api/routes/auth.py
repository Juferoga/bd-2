from fastapi import APIRouter
from models.user import AuthUser

auth_routes = APIRouter()

@auth_routes.post('/login')
def login(user: AuthUser):
    print(user.dict())
    return "success"

@auth_routes.post('/logout')
def logout():
    return "success"