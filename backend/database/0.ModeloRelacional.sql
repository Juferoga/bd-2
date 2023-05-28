/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 13.5 		*/
/*  Created On : 19-may.-2023 7:28:43 a.�m. 				*/
/*  DBMS       : Oracle 						*/
/* ---------------------------------------------------- */

/* Drop Tables */

begin
	EXECUTE IMMEDIATE 'DROP TABLE   BODE_PROD CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   BODEGA CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   CALISERVICIO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   CATEGORIA CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   CLASIFICACION CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   CLIENTE CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   METODOPAGO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   PAGOPEDIDO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   PAIS CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   PEDI_ITEM CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   PEDIDO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   PRODUCTO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   REGION CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   REPRESENTANTE CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

begin
	EXECUTE IMMEDIATE 'DROP TABLE   USUARIO CASCADE CONSTRAINTS';
	EXCEPTION WHEN OTHERS THEN NULL;
end;  
/

/* Create Tables */

CREATE TABLE  BODE_PROD
(
	K_BODEGA NUMBER(6) NOT NULL,
	K_PRODUCTO NUMBER(10) NOT NULL,
	N_CANTIDAD NUMBER(8) NOT NULL
)
;

CREATE TABLE  BODEGA
(
	K_BODEGA NUMBER(6) NOT NULL,
	T_DIRECCION VARCHAR2(50) NOT NULL,
	N_TELEFONO NUMBER(10) NOT NULL,
	T_CIUDAD VARCHAR2(30) NOT NULL,
	I_ESTADO VARCHAR2(1) NOT NULL,
	K_REGION VARCHAR2(3) NOT NULL,
	K_PAIS VARCHAR2(2) NOT NULL
)
;

CREATE TABLE  CALISERVICIO
(
	K_CALISERVICIO NUMBER(10) NOT NULL,
	N_CALIFICACION NUMBER(1) NOT NULL,
	T_OBSERVACION VARCHAR2(300) NULL,
	K_PEDIDO NUMBER(10) NOT NULL
)
;

CREATE TABLE  CATEGORIA
(
	K_CATEGORIA VARCHAR2(3) NOT NULL,
	T_DESCRIPCION VARCHAR2(30) NOT NULL,
	K_SUPERIOR VARCHAR2(3) NULL
)
;

CREATE TABLE  CLASIFICACION
(
	K_CLASIFICACION VARCHAR2(3) NOT NULL,
	T_DESCRIPCION VARCHAR2(15) NOT NULL,
	N_COMISION NUMBER(4,3) NOT NULL
)
;

CREATE TABLE  CLIENTE
(
	K_CLIENTE NUMBER(10) NOT NULL,
	T_CIUDAD VARCHAR2(30) NOT NULL,
	K_REPRESENTANTE NUMBER(10) NOT NULL
)
;

CREATE TABLE  METODOPAGO
(
	K_METPAGO VARCHAR2(2) NOT NULL,
	T_DESCRIPCION VARCHAR2(20) NOT NULL,
	I_ESTADO VARCHAR2(2) NOT NULL
)
;

CREATE TABLE  PAGOPEDIDO
(
	K_PAGOPEDIDO NUMBER(10) NOT NULL,
	N_VALOR NUMBER(10) NOT NULL,
	F_PAGO DATE NOT NULL,
	I_ESTADO VARCHAR2(1) NOT NULL,
	K_PEDIDO NUMBER(10) NOT NULL,
	K_METPAGO VARCHAR2(2) NOT NULL
)
;

CREATE TABLE  PAIS
(
	K_PAIS VARCHAR2(2) NOT NULL,
	T_NOMBRE VARCHAR2(30) NOT NULL
)
;

CREATE TABLE  PEDI_ITEM
(
	K_PEDIDO NUMBER(10) NOT NULL,
	K_PRODUCTO NUMBER(10) NOT NULL,
	N_CANTIDAD NUMBER(3) NOT NULL,
	N_PRECIOU NUMBER(6) NOT NULL
)
;

CREATE TABLE  PEDIDO
(
	K_PEDIDO NUMBER(10) NOT NULL,
	F_CREACION DATE NOT NULL,
	T_DIRECCIONE VARCHAR2(50) NOT NULL,
	N_TOTAL NUMBER(10) NULL,
	I_ESTADO VARCHAR2(1) NOT NULL,
	T_CIUDAD VARCHAR2(30) NOT NULL,
	K_REGION VARCHAR2(3) NOT NULL,
	K_PAIS VARCHAR2(2) NOT NULL,
	K_CLIENTE NUMBER(10) NOT NULL
)
;

