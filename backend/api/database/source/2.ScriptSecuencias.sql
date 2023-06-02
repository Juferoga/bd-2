/* Secuencias */
drop sequence s_bodega;
drop sequence s_producto;
drop sequence s_caliservicio;
drop sequence s_pedido;
drop sequence s_pagopedido;
drop sequence s_pediitem;

create sequence s_bodega increment by 1 start with 1 nocache;
create sequence s_producto increment by 1 start with 1 nocache;
create sequence s_caliservicio increment by 1 start with 1 nocache;
create sequence s_pedido increment by 1 start with 1 nocache;
create sequence s_pagopedido increment by 1 start with 1 nocache;
create sequence s_pediitem increment by 1 start with 1 nocache;