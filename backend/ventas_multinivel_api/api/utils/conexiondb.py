import cx_Oracle

def open_connection(user, password):
    try:
        connection=cx_Oracle.connect(
            user = user,
            password = password,
            dsn = 'redflox.com:1521/VENTAS_MULTINIVEL',
            encoding = 'utf8'
        )
        return True, connection
    except Exception as e:
        return False, e
    
def close_connection(connection):
    try:
        connection.close()
        return True
    except Exception as e:
        return False, e
    
__all__ = ['open_connection', 'close_connection']