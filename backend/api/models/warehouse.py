from pydantic import BaseModel

class Warehouse(BaseModel):
    id: int
    direccion: str
    telefono: int
    ciudad: str
    estado: str
    region: str
    pais: str

class WarehouseProductDelete(BaseModel):
    id_warehouse: int
    id_product: int

class WarehouseProduct(BaseModel):
    id_warehouse: int
    id_product: int
    cantidad: int