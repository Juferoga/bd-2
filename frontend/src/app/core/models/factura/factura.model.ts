export class A_ITEMSF{
  Q_PRODUCTO : number;
  N_PRODUCTO : string;
  V_UNITARIO : string;
  V_UNITARIOF :string;
  V_TOTAL : string;
}

export class factura{
  N_FACTURA:string;
  T_NCLIENTE:string;
  F_CREACION:string;
  F_PAGO:string;
  I_ESTADOF:string;
  T_DIRECCIONE:string;
  T_REGION:string;
  T_PAIS:string;
  A_ITEMSF: A_ITEMSF[];
  V_SUBTOTAL:string;
  V_IVA:string;
  V_TOTAL:string;
  F_GENERADA:string;
}