COMMENT ON TABLE PAIS IS 'Almacena la información de los diversos países en los cuales se encuentra funcionando NatAmE.';

COMMENT ON COLUMN PAIS.K_PAIS IS 'Código del país.';
COMMENT ON COLUMN PAIS.T_NOMBRE IS 'Nombre del país.';


COMMENT ON TABLE REGION IS 'Almacena la información de las diversas regiones de cada país en las cuales hace presencia la empresa.';

COMMENT ON COLUMN REGION.K_REGION IS 'Código de la región.';
COMMENT ON COLUMN REGION.K_PAIS IS 'Código del país en el cual se encuentra la región.';
COMMENT ON COLUMN REGION.T_NOMBRE IS 'Nombre de la región.';
COMMENT ON COLUMN REGION.I_ESTADO IS 'Indica si la bodega se encuentra activo en el sistema o no.';


COMMENT ON TABLE BODEGA IS 'Almacena información sobre las bodegas que pueden haber en cada región.';

COMMENT ON COLUMN BODEGA.K_BODEGA IS 'Código de la bodega.';
COMMENT ON COLUMN BODEGA.T_DIRECCION IS 'Dirección de la bodega.';
COMMENT ON COLUMN BODEGA.N_TELEFONO IS 'Teléfono de contacto de la bodega.';
COMMENT ON COLUMN BODEGA.T_CIUDAD IS 'Ciudad en la que se encuentra la bodega.';
COMMENT ON COLUMN BODEGA.I_ESTADO IS 'Indica si la bodega se encuentra activo en el sistema o no.';
COMMENT ON COLUMN BODEGA.K_REGION IS 'Región en la cual se encuentra la bodega.';
COMMENT ON COLUMN BODEGA.K_PAIS IS 'País al que pertenece la región.';


COMMENT ON TABLE BODE_PROD IS 'Almacena la información sobre los productos que se encuentran en una bodega específica.';

COMMENT ON COLUMN BODE_PROD.K_BODEGA IS 'Código de la bodega.';
COMMENT ON COLUMN BODE_PROD.K_PRODUCTO IS 'Código del producto.';
COMMENT ON COLUMN BODE_PROD.N_CANTIDAD IS 'Cantidad en stock que hay del producto.';


COMMENT ON TABLE PRODUCTO IS 'Almacena la información de los productos que son ofrecidos por la empresa.';

COMMENT ON COLUMN PRODUCTO.K_PRODUCTO IS 'Código del producto.';
COMMENT ON COLUMN PRODUCTO.T_NOMBRE IS 'Nombre del producto.';
COMMENT ON COLUMN PRODUCTO.T_DESCRIPCION IS 'Descripción del producto.';
COMMENT ON COLUMN PRODUCTO.I_ESTADO IS 'Indica si el producto se encuentra activo en el sistema o no.';
COMMENT ON COLUMN PRODUCTO.K_CATEGORIA IS 'Código de la categoría a la que pertenece el producto.';


COMMENT ON TABLE CATEGORIA IS 'Almacena las categorías y subcategorías de los productos ofrecidos.';

COMMENT ON COLUMN CATEGORIA.K_CATEGORIA IS 'Código de la categoría.';
COMMENT ON COLUMN CATEGORIA.T_DESCRIPCION IS 'Descripción de la categoría.';
COMMENT ON COLUMN CATEGORIA.K_SUPERIOR IS 'Código de la categoría superior a la cual pertenece.';


COMMENT ON TABLE PEDI_ITEM IS 'Almacena información sobre la compra de un producto. En otras palabras, es cada item perteneciente a una factura.';

COMMENT ON COLUMN PEDI_ITEM.K_PEDIDO IS 'Código del pedido.';
COMMENT ON COLUMN PEDI_ITEM.K_PRODUCTO IS 'Código del producto.';
COMMENT ON COLUMN PEDI_ITEM.N_CANTIDAD IS 'Cantidad del producto a comprar.';
COMMENT ON COLUMN PEDI_ITEM.N_PRECIOU IS 'Precio unitario establecido por la compra.';


COMMENT ON TABLE PEDIDO IS 'Almacena la información de los pedidos realizados por los clientes.';

COMMENT ON COLUMN PEDIDO.K_PEDIDO IS 'Código del pedido.';
COMMENT ON COLUMN PEDIDO.F_CREACION IS 'Fecha de creación del pedido.';
COMMENT ON COLUMN PEDIDO.N_DIRECCIONE IS 'Dirección en la cual se va a entregar el pedido.';
COMMENT ON COLUMN PEDIDO.I_ESTADO IS 'Estado del pedido. Puede ser Cancelado, Facturado, Entregado o Pendiente.';
COMMENT ON COLUMN PEDIDO.K_REGION IS 'Región en la cual se hizo el pedido.';
COMMENT ON COLUMN PEDIDO.K_PAIS IS 'País en el cual se hizo el pedido.';
COMMENT ON COLUMN PEDIDO.K_CLIENTE IS 'Código del cliente que realizó el pedido.';


