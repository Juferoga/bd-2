from pydantic import BaseModel

class Order(BaseModel):
    id: int
    fecha_creacion: str
    direccion: str
    total: int
    estado: str
    ciudad: str
    region: str
    pais: str

class OrderItem(BaseModel):
    id_producto: int
    id_pedido: int
    cantidad: int
    precio_unitario: int

class ServiceRating(BaseModel):
    calificacion: int
    observacion: str
    id_pedido: int

class DeleteItem(BaseModel):
    id_pedido: int
    id_producto: int