# Sistema de Vuelos - Backend API

API REST desarrollada con Django y Django REST Framework para la gestión de vuelos, reservas y pasajeros.

## Tecnologías

- Python 3.13
- Django 6.0
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Instalación

Clonar el repositorio y crear el entorno virtual:

```bash
git clone https://github.com/JossGuerrero/sistema-vuelos.git
cd sistema-vuelos
uv sync
```

Configurar variables de entorno en `.env`:

DEBUG=True
DB_NAME=sistema_vuelos
DB_USER=sistema_vuelos
DB_PASSWORD=sistema_vuelos
DB_HOST=localhost
DB_PORT=5432

Aplicar migraciones y correr el servidor:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

## Endpoints principales

- `POST /api/auth/login/` — iniciar sesión
- `POST /api/auth/registro/` — registrar usuario
- `GET /api/vuelos/` — listar vuelos
- `GET /api/aeropuertos/` — listar aeropuertos
- `GET /api/reservas/` — listar reservas
- `GET /api/pasajeros/` — listar pasajeros
- `GET /api/aeronaves/` — listar aeronaves

## Autenticación

La API usa JWT. Para acceder a los endpoints protegidos hay que incluir el token en el header:

```http
Authorization: Bearer <access_token>
```

### Endpoints de autenticación

- `POST /api/auth/registro/` — registrar un nuevo usuario
- `POST /api/auth/login/` — iniciar sesión
- `POST /api/auth/token/refresh/` — renovar token
- `POST /api/auth/token/verify/` — verificar token
- `POST /api/auth/logout/` — cerrar sesión

### Notas adicionales

- El proyecto usa autenticación JWT para todos los endpoints protegidos.
- Puedes probar la API con Postman, Insomnia o curl.
- El servidor local normalmente corre en `http://127.0.0.1:8000/`.

### Tablas principales del sistema

- `vuelos_aeropuerto`
- `vuelos_aerolinea`
- `vuelos_aeronave`
- `vuelos_asiento`
- `vuelos_asignaciontripulacion`
- `vuelos_checkin`
- `vuelos_ciudad`
- `vuelos_equipaje`
- `vuelos_escala`
- `vuelos_estadovuelo`
- `vuelos_factura`
- `vuelos_metodopago`
- `vuelos_notificacion`
- `vuelos_pais`
- `vuelos_pago`
- `vuelos_pasajero`
- `vuelos_promocion`
- `vuelos_puerta`
- `vuelos_reserva`
- `vuelos_reservaservicio`
- `vuelos_servicio`
- `vuelos_tarifa`
- `vuelos_terminal`
- `vuelos_tipoavion`
- `vuelos_tripulacion`
- `vuelos_vuelo`

### Endpoints por tabla

