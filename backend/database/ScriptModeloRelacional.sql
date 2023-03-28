CREATE TABLE  BODE_PROD(
	K_BODEGA 		NUMBER(6) 	NOT NULL,
	K_PRODUCTO 		NUMBER(10) 	NOT NULL,
	N_CANTIDAD 		NUMBER(8) 	NOT NULL	CHECK (N_CANTIDAD >= 0),
	B_ESTADO		char(1) 	NOT NULL CHECK (B_ESTADO IN ('0','1')),	
	CONSTRAINT PK_BODE_PROD PRIMARY KEY (K_BODEGA,K_PRODUCTO),
	CONSTRAINT FK_BODE_PROD_BODEGA FOREIGN KEY (K_BODEGA) REFERENCES BODEGA (K_BODEGA),
	CONSTRAINT FK_BODE_PROD_PRODUCTO FOREIGN KEY (K_PRODUCTO) REFERENCES  PRODUCTO (K_PRODUCTO)

)
CREATE INDEX IXFK_BODE_PROD_BODEGA ON  BODE_PROD (K_BODEGA);
CREATE INDEX IXFK_BODE_PROD_PRODUCTO ON  BODE_PROD (K_PRODUCTO);

CREATE TABLE  BODEGA(
	K_BODEGA 		NUMBER(6) NOT NULL,
	T_DIRECCION 	VARCHAR2(50) NOT NULL,
	N_TELEFONO 		NUMBER(10) NOT NULL,
	T_CIUDAD 		VARCHAR2(30) NOT NULL,
	K_REGION 		VARCHAR2(3) NULL,
	K_PAIS 			VARCHAR2(2) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_BODEGA_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT PK_BODEGA PRIMARY KEY(K_BODEGA),
	CONSTRAINT FK_BODEGA_REGION FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS)
) USING INDEX;
CREATE INDEX IXFK_BODEGA_REGION ON  BODEGA (K_REGION,K_PAIS);

CREATE TABLE  CALISERVICIO(
	K_PEDIDO 		NUMBER(10) NOT NULL,
	N_CALIFICACION 	NUMBER(1) NOT NULL,

	CONSTRAINT CK_CALISERVICIO_N_CALIFICACION CHECK (N_CALIFICACION >= 0 AND N_CALIFICACION <= 5),
	CONSTRAINT PK_CALISERVICIO	PRIMARY KEY (K_PEDIDO),
	CONSTRAINT FK_CALISERVICIO_PEDIDO FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO)
)USING INDEX ;
CREATE INDEX IXFK_CALISERVICIO_PEDIDO ON  CALISERVICIO (K_PEDIDO);

CREATE TABLE  CATEGORIA(
	K_CATEGORIA 	VARCHAR2(3) NOT NULL,
	T_DESCRIPCION 	VARCHAR2(30) NOT NULL,
	K_SUPERIOR 		VARCHAR2(3) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_CATEGORIA_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT PK_CATEGORIA PRIMARY KEY (K_CATEGORIA)
	CONSTRAINT FK_CATEGORIA_CATEGORIA FOREIGN KEY (K_SUPERIOR) REFERENCES  CATEGORIA (K_CATEGORIA)
)USING INDEX;
CREATE INDEX IXFK_CATEGORIA_CATEGORIA ON  CATEGORIA (K_SUPERIOR);

CREATE TABLE  CLASIFICACION(
	K_CLASIFICACION 	VARCHAR2(3) NOT NULL,
	T_DESCRIPCION 		VARCHAR2(15) NOT NULL,
	N_COMISION			NUMBER(4,3) NOT NULL,

	CONSTRAINT CK_CLASIFICACION_N_COMISION CHECK (N_COMISION >= 0 AND N_COMISION <= 1),
	CONSTRAINT PK_CLASIFICACIO_01 PRIMARY KEY (K_CLASIFICACION)
)USING INDEX;

CREATE TABLE  CLIENTE(
	K_CLIENTE 		NUMBER(10) NOT NULL,
	T_NOMBRE 		VARCHAR2(30) NOT NULL,
	T_APELLIDO 		VARCHAR2(30) NOT NULL,
	N_TELEFONO 		NUMBER(10) NOT NULL,
	T_DIRECCION 	VARCHAR2(50) NOT NULL,
	T_CIUDAD 		VARCHAR2(30) NOT NULL,
	K_REPRESENTANTE NUMBER(10) NULL,
	K_USUARIO 		NUMBER(10) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_CLIENTE_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT PK_CLIENTE PRIMARY KEY (K_CLIENTE),
	CONSTRAINT FK_CLIENTE_REPRESENTANTE FOREIGN KEY (K_REPRESENTANTE) REFERENCES  REPRESENTANTE (K_REPRESENTANTE),
	CONSTRAINT FK_CLIENTE_USUARIO	FOREIGN KEY (K_USUARIO) REFERENCES  USUARIO (K_USUARIO)
)USING INDEX;
CREATE INDEX IXFK_CLIENTE_REPRESENTANTE ON  CLIENTE (K_REPRESENTANTE);
CREATE INDEX IXFK_CLIENTE_USUARIO ON  CLIENTE (K_USUARIO);

