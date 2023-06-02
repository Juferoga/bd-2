from pydantic import BaseModel, EmailStr
from datetime import date
from .user import UserOfDB

class Representante(UserOfDB):
    contrato : date
    region : str
    pais : str
    clasificacion : str