CREATE TABLE  PRODUCTO
(
	K_PRODUCTO NUMBER(10) NOT NULL,
	T_NOMBRE VARCHAR2(50) NOT NULL,
	T_DESCRIPCION VARCHAR2(300) NULL,
	N_PRECIO NUMBER(6) NOT NULL,
	I_ESTADO VARCHAR2(1) NOT NULL,
	K_CATEGORIA VARCHAR2(3) NOT NULL
)
;

CREATE TABLE  REGION
(
	K_REGION VARCHAR2(3) NOT NULL,
	K_PAIS VARCHAR2(2) NOT NULL,
	T_NOMBRE VARCHAR2(30) NOT NULL,
	I_ESTADO VARCHAR2(1) NOT NULL
)
;

CREATE TABLE  REPRESENTANTE
(
	K_REPRESENTANTE NUMBER(10) NOT NULL,
	F_CONTRATO DATE NOT NULL,
	K_REGION VARCHAR2(3) NOT NULL,
	K_PAIS VARCHAR2(2) NOT NULL,
	K_CLASIFICACION VARCHAR2(3) NOT NULL,
	K_JEFE NUMBER(10) NULL
)
;

CREATE TABLE  USUARIO
(
	K_USUARIO NUMBER(10) NOT NULL,
	T_NOMBRE VARCHAR2(30) NOT NULL,
	T_APELLIDO VARCHAR2(30) NOT NULL,
	F_NACIMIENTO DATE NOT NULL,
	I_GENERO VARCHAR2(1) NOT NULL,
	N_TELEFONO NUMBER(10) NOT NULL,
	T_DIRECCION VARCHAR2(50) NOT NULL,
	T_EMAIL VARCHAR2(35) NOT NULL,
	I_ESTADO VARCHAR2(1) NOT NULL,
	T_USERNAME VARCHAR(20) NOT NULL UNIQUE
)
;

/* Create Primary Keys, Indexes, Uniques, Checks, Triggers */

ALTER TABLE  BODE_PROD 
 ADD CONSTRAINT PK_BODE_PROD
	PRIMARY KEY (K_BODEGA,K_PRODUCTO) 
 USING INDEX
;

ALTER TABLE  BODE_PROD 
 ADD CONSTRAINT CK_BODE_PROD_CANTIDAD CHECK (N_CANTIDAD >= 0)
;

CREATE INDEX IXFK_BODE_PROD_BODEGA   
 ON  BODE_PROD (K_BODEGA) 
;

CREATE INDEX IXFK_BODE_PROD_PRODUCTO   
 ON  BODE_PROD (K_PRODUCTO) 
;

ALTER TABLE  BODEGA 
 ADD CONSTRAINT PK_BODEGA
	PRIMARY KEY (K_BODEGA) 
 USING INDEX
;

ALTER TABLE  BODEGA 
 ADD CONSTRAINT CK_BODEGA_ESTADO CHECK (I_ESTADO IN ('A', 'I'))
;

CREATE INDEX IXFK_BODEGA_REGION   
 ON  BODEGA (K_REGION,K_PAIS) 
;

ALTER TABLE  CALISERVICIO 
 ADD CONSTRAINT PK_CALISERVICIO
	PRIMARY KEY (K_CALISERVICIO) 
 USING INDEX
;

ALTER TABLE  CALISERVICIO 
 ADD CONSTRAINT CK_CALISERVICIO_CALIFICACION CHECK (N_CALIFICACION >= 0 AND N_CALIFICACION <= 5)
;

CREATE INDEX IXFK_CALISERVICIO_PEDIDO   
 ON  CALISERVICIO (K_PEDIDO) 
;

ALTER TABLE  CATEGORIA 
 ADD CONSTRAINT PK_CATEGORIA
	PRIMARY KEY (K_CATEGORIA) 
 USING INDEX
;

CREATE INDEX IXFK_CATEGORIA_CATEGORIA   
 ON  CATEGORIA (K_SUPERIOR) 
;

ALTER TABLE  CLASIFICACION 
 ADD CONSTRAINT PK_CLASIFICACIO_01
	PRIMARY KEY (K_CLASIFICACION) 
 USING INDEX
;

ALTER TABLE  CLASIFICACION 
 ADD CONSTRAINT CK_CLASIFICACION_N_COMISION CHECK (N_COMISION >= 0 AND N_COMISION <= 1)
;

ALTER TABLE  CLIENTE 
 ADD CONSTRAINT PK_CLIENTE
	PRIMARY KEY (K_CLIENTE) 
 USING INDEX
;

CREATE INDEX IXFK_CLIENTE_REPRESENTANTE   
 ON  CLIENTE (K_REPRESENTANTE) 