CREATE TABLE  METODOPAGO(
	K_METPAGO 		VARCHAR2(2) NOT NULL,
	T_DESCRIPCION 	VARCHAR2(20) NOT NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_CATEGORIA_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT PK_METODOPAGO	PRIMARY KEY (K_METPAGO) 
)USING INDEX;

CREATE TABLE  PAGOPEDIDO(
	K_PAGOPEDIDO 	NUMBER(10) NOT NULL,
	N_VALOR 		NUMBER(10) NOT NULL,
	I_ESTADO 		VARCHAR2(1) NOT NULL,
	F_PAGO 			DATE NOT NULL,
	K_PEDIDO 		NUMBER(10) NULL,
	K_METPAGO 		VARCHAR2(2) NULL,
	
	CONSTRAINT CK_PAGOPEDIDO_I_ESTADO CHECK (I_ESTADO IN ('A', 'R')),
	CONSTRAINT PK_PAGOPEDIDO	PRIMARY KEY (K_PAGOPEDIDO),
	CONSTRAINT FK_PAGOPEDIDO_METODOPAGO FOREIGN KEY (K_METPAGO) REFERENCES  METODOPAGO (K_METPAGO),
	CONSTRAINT FK_PAGOPEDIDO_PEDIDO	FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO)
)USING INDEX;
CREATE INDEX IXFK_PAGOPEDIDO_METODOPAGO ON  PAGOPEDIDO (K_METPAGO);
CREATE INDEX IXFK_PAGOPEDIDO_PEDIDO ON  PAGOPEDIDO (K_PEDIDO);

CREATE TABLE  PAIS(
	K_PAIS 		VARCHAR2(2) NOT NULL,
	T_NOMBRE 	VARCHAR2(30) NOT NULL,
	CONSTRAINT PK_PAIS	PRIMARY KEY (K_PAIS) 
)USING INDEX;

CREATE TABLE  PEDI_ITEM(
	K_PEDIDO	NUMBER(10) NOT NULL,
	K_PRODUCTO 	NUMBER(10) NOT NULL,
	N_CANTIDAD 	NUMBER(3) NOT NULL,
	N_PRECIOU 	NUMBER(6) NOT NULL,

	CONSTRAINT PK_PEDI_ITEM PRIMARY KEY (K_PEDIDO,K_PRODUCTO),
	CONSTRAINT FK_PEDI_ITEM_PEDIDO	FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO),
	CONSTRAINT FK_PEDI_ITEM_PRODUCTO	FOREIGN KEY (K_PRODUCTO) REFERENCES  PRODUCTO (K_PRODUCTO)
)USING INDEX;
CREATE INDEX IXFK_PEDI_ITEM_PEDIDO ON  PEDI_ITEM (K_PEDIDO);
CREATE INDEX IXFK_PEDI_ITEM_PRODUCTO ON  PEDI_ITEM (K_PRODUCTO);

CREATE TABLE  PEDIDO(
	K_PEDIDO		NUMBER(10) NOT NULL,
	F_CREACION 		DATE NOT NULL,
	I_ESTADO		VARCHAR2(1) NOT NULL,
	N_DIRECCIONE 	VARCHAR2(50) NOT NULL,
	K_REGION		VARCHAR2(3) NULL,
	K_PAIS 			VARCHAR2(2) NULL,
	K_CLIENTE 		NUMBER(10) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_CATEGORIA_B_ESTADO B_ESTADO (ONOFF in ('0','1')),	
	CONSTRAINT CK_PEDIDO_I_ESTADO CHECK (I_ESTADO IN ('C', 'F', 'E', 'P')),
	CONSTRAINT PK_PEDIDO	PRIMARY KEY (K_PEDIDO),
	CONSTRAINT FK_PEDIDO_CLIENTE	FOREIGN KEY (K_CLIENTE) REFERENCES  CLIENTE (K_CLIENTE),
	CONSTRAINT FK_PEDIDO_REGION	FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS)
)USING INDEX;
CREATE INDEX IXFK_PEDIDO_CLIENTE ON  PEDIDO (K_CLIENTE);
CREATE INDEX IXFK_PEDIDO_REGION ON  PEDIDO (K_REGION,K_PAIS);

