<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MecanicaCUT</title>
<link href="css/IndexStyle.css" rel="stylesheet" type="text/css">
</head>

<body>
<header role="banner" class="header">
      <div class="logo">
          <img
            src="Logo.png"
            alt="Logo"
            class="logo-img"
          />
      </div>
      <nav class="navbar">
        <ul>
          <li><a>Inicio</a></li>
          <li><a href="#productos">Productos</a></li>
          <li><a href="#servicios">Servicios</a></li>
          <li><a href="#registro-cita" class="cita">Crear Cita</a></li>
        </ul>
      </nav>
</header>

<section id="productos">
    <h2>Productos</h2>
    <div class="producto-list">
        <article class="producto">
            <img src="css/imagenes/suspension.jpg">
            <h3>Suspensiones</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/llantas.jpg">
            <h3>Llantas</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/aceite.jpg">
            <h3>Aceite</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/bateria.jpeg">
            <h3>Batería para Autos</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/jump.jpg">
            <h3>Cables para corriente</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/kit.jpg">
            <h3>Kit de Limpieza</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/caralarm.png">
            <h3>Alarma de Coche</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/tapete.jpg">
            <h3>Tapetes para Coche</h3>
        </article>
        <article class="producto">
            <img src="css/imagenes/cera.jpg">
            <h3>Cera para Coche</h3>
        </article>
    </div>
</section>

<section id="servicios">
    <h2>Servicios</h2>
    <div class="servicios-container">
        <div class="about-card">
            <h3>Cambio de Aceite</h3>
            <p>
                Cambio de Aceite para prevenir desgaste entre las piezas del motor <br><br><br>
            </p>
            <img src="css/imagenes/oilchange.png" class="bottom-image">
        </div>
        <div class="about-card">
            <h3>Revisiones</h3>
            <p>
                Queremos ofrecer revisiones a nuestros clientes para prevenir desgastes y cuidar el estado de su vehículo <br><br>
            </p>
            <img src="css/imagenes/repair.jpg" class="bottom-image">
        </div>
        <div class="about-card">
            <h3>Mantenimiento</h3>
            <p>
                Realizar revisión para tener un panorama más claro sobre el estado de tu vehículo y planificar los próximos servicios antes de presentar una falla
            </p>
            <img src="css/imagenes/carmain.png" class="bottom-image" />
        </div>
    </div>
</section>

<!-- Registro de Cita -->
<section id="registro-cita">
    <h2>Registro de citas</h2>
    <div class="container">
        <form action="/registro" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required><br>

            <label for="apellido">Apellido:</label>
            <input type="text" id="apellido" name="apellido" required><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="telefono">Telefono:</label>
            <input type="number" id="telefono" name="telefono" required><br>

            <label for="servicio">Servicio:</label>
            <select id="servicio" name="servicio" required>
                <option value="">Seleccione un servicio</option>
                <option value="mantenimiento">Mantenimiento</option>
                <option value="reparacion">Reparación</option>
                <option value="cambio">Cambio de Aceite</option>
                <option value="revision">Revisión de luces</option>
                <option value="limpieza">Limpieza de filtro de aire</option>
                <option value="limpieza1">Limpieza de gasolina</option>
                <option value="limpieza2">Limpieza de bujías</option>
                <option value="bateria">Nivelar la batería</option>
            </select><br>

            <label for="fecha-hora">Selecciona fecha y hora:</label>
            <input type="datetime-local" id="fecha-hora" name="fecha-hora" required><br>

            <button type="submit">Registrarse</button>
        </form>
    </div>
</section>

</body>
</html>
