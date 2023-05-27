/* Crear un usuario administrador */
create user albaqueroh identified by mipassword
default tablespace usersmulvendef
temporary tablespace usersmulventmp quota 2m on usersmulvendef;

grant administrador to albaqueroh;

insert into usuario values (
    2018102012, 'Andrés Leonardo', 'Baquero Hernández', to_date('2000-02-17', 'YYYY-mm-dd'),
    'M', 3112401388, 'Calle 40 # 8B - 28', 'albaqueroh@udistrital.edu.co', 'A'
);

connect albaqueroh/mipassword@34.125.158.31:1521/xe;

/* Pais */
insert into pais values ('CO', 'Colombia');

/* Región */
insert into region values ('CAR', 'CO', 'Región Caribe', 'A');
insert into region values ('PAC', 'CO', 'Región Pacífica', 'A');
insert into region values ('AND', 'CO', 'Región Andina', 'A');
insert into region values ('LAO', 'CO', 'Llanos Orientales', 'A');
insert into region values ('AMA', 'CO', 'Amazonía', 'A');

/* Clasificaciones de representantes */
insert into clasificacion values ('BEG', 'Beginner', .1);
insert into clasificacion values ('JUN', 'Junior', .15);
insert into clasificacion values ('SEN', 'Senior', .20);
insert into clasificacion values ('MAS', 'Master', .30);
insert into clasificacion values ('DIR', 'Director', .30);

/* Métodos de pago */
insert into metodopago values ('PE', 'PSE', 'A');
insert into metodopago values ('TC', 'Tarjeta de Crédito', 'A');

/* Bodegas */
insert into bodega values (s_bodega.nextval, 'Calle 13 # 45-87', 1111111, 'Bogotá', 'A', 'AND', 'CO');

/* Categorías de productos */
insert into categoria values ('LIM', 'Limpieza para el hogar.', null);

/* Productos */
insert into producto values (s_producto.nextval, 'Clorox Limpido', 'Clorox de 100mL para desinfectar todo tipo de superficies.', 8500, 'A', 'LIM');
insert into inventario values (s_bodega.currval, s_producto.currval, 50);

insert into producto values (s_producto.nextval, 'Fabuloso Lavanda', 'Fabuloso olor a lavanda de 100mL para desinfectar todo tipo de superficies.', 12000, 'A', 'LIM');
insert into inventario values (s_bodega.currval, s_producto.currval, 50);

insert into producto values (s_producto.nextval, 'Fabuloso Cereza', 'Fabuloso olor a cereza de 500mL para desinfectar todo tipo de superficies.', 18000, 'A', 'LIM');
insert into inventario values (s_bodega.currval, s_producto.currval, 50);

insert into producto values (s_producto.nextval, 'Jabón Líquido Rey', 'Jabón Rey líquido de 500mL.', 6000, 'A', 'LIM');
insert into inventario values (s_bodega.currval, s_producto.currval, 200);

/* Crear un director regional */

-- El usuario debe crearse con el usuario adminmulven.
create user mfpardoh identified by mipassword
default tablespace usersmulvendef
temporary tablespace usersmulventmp quota 2m on usersmulvendef;

grant director to mfpardoh;

-- Las inserciones en tablas ya se pueden hacer con el usuario responsable.
insert into usuario values (2018102002, 'María Fernanda', 'Pardo Hernández', to_date('2003-10-15', 'YYYY-mm-dd'), 'F', 3111111111, 'Calle 40 # 8B - 28', 'mfpardoh@udistrital.edu.co', 'A');
insert into representante values (2018102002, to_date('2023-05-09', 'YYYY-mm-dd'), 'AND', 'CO', 'DIR', null);

connect mfpardoh/mipassword@34.125.158.31:1521/xe;

/* Crear un cliente */
create user savilar identified by mipassword
default tablespace usersmulvendef
temporary tablespace usersmulventmp quota 2m on usersmulvendef;

grant cliente to savilar;

insert into usuario values (2018102003, 'Santiago', 'Ávila Reina', to_date('2000-10-05', 'YYYY-mm-dd'), 'M', 3222222222, 'Calle 127 # 8B - 28', 'savilar@udistrital.edu.co', 'A');
insert into cliente values (2018102003, 'Bogotá', 2018102002);

connect savilar/mipassword@34.125.158.31:1521/xe;

/* Seleccionar ID de cliente según usuario conectado a la BD */
select k_usuario from usuario
    where t_email like ('%' || lower(user) || '%');

/* Crear un pedido */
insert into pedido values (s_pedido.nextval, sysdate, 'Calle 27 Sur # 12-57', 0, 'P', 'AND', 'CO', :k_usuario);