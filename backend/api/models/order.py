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
    id_cliente: int

class OrderItem(BaseModel):
    id: int
    id_pedido: int
    id_producto: int
    cantidad: int
    precio_unitario: int

class ServiceRating(BaseModel):
    id: int
    calificacion: int
    observacion: str
    id_pedido: int