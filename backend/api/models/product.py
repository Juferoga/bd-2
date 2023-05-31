from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: int
    estado: str
    categoria: str

class CreateProduct(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    estado: str
    categoria: str

class FilterRegionCounty(BaseModel):
    region: str
    country: str