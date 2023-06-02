drop tablespace adminmulvendef;
drop tablespace adminmulventmp;

create tablespace adminmulvendef datafile '/opt/oradata/ADMINMULVENDEF.DBF' size 2m autoextend on;
create temporary tablespace adminmulventmp tempfile '/opt/oradata/ADMINMULVENTMP.DBF' size 2m autoextend on;

create tablespace usersmulvendef datafile '/opt/oradata/USERSMULVENDEF.DBF' size 2m autoextend on;
create temporary tablespace usersmulventmp tempfile '/opt/oradata/USERSMULVENTMP.DBF' size 2m autoextend on;

drop user adminmulven cascade;

create user adminmulven identified by adminmulven
default tablespace adminmulvendef
temporary tablespace adminmulventmp quota 2m on adminmulvendef;

-- Revocar privilegios del sistema.
revoke connect from adminmulven;
revoke resource from adminmulven;

-- Revocar gestión de la base de datos.
revoke create role from adminmulven;
revoke create user from adminmulven;
revoke alter user from adminmulven;
revoke drop user from adminmulven;
revoke grant any role from adminmulven;
revoke grant any privilege from adminmulven;
revoke unlimited tablespace from adminmulven;

-- Privilegios del sistema.
grant connect, resource to adminmulven;
grant create public synonym to adminmulven;

-- Gestión de la base de datos.
grant create role to adminmulven;
grant create user to adminmulven;
grant alter user to adminmulven;
grant drop user to adminmulven;
grant grant any role to adminmulven;
grant grant any privilege to adminmulven;
grant unlimited tablespace to adminmulven;

-- Borrar roles
drop role administrador;
drop role cliente;
drop role representante;
drop role director;

-- Rol de administrador.
create role administrador;
grant connect to administrador;
grant create user to administrador;
grant grant any role to administrador;
grant execute any procedure to administrador;
grant execute any type to administrador;
grant select any sequence to administrador;
grant select, insert, update on adminmulven.pais to administrador;
grant select, insert, update on adminmulven.region to administrador;
grant select, insert, update on adminmulven.bodega to administrador;
grant select, insert, update on adminmulven.bode_prod to administrador;
grant select, insert, update on adminmulven.producto to administrador;
grant select, insert, update on adminmulven.categoria to administrador;
grant select, insert, update on adminmulven.metodopago to administrador;
grant select, insert, update on adminmulven.clasificacion to administrador;
grant select, insert, update on adminmulven.usuario to administrador;
grant select, insert on adminmulven.representante to administrador;
grant select on adminmulven.cliente to administrador;
grant select on adminmulven.pedido to administrador;
grant select on adminmulven.pagopedido to administrador;
grant select on adminmulven.pedi_item to administrador;
grant select on adminmulven.caliservicio to administrador;

-- Rol cliente
create role cliente;
grant connect to cliente;
grant execute any procedure to cliente;
grant execute any type to cliente;
grant select any sequence to cliente;
grant select, insert, update, delete on adminmulven.pedi_item to cliente;
grant select, insert, update on adminmulven.caliservicio to cliente;
grant select, insert, update on adminmulven.pagopedido to cliente;
grant select, insert, update on adminmulven.pedido to cliente;
grant select, update on adminmulven.cliente to cliente;
grant select, update on adminmulven.usuario to cliente;
grant select, update(n_cantidad) on adminmulven.bode_prod to cliente;
grant select on adminmulven.pais to cliente;
grant select on adminmulven.region to cliente;
grant select on adminmulven.producto to cliente;
grant select on adminmulven.categoria to cliente;
grant select on adminmulven.metodopago to cliente;
grant select on adminmulven.representante to cliente;

-- Rol representante
create role representante;
grant connect to representante;
grant execute any procedure to representante;
grant execute any type to representante;
grant select any sequence to representante;
grant select, insert, update on adminmulven.pedi_item to representante;
grant select, insert, update on adminmulven.pedido to representante;
grant select, insert, update on adminmulven.usuario to representante;
grant select, insert on adminmulven.cliente to representante;
grant select, update on adminmulven.representante to representante;
grant select on adminmulven.pais to representante;
grant select on adminmulven.region to representante;
grant select on adminmulven.bodega to representante;
grant select on adminmulven.bode_prod to representante;
grant select on adminmulven.producto to cliente;
grant select on adminmulven.categoria to cliente;
grant select on adminmulven.clasificacion to cliente;

-- Rol director
create role director;
grant representante to director;
grant insert on adminmulven.representante to director;

-- Borrar sinónimos
drop public synonym estudiante;
drop public synonym pais;
drop public synonym region;
drop public synonym bodega;
drop public synonym bode_prod;
drop public synonym producto;
drop public synonym categoria;
drop public synonym metodopago;
drop public synonym clasificacion;
drop public synonym usuario;
drop public synonym representante;
drop public synonym cliente;
drop public synonym pedido;
drop public synonym pagopedido;
drop public synonym pedi_item;
drop public synonym caliservicio;

drop public synonym s_bodega;
drop public synonym s_producto;
drop public synonym s_caliservicio;
drop public synonym s_pedido;
drop public synonym s_pagopedido;
drop public synonym s_pediitem;

-- Crear sinónimos
create public synonym estudiante for adminsga.estudiante;
create public synonym pais for adminmulven.pais;
create public synonym region for adminmulven.region;
create public synonym bodega for adminmulven.bodega;
create public synonym inventario for adminmulven.bode_prod;
create public synonym producto for adminmulven.producto;
create public synonym categoria for adminmulven.categoria;
create public synonym metodopago for adminmulven.metodopago;
create public synonym clasificacion for adminmulven.clasificacion;
create public synonym usuario for adminmulven.usuario;
create public synonym representante for adminmulven.representante;
create public synonym cliente for adminmulven.cliente;
create public synonym pedido for adminmulven.pedido;
create public synonym pagopedido for adminmulven.pagopedido;
create public synonym carrito for adminmulven.pedi_item;
create public synonym calificacion for adminmulven.caliservicio;

create public synonym s_bodega for adminmulven.s_bodega;
create public synonym s_producto for adminmulven.s_producto;
create public synonym s_caliservicio for adminmulven.s_caliservicio;
create public synonym s_pedido for adminmulven.s_pedido;
create public synonym s_pagopedido for adminmulven.s_pagopedido;
create public synonym s_pediitem for adminmulven.s_pediitem;