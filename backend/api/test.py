from database.connection_manager import ConnectionManager
from services.conexion import is_connection_active

manager = ConnectionManager()


username = "sga"
password = "netware124"



conn = manager.create_connection(username,password)


# Crear un cursor
cur = conn.cursor()


# Ejecutar una consulta
cur.execute('SELECT * FROM pais')

# Imprimir los resultados
for row in cur:
    print(row)


con1 = manager.create_connection(username,password)

cur1 = con1.cursor()

cur1.execute('SELECT * FROM pais')


# Imprimir los resultados
for row in cur1:
    print(row)

