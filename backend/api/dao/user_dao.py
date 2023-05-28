from models.user import User, UserOfDB

class UserDao:
    def __init__(self, connection):
        self.nombre = "UserDao"
        self.connection = connection

    def get_by_username(self, username):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'''
                    SELECT *
                    FROM USUARIO
                    WHERE T_USERNAME = '{username}'
            ''')
            print("ESTE ES EL USERNAME:", username)
            # Obtener los nombres de las columnas
            columnas = [d[0] for d in cursor.description]
            # Obtener el primer resultado
            row = cursor.fetchone()
        except Exception as e:
            return {"error": e.message}
        if row is None:
            cursor.close()
            return {"error": "Usuario no existe"} 
        # Obtener los datos del usuario en un diccionario
        response_db = dict(zip(columnas, row))
        usuario = User(
            id=response_db["K_USUARIO"],
            nombre=response_db["T_NOMBRE"],
            apellido=response_db["T_APELLIDO"],
            fecha_de_nacimiento=response_db["F_NACIMIENTO"],
            genero=response_db["I_GENERO"],
            telefono=response_db["N_TELEFONO"],
            direccion=response_db["T_DIRECCION"],
            email=response_db["T_EMAIL"],
            estado=response_db["I_ESTADO"]
        )
        cursor.close()
        return usuario

    def get_by_id(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f'''
                SELECT *
                FROM USUARIO
                WHERE K_USUARIO = '{id}';
        ''')
        # Obtener los nombres de las columnas
        columnas = [d[0] for d in cursor.description]
        # Obtener los datos del usuario en un diccionario
        usuario = dict(zip(columnas, cursor.fetchone()))
        cursor.close()
        return usuario

    def create(self, user: UserOfDB):
        sql = [ 
            f"create user {user.username} identified by {user.password} default tablespace USERSDEF temporary tablespace USERSTMP quota 1m on USERSDEF",
            f"grant connect to {user.username}",
            f"INSERT INTO usuario (t_nombre, t_apellido, f_nacimiento, i_genero, n_telefono, t_direccion, t_email, i_estado) VALUES {user.nombre},{user.apellido},{user.fecha_de_nacimiento},{user.genero},{user.telefono},{user.direccion},{user.email},'A'"
        ]
        cursor_create_in_db = self.connection.cursor()
        try:
            cursor_create_in_db.execute(sql[0])
        except Exception as e:
            return e
        if cursor_create_in_db.rowcount > 0:
            cursor_add_permission = self.connection.cursor()
            try:
                cursor_add_permission.execute(sql[1])
            except Exception as e:
                return e
            if cursor_add_permission > 0:
                cursor_insert = self.connection.cursor()
                try:
                    cursor_insert.execute(sql[2])
                except Exception as e:
                    return e
                if cursor_insert > 0:
                    return self.get_by_username(user.username)
        return None

    def edit(self, user: User):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'''
                    UPDATE USUARIO
                    SET T_NOMBRE = '{user.nombre}',
                    T_APELLIDO = '{user.apellido}',
                    F_NACIMIENTO = TO_DATE('{user.fecha_de_nacimiento}', 'YYYY-MM-DD'),
                    I_GENERO = '{user.genero}',
                    N_TELEFONO = {user.telefono},
                    T_DIRECCION = '{user.direccion}',
                    T_EMAIL = '{user.email}',
                    I_ESTADO = '{user.estado}',
                    WHERE K_USUARIO = {user.id}
            ''')
        except Exception as e:
            return e
        if cursor > 0:
            cursor.close()
            user = self.get_by_id(user.id)
            return user
        cursor.close()
        return None
    
    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM USUARIO')
        users = []
        for row in cursor:
            K_USUARIO, T_NOMBRE, T_APELLIDO, F_NACIMIENTO, I_GENERO, N_TELEFONO, T_DIRECCION, T_EMAIL, I_ESTADO, T_USERNAME = row
            users.append({
                'id': K_USUARIO,
                'username': T_USERNAME,
                'nombre': T_NOMBRE,
                'apellido': T_APELLIDO,
                'fecha_de_nacimiento': F_NACIMIENTO,
                'genero': I_GENERO,
                'telefono': N_TELEFONO,
                'direccion': T_DIRECCION,
                'email': T_EMAIL,
                'estado': I_ESTADO
            })

        return users
    
    def __del__(self):
        print(f"El objeto {self.nombre} se está destruyendo")
        self.connection.close()
