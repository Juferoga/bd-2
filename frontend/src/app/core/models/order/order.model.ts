export class Order{
  id: number;
  fecha_creacion: string;
  direccion: string;
  total: number;
  estado: string;
  ciudad: string;
  region: string;
  pais: string;
}

export class OrderItem{
  id_producto: number;
  id_pedido: number;
  cantidad: number;
  precio_unitario: number;
}

export class RateService{
  calificacion: number;
  observacion: string;
  id_pedido: number;
}

