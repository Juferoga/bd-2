from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from datetime import timedelta, datetime
from jose import JWTError, jwt
from os import getenv

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode,getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))
    return encode_jwt


