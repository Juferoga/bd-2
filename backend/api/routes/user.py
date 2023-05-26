from fastapi import APIRouter, Depends
from models.user import User, UserOfDB, get_current_user
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


@user_routes.get('/user/all')
async def get_users(current_user: UserOfDB = Depends(get_current_user)):
    return current_user