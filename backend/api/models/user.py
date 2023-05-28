from fastapi import Depends, HTTPException, status
from database.connection_manager import try_connect_to_db
from services.crypto import desencriptar, encriptar
from pydantic import BaseModel, EmailStr
from datetime import date
from fastapi.security import OAuth2PasswordBearer
from os import getenv
from jose import JWTError, jwt
from models.jwt import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

class User(BaseModel):
    id: int or None = None
    nombre: str or None = None
    apellido: str or None = None
    fecha_de_nacimiento: date or None = None
    genero: str or None = None 
    telefono: str or None = None
    direccion: str or None = None
    email: EmailStr or None = None
    estado: str or None = None

class UserOfDB(User):
    username: str
    password: str

def authenticate_user(username : str, password : str):
    response = try_connect_to_db(username, desencriptar(password))
    
    if response['status']:
        return UserOfDB(username=username, password=password)
    return response['message']

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not valide credentials", headers={"WWW-Authenticate": "Bearer"})   
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
        username: str = payload.get("username")
        password: str = payload.get("password")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError: 
        raise credential_exception
    user = authenticate_user(username,password)
    if not isinstance(user, UserOfDB):
        raise credential_exception
    return user