from fastapi import APIRouter
from models.user import User
from typing import List

user_routes = APIRouter()

@user_routes.post('/user/create')
def create(user: User):
    print(user.dict())
    return "success"


@user_routes.post('/user/edit')
def edit(user: User):
    print(user.dict())
    return "success"


@user_routes.get('/user/all', response_model=List[User])
def get_users():
    return "success"