- `Usuarios`: `GET /api/usuarios/`, `GET /api/usuarios/{id}/`, `POST /api/usuarios/`, `PATCH /api/usuarios/{id}/`, `PUT /api/usuarios/{id}/`, `DELETE /api/usuarios/{id}/`
- `Aeropuertos`: `GET /api/aeropuertos/`, `GET /api/aeropuertos/{id}/`, `POST /api/aeropuertos/`, `PATCH /api/aeropuertos/{id}/`, `PUT /api/aeropuertos/{id}/`, `DELETE /api/aeropuertos/{id}/`
- `Aerolineas`: `GET /api/aerolineas/`, `GET /api/aerolineas/{id}/`, `POST /api/aerolineas/`, `PATCH /api/aerolineas/{id}/`, `PUT /api/aerolineas/{id}/`, `DELETE /api/aerolineas/{id}/`
- `Aeronaves`: `GET /api/aeronaves/`, `GET /api/aeronaves/{id}/`, `POST /api/aeronaves/`, `PATCH /api/aeronaves/{id}/`, `PUT /api/aeronaves/{id}/`, `DELETE /api/aeronaves/{id}/`
- `Vuelos`: `GET /api/vuelos/`, `GET /api/vuelos/{id}/`, `POST /api/vuelos/`, `PATCH /api/vuelos/{id}/`, `PUT /api/vuelos/{id}/`, `DELETE /api/vuelos/{id}/`
- `Pasajeros`: `GET /api/pasajeros/`, `GET /api/pasajeros/{id}/`, `POST /api/pasajeros/`, `PATCH /api/pasajeros/{id}/`, `PUT /api/pasajeros/{id}/`, `DELETE /api/pasajeros/{id}/`
- `Reservas`: `GET /api/reservas/`, `GET /api/reservas/{id}/`, `POST /api/reservas/`, `PATCH /api/reservas/{id}/`, `PUT /api/reservas/{id}/`, `DELETE /api/reservas/{id}/`
- `Países`: `GET /api/paises/`, `GET /api/paises/{id}/`, `POST /api/paises/`, `PATCH /api/paises/{id}/`, `PUT /api/paises/{id}/`, `DELETE /api/paises/{id}/`
- `Ciudades`: `GET /api/ciudades/`, `GET /api/ciudades/{id}/`, `POST /api/ciudades/`, `PATCH /api/ciudades/{id}/`, `PUT /api/ciudades/{id}/`, `DELETE /api/ciudades/{id}/`
- `Terminales`: `GET /api/terminales/`, `GET /api/terminales/{id}/`, `POST /api/terminales/`, `PATCH /api/terminales/{id}/`, `PUT /api/terminales/{id}/`, `DELETE /api/terminales/{id}/`
- `Puertas`: `GET /api/puertas/`, `GET /api/puertas/{id}/`, `POST /api/puertas/`, `PATCH /api/puertas/{id}/`, `PUT /api/puertas/{id}/`, `DELETE /api/puertas/{id}/`
- `Tipos de avión`: `GET /api/tipos-avion/`, `GET /api/tipos-avion/{id}/`, `POST /api/tipos-avion/`, `PATCH /api/tipos-avion/{id}/`, `PUT /api/tipos-avion/{id}/`, `DELETE /api/tipos-avion/{id}/`
- `Tarifas`: `GET /api/tarifas/`, `GET /api/tarifas/{id}/`, `POST /api/tarifas/`, `PATCH /api/tarifas/{id}/`, `PUT /api/tarifas/{id}/`, `DELETE /api/tarifas/{id}/`
- `Equipajes`: `GET /api/equipajes/`, `GET /api/equipajes/{id}/`, `POST /api/equipajes/`, `PATCH /api/equipajes/{id}/`, `PUT /api/equipajes/{id}/`, `DELETE /api/equipajes/{id}/`
- `Tripulación`: `GET /api/tripulacion/`, `GET /api/tripulacion/{id}/`, `POST /api/tripulacion/`, `PATCH /api/tripulacion/{id}/`, `PUT /api/tripulacion/{id}/`, `DELETE /api/tripulacion/{id}/`
- `Asignaciones`: `GET /api/asignaciones/`, `GET /api/asignaciones/{id}/`, `POST /api/asignaciones/`, `PATCH /api/asignaciones/{id}/`, `PUT /api/asignaciones/{id}/`, `DELETE /api/asignaciones/{id}/`
- `Escalas`: `GET /api/escalas/`, `GET /api/escalas/{id}/`, `POST /api/escalas/`, `PATCH /api/escalas/{id}/`, `PUT /api/escalas/{id}/`, `DELETE /api/escalas/{id}/`
- `Estados de vuelo`: `GET /api/estados-vuelo/`, `GET /api/estados-vuelo/{id}/`, `POST /api/estados-vuelo/`, `PATCH /api/estados-vuelo/{id}/`, `PUT /api/estados-vuelo/{id}/`, `DELETE /api/estados-vuelo/{id}/`
- `Notificaciones`: `GET /api/notificaciones/`, `GET /api/notificaciones/{id}/`, `POST /api/notificaciones/`, `PATCH /api/notificaciones/{id}/`, `PUT /api/notificaciones/{id}/`, `DELETE /api/notificaciones/{id}/`
- `Métodos de pago`: `GET /api/metodos-pago/`, `GET /api/metodos-pago/{id}/`, `POST /api/metodos-pago/`, `PATCH /api/metodos-pago/{id}/`, `PUT /api/metodos-pago/{id}/`, `DELETE /api/metodos-pago/{id}/`
- `Pagos`: `GET /api/pagos/`, `GET /api/pagos/{id}/`, `POST /api/pagos/`, `PATCH /api/pagos/{id}/`, `PUT /api/pagos/{id}/`, `DELETE /api/pagos/{id}/`
- `Promociones`: `GET /api/promociones/`, `GET /api/promociones/{id}/`, `POST /api/promociones/`, `PATCH /api/promociones/{id}/`, `PUT /api/promociones/{id}/`, `DELETE /api/promociones/{id}/`
- `Asientos`: `GET /api/asientos/`, `GET /api/asientos/{id}/`, `POST /api/asientos/`, `PATCH /api/asientos/{id}/`, `PUT /api/asientos/{id}/`, `DELETE /api/asientos/{id}/`
- `Check-in`: `GET /api/checkins/`, `GET /api/checkins/{id}/`, `POST /api/checkins/`, `PATCH /api/checkins/{id}/`, `PUT /api/checkins/{id}/`, `DELETE /api/checkins/{id}/`
- `Servicios`: `GET /api/servicios/`, `GET /api/servicios/{id}/`, `POST /api/servicios/`, `PATCH /api/servicios/{id}/`, `PUT /api/servicios/{id}/`, `DELETE /api/servicios/{id}/`
- `Reserva servicios`: `GET /api/reserva-servicios/`, `GET /api/reserva-servicios/{id}/`, `POST /api/reserva-servicios/`, `PATCH /api/reserva-servicios/{id}/`, `PUT /api/reserva-servicios/{id}/`, `DELETE /api/reserva-servicios/{id}/`
- `Facturas`: `GET /api/facturas/`, `GET /api/facturas/{id}/`, `POST /api/facturas/`, `PATCH /api/facturas/{id}/`, `PUT /api/facturas/{id}/`, `DELETE /api/facturas/{id}/`

