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
| Tabla\Rol     | Admin | Cliente | Empleado |
|---------------|-------|---------|----------|
| BODEGA        | CRU   | -       | -        |
| BODE_PROD     | CRU   | -       | RU       |
| CALISERVICIO  | CR    | -       | CR       |
| CATEGORIA     | CRU   | R       | R        |
| CLASIFICACION | CRU   | -       | -        |
| CLIENTE       | CRU   | R       | R        |
| METODOPAGO    | CRU   | -       | -        |
| PAGOPEDIDO    | CR    | -       | -        |
| PEDIDO        | CRU   | CR      | CRU      |
| PRODUCTO      | CRU   | R       | R        |
| REGION        | CRU   | R       | R        |
| REPRESENTANTE | CRU   | -       | R        |
| USUARIO       | CRU   | R       | R        |

##### Extras 🙂
Comando xD, pero que salio muy áspero.
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print $3".sql"}' | xargs touch
```
x2 hahaha
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print "start /home/juferoga/repos/ud/bd-2/backend/database/scriptsLlenado/"$3".sql;"}' >> ../scriptLlenado.sql
```