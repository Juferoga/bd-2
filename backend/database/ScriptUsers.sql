-- ::: Creación y llenado automatico de la BD ::: ---
-- ! VERIFICAR EN ESTE ARCHIVO LA RUTA DE ACCESO
start /home/juferoga/repos/ud/bd-2/backend/database/scriptModeloRelacional.sql;
start /home/juferoga/repos/ud/bd-2/backend/database/scriptLlenado.sql;

-- ::: Crear tablespace default ::: ---
create tablespace ADMDEF datafile '/opt/oracle/oradata/XE/ADMDEF.DBF' size 512m autoextend on;
--- ::: Crear tablespace temporal ::: ---
create temporary tablespace ADMTMP tempfile '/opt/oracle/oradata/XE/ADMTMP.DBF' size 512m autoextend on;

create tablespace USERSDEF datafile '/opt/oracle/oradata/XE/USERSDEF.DBF' size 512m autoextend on;

create temporary tablespace USERSTMP tempfile '/opt/oracle/oradata/XE/USERSTMP.DBF' size 512m autoextend on;

--- 1er rol ADMINDB user
create user ADMINDB identified by nomelase123 default tablespace ADMDEF temporary tablespace ADMTMP quota 512m on ADMDEF;
grant connect,resource to ADMINDB;
--- 2nd rol USERLOGIN user
create user USERLOGIN identified by nomelase123 default tablespace USERSDEF temporary tablespace USERSTMP quota 1m on USERSDEF;
grant connect to USERLOGIN;

CREATE TABLESPACE DJADEF DATAFILE '/opt/oracle/oradata/XE/DJADEF.DBF' SIZE 1G AUTOEXTEND ON;
CREATE TEMPORARY TABLESPACE DJATMP TEMPFILE '/opt/oracle/oradata/XE/DJATMP.DBF' SIZE 1G AUTOEXTEND ON;
CREATE USER DJANGO IDENTIFIED BY nomelase123 DEFAULT TABLESPACE DJADEF TEMPORARY TABLESPACE DJATMP QUOTA UNLIMITED ON DJADEF;
grant connect, resource TO DJANGO;

-- Permisos para el Rol ADMINISTRADOR
create role ADMINISTRADOR;
grant SELECT,INSERT,UPDATE on ADMINDB.BODE_PROD to ADMINISTRADOR;
grant SELECT,INSERT,UPDATE on ADMINDB.BODEGA to ADMINISTRADOR;
-- TODO: (DELETES) VERIFICAR QUE SEAN NECESARIOS --
grant SELECT,INSERT,UPDATE,DELETE on ADMINDB.CATEGORIA to ADMINISTRADOR;
grant SELECT,INSERT,UPDATE,DELETE on ADMINDB.METODOPAGO to ADMINISTRADOR;
-- END DELETES (Se puede cambiar por un estado activo/inactivo)
grant SELECT,INSERT,UPDATE on ADMINDB.PRODUCTO to ADMINISTRADOR;
grant SELECT,INSERT on ADMINDB.REPRESENTANTE to ADMINISTRADOR;
grant SELECT,INSERT,UPDATE on ADMINDB.CLASIFICACION to ADMINISTRADOR;
grant SELECT,INSERT ON ADMINDB.REGION to ADMINISTRADOR;
grant SELECT,INSERT on ADMINDB.PAIS to ADMINISTRATOR;
grant SELECT ON ADMINDB.CALISERVICIO to ADMINISTRADOR;
grant SELECT ON ADMINDB.PEDIDO to ADMINISTRADOR;

-- Permisos para el Rol Cliente
create role CLIENTE;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDIDO to CLIENTE;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDI_ITEM to CLIENTE;
grant SELECT,UPDATE on ADMINDB.CLIENTE to CLIENTE;
grant UPDATE on ADMINDB.CALISERVICIO to CLIENTE;
grant UPDATE on ADMINDB.PAGOPEDIDO to CLIENTE;
grant SELECT on ADMINDB.PRODUCTO to CLIENTE;
grant SELECT on ADMINDB.METODOPAGO to CLIENTE;
grant SELECT on ADMINDB.REPRESENTANTE to CLIENTE;
grant SELECT on ADMINDB.PAIS to CLIENTE;

-- Permisos para el Rol Representante
create role REPRESENTANTE;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDI_ITEM to REPRESENTANTE;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDIDO to REPRESENTANTE;
grant SELECT,INSERT on ADMINDB.CLIENTE to REPRESENTANTE;
grant SELECT on ADMINDB.PAIS to REPRESENTANTE;
grant UPDATE on ADMINDB.REPRESENTANTE to REPRESENTANTE;

-- Permisos para el Rol Director
create role DIRECTOR;
grant SELECT,UPDATE,INSERT on ADMINDB.REPRESENTANTE to DIRECTOR;
grant SELECT,INSERT on ADMINDB.CLIENTE to DIRECTOR;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDIDO to DIRECTOR;
grant SELECT,UPDATE,INSERT on ADMINDB.PEDI_ITEM to DIRECTOR;
grant SELECT on ADMINDB.PAIS to DIRECTOR;