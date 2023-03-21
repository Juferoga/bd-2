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
##### Extras 🙂
Comando xD, pero que salio muy áspero.
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print $3".sql"}' | xargs touch
```
x2 hahaha
```bash
head -n 15 ../ScriptModeloRelacional.sql | awk '{print "start /home/juferoga/repos/ud/bd-2/backend/database/scriptsLlenado/"$3".sql;"}' >> ../scriptLlenado.sql
```