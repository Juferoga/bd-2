from pydantic import BaseModel, EmailStr
from datetime import date

class AuthUser(BaseModel):
    username: str
    password: str


class User(BaseModel):
    nombre: str
    apellido: str
    fecha_de_nacimiento: date
    genero: str
    telefono: str
    direccion: str
    email: EmailStr
    estado: str