CREATE TABLE  PRODUCTO(
	K_PRODUCTO 		NUMBER(10) NOT NULL,
	T_NOMBRE		VARCHAR2(30) NOT NULL,
	T_DESCRIPCION	VARCHAR2(100) NOT NULL,
	K_CATEGORIA 	VARCHAR2(3) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_PRODUCTO_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT PK_PRODUCTO	PRIMARY KEY (K_PRODUCTO), 
	CONSTRAINT FK_PRODUCTO_CATEGORIA	FOREIGN KEY (K_CATEGORIA) REFERENCES  CATEGORIA (K_CATEGORIA)
)USING INDEX;
CREATE INDEX IXFK_PRODUCTO_CATEGORIA ON  PRODUCTO (K_CATEGORIA);

CREATE TABLE  REGION(
	K_REGION 	VARCHAR2(3) NOT NULL,
	K_PAIS 		VARCHAR2(2) NOT NULL,
	T_NOMBRE 	VARCHAR2(30) NOT NULL,

	CONSTRAINT PK_REGION	PRIMARY KEY (K_REGION,K_PAIS),
	CONSTRAINT FK_REGION_PAIS	FOREIGN KEY (K_PAIS) REFERENCES  PAIS (K_PAIS)
)USING INDEX;
CREATE INDEX IXFK_REGION_PAIS ON  REGION (K_PAIS);

CREATE TABLE  REPRESENTANTE(
	K_REPRESENTANTE NUMBER(10) NOT NULL,
	T_NOMBRE 		VARCHAR2(30) NOT NULL,
	T_APELLIDO 		VARCHAR2(30) NOT NULL,
	F_NACIMIENTO 	DATE NOT NULL,
	I_GENERO 		VARCHAR2(1) NOT NULL,
	N_TELEFONO 		NUMBER(10) NOT NULL,
	F_CONTRATO 		DATE NOT NULL,
	T_DIRECCION 	VARCHAR2(50) NOT NULL,
	K_REGION 		VARCHAR2(3) NULL,
	K_PAIS 			VARCHAR2(2) NULL,
	K_CLASIFICACION VARCHAR2(3) NULL,
	K_USUARIO 		NUMBER(10) NULL,
	K_JEFE 			NUMBER(10) NULL,
	B_ESTADO		char(1) DEFAULT '1',

	CONSTRAINT CK_REPRESENTANTE_B_ESTADO B_ESTADO (ONOFF in ('0','1')),
	CONSTRAINT CK_REPRESENTANTE_I_GENERO CHECK (I_GENERO IN ('M', 'F', 'O')),
	CONSTRAINT PK_REPRESENTANT_01	PRIMARY KEY (K_REPRESENTANTE),
	CONSTRAINT FK_REPRESENTANTE_CLASIFICACION	FOREIGN KEY (K_CLASIFICACION) REFERENCES  CLASIFICACION (K_CLASIFICACION),
	CONSTRAINT FK_REPRESENTANTE_REGION	FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS),
	CONSTRAINT FK_REPRESENTANTE_REPRESENTANTE	FOREIGN KEY (K_JEFE) REFERENCES  REPRESENTANTE (K_REPRESENTANTE),
	CONSTRAINT FK_REPRESENTANTE_USUARIO	FOREIGN KEY (K_USUARIO) REFERENCES  USUARIO (K_USUARIO)
)USING INDEX;
CREATE INDEX IXFK_REPRESENTANTE_CLASIF01 ON  REPRESENTANTE (K_CLASIFICACION);
CREATE INDEX IXFK_REPRESENTANTE_REGION ON  REPRESENTANTE (K_REGION,K_PAIS);
CREATE INDEX IXFK_REPRESENTANTE_REPRES01 ON  REPRESENTANTE (K_JEFE);
CREATE INDEX IXFK_REPRESENTANTE_USUARIO ON  REPRESENTANTE (K_USUARIO);

CREATE TABLE  USUARIO(
	K_USUARIO 	NUMBER(10) NOT NULL,
	T_USERNAME 	VARCHAR2(30) NOT NULL,
	T_ROL		VARCHAR2(30) NOT NULL,
	T_EMAIL 	VARCHAR2(50) NOT NULL,

	ADD CONSTRAINT UK_USUARIO_EMAIL UNIQUE (T_EMAIL),
	ADD CONSTRAINT UK_USUARIO_USERNAME UNIQUE (T_USERNAME),
	ADD CONSTRAINT PK_USUARIO	PRIMARY KEY (K_USUARIO)
)USING INDEX;

drop sequence s_bodega;
drop sequence s_producto;
drop sequence s_usuario;
drop sequence s_representante;
drop sequence s_cliente;
drop sequence s_pedido;
drop sequence s_pagopedido;

create sequence s_bodega increment by 1 start with 6 nocache;
create sequence s_producto increment by 1 start with 9 nocache;
create sequence s_usuario increment by 1 start with 1 nocache;
create sequence s_representante increment by 1 start with 1 nocache;
create sequence s_cliente increment by 1 start with 1 nocache;
create sequence s_pedido increment by 1 start with 1 nocache;
create sequence s_pagopedido increment by 1 start with 1 nocache;