;

ALTER TABLE  METODOPAGO 
 ADD CONSTRAINT PK_METODOPAGO
	PRIMARY KEY (K_METPAGO) 
 USING INDEX
;

ALTER TABLE  METODOPAGO 
 ADD CONSTRAINT CK_METODOPAGO_ESTADO CHECK (I_ESTADO IN ('A', 'I'))
;

ALTER TABLE  PAGOPEDIDO 
 ADD CONSTRAINT PK_PAGOPEDIDO
	PRIMARY KEY (K_PAGOPEDIDO) 
 USING INDEX
;

ALTER TABLE  PAGOPEDIDO 
 ADD CONSTRAINT CK_PAGOPEDIDO_ESTADO CHECK (I_ESTADO IN ('A', 'R'))
;

CREATE INDEX IXFK_PAGOPEDIDO_METODOPAGO   
 ON  PAGOPEDIDO (K_METPAGO) 
;

CREATE INDEX IXFK_PAGOPEDIDO_PEDIDO   
 ON  PAGOPEDIDO (K_PEDIDO) 
;

ALTER TABLE  PAIS 
 ADD CONSTRAINT PK_PAIS
	PRIMARY KEY (K_PAIS) 
 USING INDEX
;

ALTER TABLE  PEDI_ITEM 
 ADD CONSTRAINT PK_PEDI_ITEM
	PRIMARY KEY (K_PEDIDO,K_PRODUCTO) 
 USING INDEX
;

ALTER TABLE  PEDI_ITEM 
 ADD CONSTRAINT CK_PEDI_ITEM_CANTIDAD CHECK (N_CANTIDAD > 0)
;

CREATE INDEX IXFK_PEDI_ITEM_PEDIDO   
 ON  PEDI_ITEM (K_PEDIDO) 
;

CREATE INDEX IXFK_PEDI_ITEM_PRODUCTO   
 ON  PEDI_ITEM (K_PRODUCTO) 
;

ALTER TABLE  PEDIDO 
 ADD CONSTRAINT PK_PEDIDO
	PRIMARY KEY (K_PEDIDO) 
 USING INDEX
;

ALTER TABLE  PEDIDO 
 ADD CONSTRAINT CK_PEDIDO_ESTADO CHECK (I_ESTADO IN ('C', 'F', 'E', 'P'))
;

ALTER TABLE  PEDIDO 
 ADD CONSTRAINT CK_PEDIDO_TOTAL CHECK (N_TOTAL >= 0)
;

CREATE INDEX IXFK_PEDIDO_CLIENTE   
 ON  PEDIDO (K_CLIENTE) 
;

CREATE INDEX IXFK_PEDIDO_REGION   
 ON  PEDIDO (K_REGION,K_PAIS) 
;

ALTER TABLE  PRODUCTO 
 ADD CONSTRAINT PK_PRODUCTO
	PRIMARY KEY (K_PRODUCTO) 
 USING INDEX
;

ALTER TABLE  PRODUCTO 
 ADD CONSTRAINT CK_PRODUCTO_ESTADO CHECK (I_ESTADO IN ('A', 'I'))
;

CREATE INDEX IXFK_PRODUCTO_CATEGORIA   
 ON  PRODUCTO (K_CATEGORIA) 
;

ALTER TABLE  REGION 
 ADD CONSTRAINT PK_REGION
	PRIMARY KEY (K_REGION,K_PAIS) 
 USING INDEX
;

ALTER TABLE  REGION 
 ADD CONSTRAINT CK_REGION_ESTADO CHECK (I_ESTADO IN ('A', 'I'))
;

CREATE INDEX IXFK_REGION_PAIS   
 ON  REGION (K_PAIS) 
;

ALTER TABLE  REPRESENTANTE 
 ADD CONSTRAINT PK_REPRESENTANT_01
	PRIMARY KEY (K_REPRESENTANTE) 
 USING INDEX
;

CREATE INDEX IXFK_REPRESENTANTE_CLASIF01   
 ON  REPRESENTANTE (K_CLASIFICACION) 
;

CREATE INDEX IXFK_REPRESENTANTE_REGION   
 ON  REPRESENTANTE (K_REGION,K_PAIS) 
;

CREATE INDEX IXFK_REPRESENTANTE_REPRES01   
 ON  REPRESENTANTE (K_JEFE) 
;

ALTER TABLE  USUARIO 
 ADD CONSTRAINT PK_USUARIO
	PRIMARY KEY (K_USUARIO) 
 USING INDEX
;

ALTER TABLE  USUARIO 
 ADD CONSTRAINT UK_USUARIO_EMAIL UNIQUE (T_EMAIL) 
 USING INDEX
