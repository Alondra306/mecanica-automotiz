from flask import Flask, render_template, request, redirect, url_for, session 
from controllers.AuthController import AuthController
from controllers.EmpleadoController import EmpleadoController

app = Flask(__name__)

#app.config['SERVER_NAME'] = 'localhost:8000'

auth_controller = AuthController()
empleado_controller = EmpleadoController()

app.secret_key = 'tu_clave_secreta_aqui'
    
@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        
        # validar y obtener usuario
        usuario = auth_controller.obtener_usuario(username, password)
        
        if usuario:
            session['usuario'] = usuario['correo']
            session['cargo'] = usuario['cargo']
            
            if usuario['cargo'] == 'Administrador':
                return redirect(url_for('inicio_admin'))  #administrador
            else:
                return redirect(url_for('inicio_empleado'))  # empleados
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos.")
    return render_template('login.html')

@app.route('/inicio_admin')
def inicio_admin():
    if 'usuario' in session and session['cargo'] == 'Administrador':
        return render_template('header.html', usuario=session['usuario'], cargo=session['cargo'])  # acceso completo
    else:
        return redirect(url_for('login'))

@app.route('/inicio_empleado')
def inicio_empleado():
    if 'usuario' in session and session['cargo'] != 'Administrador':
        return render_template('headerE.html', usuario=session['usuario'], cargo=session['cargo'])  # acceso empleado
    else:
        return redirect(url_for('login'))  

@app.route('/logout', methods=['GET'])  
def logout(): 
    session.pop('usuario', None)
    session.pop('cargo', None)
    return redirect(url_for('login'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            telefono = request.form['telefono']
            fecha_nacimiento = request.form['fecha_nacimiento']
            correo = request.form['correo'] 
            rfc = request.form['rfc']
            cargo = request.form['cargo']
            genero = request.form['genero'] 
            password = request.form['password'] 
           # Registrar el empleado
            registro_exitoso = empleado_controller.registrar_empleado(nombre, apellido, telefono, fecha_nacimiento, correo, rfc, cargo, genero, password)

            if registro_exitoso:
                return redirect(url_for('inicio_admin'))
            else:
                return "Error al registrar el empleado :(", 500
        except KeyError as e:
            return f"Falta el campo requerido: {e}", 400
        
    return render_template('empleados.html') 

@app.route('/empleados')
def ver_empleados():
    empleados = empleado_controller.obtener_empleados()
    return render_template('ver_empleados.html', empleados=empleados)

@app.route('/empleados/editar/<rfc>', methods=['GET', 'POST'])
def editar_empleado(rfc):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        correo = request.form['correo']
        rfc= request.form['rfc']
        cargo = request.form['cargo']
        genero = request.form['genero']

        empleado_controller.actualizar_empleado( nombre, apellido, telefono, fecha_nacimiento,correo, rfc, cargo, genero)
        return redirect(url_for('ver_empleados'))
 
    empleado = empleado_controller.obtener_empleado_por_rfc(rfc)
    return render_template('empleados.html', empleado=empleado)
 
@app.route('/empleados/eliminar/<rfc>')
def eliminar_empleado(rfc):
    empleado_controller.eliminar_empleado(rfc)
    return redirect(url_for('ver_empleados'))

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True)
    app.run(debug=True)

