from pydantic import BaseModel

class PaymentMethod(BaseModel):
    id: str
    descripcion: str
    estado: str

class PaymentOrder(BaseModel):
    id: int
    valor: int
    fecha_pago: str
    estado: str
    id_pedido: int
    id_metpago: str