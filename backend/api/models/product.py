from pydantic import BaseModel, EmailStr
from datetime import date

class Product(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: int
    estado: str
    categoria: str

class FilterRegionCounty(BaseModel):
    region: str
    country: str