;

ALTER TABLE  USUARIO 
 ADD CONSTRAINT CK_USUARIO_GENERO CHECK (I_GENERO IN ('M', 'F', 'O'))
;

ALTER TABLE  USUARIO 
 ADD CONSTRAINT CK_USUARIO_ESTADO CHECK (I_ESTADO IN ('A', 'I'))
;

/* Create Foreign Key Constraints */

ALTER TABLE  BODE_PROD 
 ADD CONSTRAINT FK_BODE_PROD_BODEGA
	FOREIGN KEY (K_BODEGA) REFERENCES  BODEGA (K_BODEGA)
;

ALTER TABLE  BODE_PROD 
 ADD CONSTRAINT FK_BODE_PROD_PRODUCTO
	FOREIGN KEY (K_PRODUCTO) REFERENCES  PRODUCTO (K_PRODUCTO)
;

ALTER TABLE  BODEGA 
 ADD CONSTRAINT FK_BODEGA_REGION
	FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS)
;

ALTER TABLE  CALISERVICIO 
 ADD CONSTRAINT FK_CALISERVICIO_PEDIDO
	FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO)
;

ALTER TABLE  CATEGORIA 
 ADD CONSTRAINT FK_CATEGORIA_CATEGORIA
	FOREIGN KEY (K_SUPERIOR) REFERENCES  CATEGORIA (K_CATEGORIA)
;

ALTER TABLE  CLIENTE 
 ADD CONSTRAINT FK_CLIENTE_REPRESENTANTE
	FOREIGN KEY (K_REPRESENTANTE) REFERENCES  REPRESENTANTE (K_REPRESENTANTE)
;

ALTER TABLE  CLIENTE 
 ADD CONSTRAINT FK_CLIENTE_USUARIO
	FOREIGN KEY (K_CLIENTE) REFERENCES  USUARIO (K_USUARIO)
;

ALTER TABLE  PAGOPEDIDO 
 ADD CONSTRAINT FK_PAGOPEDIDO_METODOPAGO
	FOREIGN KEY (K_METPAGO) REFERENCES  METODOPAGO (K_METPAGO)
;

ALTER TABLE  PAGOPEDIDO 
 ADD CONSTRAINT FK_PAGOPEDIDO_PEDIDO
	FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO)
;

ALTER TABLE  PEDI_ITEM 
 ADD CONSTRAINT FK_PEDI_ITEM_PEDIDO
	FOREIGN KEY (K_PEDIDO) REFERENCES  PEDIDO (K_PEDIDO)
;

ALTER TABLE  PEDI_ITEM 
 ADD CONSTRAINT FK_PEDI_ITEM_PRODUCTO
	FOREIGN KEY (K_PRODUCTO) REFERENCES  PRODUCTO (K_PRODUCTO)
;

ALTER TABLE  PEDIDO 
 ADD CONSTRAINT FK_PEDIDO_CLIENTE
	FOREIGN KEY (K_CLIENTE) REFERENCES  CLIENTE (K_CLIENTE)
;

ALTER TABLE  PEDIDO 
 ADD CONSTRAINT FK_PEDIDO_REGION
	FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS)
;

ALTER TABLE  PRODUCTO 
 ADD CONSTRAINT FK_PRODUCTO_CATEGORIA
	FOREIGN KEY (K_CATEGORIA) REFERENCES  CATEGORIA (K_CATEGORIA)
;

ALTER TABLE  REGION 
 ADD CONSTRAINT FK_REGION_PAIS
	FOREIGN KEY (K_PAIS) REFERENCES  PAIS (K_PAIS)
;

ALTER TABLE  REPRESENTANTE 
 ADD CONSTRAINT FK_REPRESENTANTE_CLASIFICACION
	FOREIGN KEY (K_CLASIFICACION) REFERENCES  CLASIFICACION (K_CLASIFICACION)
;

ALTER TABLE  REPRESENTANTE 
 ADD CONSTRAINT FK_REPRESENTANTE_REGION
	FOREIGN KEY (K_REGION,K_PAIS) REFERENCES  REGION (K_REGION,K_PAIS)
;

ALTER TABLE  REPRESENTANTE 
 ADD CONSTRAINT FK_REPRESENTANTE_REPRESENTANTE
	FOREIGN KEY (K_JEFE) REFERENCES  REPRESENTANTE (K_REPRESENTANTE)
;

ALTER TABLE  REPRESENTANTE 
 ADD CONSTRAINT FK_REPRESENTANTE_USUARIO
	FOREIGN KEY (K_REPRESENTANTE) REFERENCES  USUARIO (K_USUARIO)
;
