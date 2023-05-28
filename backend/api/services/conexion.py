from cx_Oracle import DatabaseError

def is_connection_active(connection):
    try:
        # Crea un cursor
        cur = connection.cursor()
        
        # Ejecuta una consulta simple
        cur.execute('SELECT 1 FROM DUAL')

        # Si no hubo errores, la conexión está activa
        return True
    except:
        return False