# Base de datos

## Como ejecutar

Para ejecutar la creación automática de la base de datos, con su base de datos pluggable, tendremos que entrar como SYS y ejecutar el siguiente comando.
Este se ejecuta en un contenedor de Docker especializado para la versión 18c o la versión 21c de Oracle.

```sql
create pluggable database VENTAS_MULTINIVEL admin user <USUARIO> identified by <CLAVE> roles=(connect) file_name_convert=('/opt/oracle/oradata/XE/pdbseed','/opt/oracle/oradata/CE/ventas_multinivel');
```

Luego abrimos la base de datos al público, con el comando.
```sql
alter pluggable database VENTAS_MULTINIVEL open;
```

Entramos a la base de datos creada.
```bash
sqlplus system/<CLAVE>@localhost:1521/VENTAS_MULTINIVEL;
```

Ejecutamos el script de creación y llenado utilizando el comando:
```sql
start ScriptUsers.sql;
```
Recuerda revisar las rutas para que coincidan con el sistema operativo o el contenedor.

---
### OPERACIONES PERMITIDAS POR ROL
| Rol           | C (Crear) | R (Leer) | U (Actualizar) | D (Eliminar) |
|---------------|-----------|----------|----------------|--------------|
| Administrador | Sí        | Sí       | Sí             | Sí           |
| Cliente       | Sí        | Sí       | Sí             | No           |
| Representante | Sí        | Sí       | Sí             | No           |
| Director      | Sí        | Sí       | Sí             | Sí           |
---
### OPERACIONES POR TABLA
--- 
| Tabla\Rol     | Admin | Cliente | Representante | Director  | 
|---------------|-------|---------|---------------|-----------|
| BODEGA        | CRU   | -       | -             |           |
| BODE_PROD     | CRU   | -       | RU            |           |
| CALISERVICIO  | R     | CR      | R             |           |
| CATEGORIA     | CRU   | R       | R             |           |
| CLASIFICACION | CRU   | -       | -             |           |
| CLIENTE       | RU    | CRU     | CR            | CRU       |
| METODOPAGO    | CRU   | -       | -             |           |
| PAGOPEDIDO    | R     | CR      | -             |           |
| PEDIDO        | RU    | CRU     | RU            |           |
| PEDI_ITEM     | R     | CRU     |               |           |
| PRODUCTO      | CRU   | R       | R             |           |
| REGION        | CRU   | R       | R             |           |
| REPRESENTANTE | CRU   | -       | RU            | CRU       |

---
### OPERACIONES DE TABLAS DE PRIVILEGIOS
--- 
| Tabla\Rol        | DJANGO | Contenidos                                                                    |
|------------------|--------|-------------------------------------------------------------------------------|
| DBA_ROLES        |        | Nombres de los roles y su estado del password.                                |
| DBA_ROLE_PRIVS   | R      | Usuarios a los que han sido otorgados roles.                                  |
| DBA_SYS_PRIVS    |        | Usuarios a los que han sido otorgados privilegios del sistema.                |
| DBA_TAB_PRIVS    |        | Usuarios a los que han sido otorgados privilegios sobre objetos.              |
| DBA_COL_PRIVS    |        | Usuarios a los que han sido otorgados privilegios sobre columnas de tablas.   |
| ROLE_ROLE_PRIVS  |        | Roles que han sido otorgados a otros roles.                                   |
| ROLE_SYS_PRIVS   |        | Privilegios de sistema que han sido otorgados a roles.                        |
| ROLE_TAB_PRIVS   |        | Privilegios de tabla que han sido otorgados a roles.                          |





1. Añadir un limite de creacion de clientes -> clientes

##### Extras 🙂
Comando xD, pero que salio muy áspero.
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print $3".sql"}' | xargs touch
```
x2 hahaha
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print "start /home/juferoga/repos/ud/bd-2/backend/database/scriptsLlenado/"$3".sql;"}' >> ../scriptLlenado.sql
```
