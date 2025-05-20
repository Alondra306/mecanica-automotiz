from models.database import conectar

class EmpleadoController:
    
    def __init__(self):
        self.conexion = conectar() 

    def registrar_empleado(self, nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero, password):
        try:
            cursor = self.conexion.cursor()
 
            query = """
                INSERT INTO registro
                (nombre, apellido, telefono, fecha_nacimiento,correo, rfc, cargo, genero, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            valores = (nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero,  password)
            cursor.execute(query, valores)
            self.conexion.commit()

            return True  # Registro exitoso
        except Exception as e:
            print(f"Error al registrar: {e}")
            return False
        
    def obtener_empleados(self):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero FROM registro"
            cursor.execute(query)
            filas = cursor.fetchall()

            empleados = []
            for fila in filas:
                empleados.append({
                    'nombre': fila[0],
                    'apellido': fila[1],
                    'telefono': fila[2],
                    'fecha_nacimiento': fila[3],
                    'correo': fila[4],
                    'rfc': fila[5],
                    'cargo': fila[6],
                    'genero': fila[7],
                })

            return empleados
        except Exception as e:
            print(f"Error al obtener empleados: {e}")
            return []

    def obtener_empleado_por_rfc(self, rfc):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero  FROM registro WHERE rfc = %s"
            cursor.execute(query, (rfc,))
            fila = cursor.fetchone()
            if fila:
                return {
                    'nombre': fila[0],
                    'apellido': fila[1],
                    'telefono': fila[2],
                    'fecha_nacimiento': fila[3],
                    'correo': fila[4],
                    'rfc': fila[5],
                    'cargo': fila[6],
                    'genero': fila[7],
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener empleado por RFC: {e}")
            return None
 
    def actualizar_empleado(self, nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero):
        try:
            cursor = self.conexion.cursor()
            query = """
                UPDATE registro
                SET nombre=%s, apellido=%s, telefono=%s, fecha_nacimiento=%s, correo=%s, cargo=%s, genero=%s
                WHERE rfc=%s
            """
            cursor.execute(query, (nombre, apellido, telefono, fecha_nacimiento, correo, cargo, genero, rfc))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")


    def eliminar_empleado(self, rfc):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM registro WHERE rfc=%s", (rfc,))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