COMMENT ON TABLE CALISERVICIO IS 'Almacena la información de las calificaciones que realizan los clientes sobre la atención ofrecida por los representantes en cada pedido.';

COMMENT ON COLUMN CALISERVICIO.K_CALISERVICIO IS 'Consecutivo.';
COMMENT ON COLUMN CALISERVICIO.K_PEDIDO IS 'Código del pedido.';
COMMENT ON COLUMN CALISERVICIO.N_CALIFICACION IS 'Calificación dada por el cliente.';


COMMENT ON TABLE PAGOPEDIDO IS 'Almacena información relacionada a los pagos que ha tenido un pedido.';

COMMENT ON COLUMN PAGOPEDIDO.K_PAGOPEDIDO IS 'Código del pago del pedido.';
COMMENT ON COLUMN PAGOPEDIDO.N_VALOR IS 'Valor total a cancelar.';
COMMENT ON COLUMN PAGOPEDIDO.F_PAGO IS 'Fecha en la que se realizó el pago.';
COMMENT ON COLUMN PAGOPEDIDO.I_ESTADO IS 'Estado del pago. Puede ser Aceptado o Rechazado.';
COMMENT ON COLUMN PAGOPEDIDO.K_PEDIDO IS 'Código del pedido.';
COMMENT ON COLUMN PAGOPEDIDO.K_METPAGO IS 'Código del método de pago.';


COMMENT ON TABLE METODOPAGO IS 'Almacena información sobre los métodos de pago ofrecidos en la empresa.';

COMMENT ON COLUMN METODOPAGO.K_METPAGO IS 'Código del método de pago.';
COMMENT ON COLUMN METODOPAGO.T_DESCRIPCION IS 'Descripción del método de pago.';
COMMENT ON COLUMN METODOPAGO.I_ESTADO IS 'Indica si el método de pago se encuentra activo en el sistema o no.';


COMMENT ON TABLE CLIENTE IS 'Almacena información acerca de los clientes registrados en el sistema.';

COMMENT ON COLUMN CLIENTE.K_CLIENTE IS 'Código del cliente.';
COMMENT ON COLUMN CLIENTE.T_CIUDAD IS 'Ciudad de residencia del cliente.';
COMMENT ON COLUMN CLIENTE.K_USUARIO IS 'Código del usuario registrado.';
COMMENT ON COLUMN CLIENTE.K_REPRESENTANTE IS 'Código del representante que introdujo al cliente.';


COMMENT ON TABLE REPRESENTANTE IS 'Almacena información sobre los representantes de ventas registrados.';

COMMENT ON COLUMN REPRESENTANTE.K_REPRESENTANTE IS 'Código del representante.';
COMMENT ON COLUMN REPRESENTANTE.F_CONTRATO IS 'Fecha en la que el representante firmó contrato.';
COMMENT ON COLUMN REPRESENTANTE.K_USUARIO IS 'Código del usuario registrado.';
COMMENT ON COLUMN REPRESENTANTE.K_REGION IS 'Región a la que pertenece el representante.';
COMMENT ON COLUMN REPRESENTANTE.K_PAIS IS 'País al que pertenece el representante.';
COMMENT ON COLUMN REPRESENTANTE.K_CLASIFICACION IS 'Clasificación en la cual se encuentra el representante.';
COMMENT ON COLUMN REPRESENTANTE.K_JEFE IS 'Código del representante jefe.';


COMMENT ON TABLE CLASIFICACION IS 'Almacena la información relacionada a los tipos de clasificación que puede tener un representante.';

COMMENT ON COLUMN CLASIFICACION.K_CLASIFICACION IS 'Código de la clasificación.';
COMMENT ON COLUMN CLASIFICACION.T_DESCRIPCION IS 'Descripción de la clasificación.';
COMMENT ON COLUMN CLASIFICACION.N_COMISION IS 'Comisión que tiene sobre el total de ventas realizado.';


COMMENT ON TABLE USUARIO IS 'Almacena información relacionada a los usuarios que van a usar el sistema.';

COMMENT ON COLUMN USUARIO.K_USUARIO IS 'Identificador único de cada usuario. Para este caso, se trata de la cédula de ciudadanía.';
COMMENT ON COLUMN USUARIO.T_NOMBRE IS 'Descripción de la clasificación.';
COMMENT ON COLUMN USUARIO.T_APELLIDO IS 'Comisión que tiene sobre el total de ventas realizado.';
COMMENT ON COLUMN USUARIO.F_NACIMIENTO IS 'Fecha de nacimiento del usuario.';
COMMENT ON COLUMN USUARIO.I_GENERO IS 'Género del usuario.';
COMMENT ON COLUMN USUARIO.N_TELEFONO IS 'Teléfono del usuario.';
COMMENT ON COLUMN USUARIO.T_DIRECCION IS 'Dirección de residencia del usuario.';
COMMENT ON COLUMN USUARIO.T_EMAIL IS 'Correo electrónico del usuario.';
COMMENT ON COLUMN USUARIO.I_ESTADO IS 'Indica si el usuario se encuentra activo en el sistema o no.';
