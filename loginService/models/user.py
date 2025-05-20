from models.database import conectar

class User:
    @staticmethod
    def buscar_usuario(username):
        conexion = conectar()
        cursor = conexion.cursor() 

        consulta = "SELECT correo, password FROM registro WHERE correo = %s"
 
        cursor.execute(consulta, (username,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado 

