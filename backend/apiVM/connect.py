import cx_Oracle

class Connect:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
    
    def open_connection(self):
        try:
            self.connection = cx_Oracle.connect(user=self.user, password=self.password, dsn='redflox.com:1521/VENTAS_MULTINIVEL', encoding="UTF-8")
            self.cursor = self.connection.cursor()
            return [True,'Conectado']
        except cx_Oracle.Error as error:
            return [False, str(error)]
    def execute_query(self, query, params):
        try:
            self.cursor.execute(query, params)
            if self.cursor.description != None:
                return [True, self.cursor.fetchall()]
            else:
                return [True, None]
        except cx_Oracle.Error as error:
            print(error)
            print(query)
            return [False, str(error)]
    def commit(self):
        self.connection.commit()
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    def get_cursor(self):
        return self.cursor