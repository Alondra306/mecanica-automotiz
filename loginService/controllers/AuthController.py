#from models.user import User
from models.database import conectar 

class AuthController:
    def __init__(self):
        self.conexion = conectar()
        
    def obtener_usuario(self, correo, password):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM registro WHERE correo=%s AND password=%s", (correo, password))

            return cursor.fetchone()
        
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None

