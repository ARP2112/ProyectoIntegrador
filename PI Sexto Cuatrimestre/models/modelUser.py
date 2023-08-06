from .entities.user import User


class ModelUser():

    @classmethod
    def login(self, mysql, user):
        try:
            cursor = mysql.connection.cursor()
            sql = """SELECT id_usuarios, nombreusuario, contraseña, Nombre_completo FROM Usuarios 
                    WHERE nombreusuario = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, sql, id):
        try:
            cursor = sql.connection.cursor()
            sql = "SELECT id_usuarios, nombreusuario, Nombre_completo FROM Usuarios WHERE id_usuarios = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)