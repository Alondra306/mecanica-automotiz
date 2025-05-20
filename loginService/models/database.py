import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host= "localhost",
            port=3306,
            user="root",
            password="",
            database="empleados"
        )
        if conexion.is_connected():
            print("¡Conexión exitosa a la base de datos!")
            return conexion 
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
if __name__ == "__main__":
    conectar()