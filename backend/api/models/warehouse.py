from pydantic import BaseModel

class Warehouse(BaseModel):
    id: int
    direccion: str
    telefono: int
    ciudad: str
    estado: str
    region: str
    pais: str

class WarehouseProduct(BaseModel):
    id: int
    id_warehouse: int
    id_product: int
    cantidad: int