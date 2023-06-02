from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.jwt import Token
from models.user import authenticate_user, UserOfDB
from os import getenv
from datetime import timedelta
from models.jwt import create_access_token
from services.crypto import encriptar


auth_routes = APIRouter()

@auth_routes.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    password_encrypted = encriptar(form_data.password)
    user = authenticate_user(form_data.username, password_encrypted)
    if not isinstance(user, UserOfDB):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=user, headers={"WWW-Authenticate" : "Bearer"})
    access_token_expires = timedelta(minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(data=
                                        {"username": form_data.username,
                                        "password": encriptar(form_data.password)},
                                        expires_delta=access_token_expires)
    return {"access_token": access_token,
            "token_type": "bearer",
            "username": form_data.username}