## Cómo funciona la API en general

La API está construida con Django REST Framework y representa el ciclo completo de operación de una aerolínea o sistema de vuelos.

### 1. Flujo completo del sistema

1. Se crean los datos base del sistema:
   - países y ciudades
   - aeropuertos, terminales y puertas
   - aerolíneas y tipos de avión
   - aeronaves

2. Se definen las condiciones operativas:
   - tarifas
   - promociones
   - estados de vuelo
   - servicios opcionales

3. Se registran los vuelos:
   - un vuelo tiene origen y destino
   - usa una aeronave específica
   - puede tener estado, escalas y tripulación asignada

4. Se procesa la venta:
   - se registran pasajeros
   - se generan reservas
   - se asignan asientos
   - se registran pagos y métodos de pago

5. Se completa la operación del viaje:
   - se realiza el check-in
   - se emiten facturas
   - se registran servicios adicionales
   - se generan notificaciones

### 2. Cómo se conectan las tablas

La lógica del sistema está organizada por relaciones entre modelos:

- `vuelos_pais` y `vuelos_ciudad` → definen la ubicación geográfica de los aeropuertos.
- `vuelos_aeropuerto` → contiene terminales, puertas y está conectado a ciudades y países.
- `vuelos_aerolinea` → representa la empresa aérea.
- `vuelos_tipoavion` y `vuelos_aeronave` → definen la flota disponible.
- `vuelos_vuelo` → se conecta con aeropuertos, aeronaves, estados de vuelo, tarifas y promociones.
- `vuelos_pasajero` → representa a la persona que viaja.
- `vuelos_asiento` → pertenece a un vuelo y se usa en la reserva.
- `vuelos_reserva` → une pasajero, vuelo, asiento y pago.
- `vuelos_pago` → registra el pago asociado a una reserva.
- `vuelos_factura` → se genera a partir del pago o la reserva.
- `vuelos_checkin` → se relaciona con una reserva y un pasajero.
- `vuelos_servicio` y `vuelos_reservaservicio` → agregan servicios extras a una reserva.
- `vuelos_tripulacion` y `vuelos_asignaciontripulacion` → asignan personal a un vuelo.
- `vuelos_escala` → representa escalas intermedias del trayecto.
- `vuelos_notificacion` → se usa para mandar avisos al usuario o al sistema.

### 3. Qué hacen los administradores

El rol de administrador o staff es el encargado de gestionar los datos maestros y operativos del sistema.

Los administradores normalmente tienen acceso a:

- crear, editar y eliminar aeropuertos
- crear, editar y eliminar aeronaves
- crear, editar y eliminar vuelos
- administrar tarifas, promociones y estados de vuelo
- manejar tripulación, asignaciones y escalas
- ver y controlar reservas, pagos y facturas
- gestionar servicios y check-in

En términos prácticos, los admins son los encargados de mantener el sistema operativo y de asegurar que los vuelos, reservas y procesos financieros funcionen correctamente.

### 4. Qué hace cada parte del sistema

- `Autenticación`: permite registrar usuarios, iniciar sesión y proteger endpoints con JWT.
- `Usuarios`: gestionan los usuarios del sistema.
- `Aeropuertos`: administran la infraestructura de llegada y salida.
- `Aeronaves`: administran la flota disponible.
- `Vuelos`: coordinan horarios, rutas, aeronaves y estados.
- `Pasajeros`: guardan la información de quienes viajan.
- `Reservas`: representan la compra o asignación de un lugar en un vuelo.
- `Asientos`: controlan la disponibilidad del avión.
- `Pagos y facturas`: administran la parte financiera.
- `Check-in`: gestiona el proceso de ingreso al vuelo.
- `Servicios`: permiten agregar extras como equipaje o servicios premium.
- `Tripulación`: gestiona el personal responsable del vuelo.

### 5. Comportamiento de los endpoints

- `GET` → consulta información.
- `POST` → crea un nuevo registro.
- `PATCH` → actualiza parcialmente.
- `PUT` → reemplaza completamente un recurso.
- `DELETE` → elimina un recurso.
- Los endpoints protegidos requieren `Authorization: Bearer <token>`.

### 6. Resumen ejecutivo de negocio

Este backend está pensado para cubrir todo el flujo de una aerolínea:

- definir la infraestructura y la flota
- programar vuelos
- vender asientos
- registrar pasajeros y reservas
- cobrar y emitir comprobantes
- gestionar el embarque y servicios adicionales
- mantener el control operativo del viaje

En pocas palabras, la API permite pasar desde la planificación del vuelo hasta la operación real del mismo, con todos los datos relacionados entre sí.