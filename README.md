# 📅 API de Reservas y Gestión de Turnos

Una API REST moderna, modular y robusta para la gestión automatizada de turnos y reservas, construida con **FastAPI** y **SQLAlchemy**. El sistema implementa reglas de negocio avanzadas para garantizar la consistencia de los datos, evitando solapamientos de horarios de manera inteligente.

---

##  Características Clave

- ✅ **Arquitectura Limpia:** Estructura modular que separa modelos, esquemas de validación, rutas y lógica de negocio.
- ✅ **Gestión de Relaciones (ORM):** Base de datos relacional modelada con SQLAlchemy utilizando claves foráneas e integridad referencial.
- ✅ **Reglas de Negocio Inteligentes:**
  - Validación automática para impedir reservas en fechas u horarios pasados utilizando zonas horarias (UTC).
  - Prevención de reservas simultáneas para un mismo usuario.
  - Prevención de reservas duplicadas para un mismo servicio en el mismo horario.
- ✅ **Validación de Datos:** Uso de **Pydantic** para validar tipos de datos y direcciones de correo electrónico.
- ✅ **Documentación Interactiva:** Generación automática mediante Swagger UI.

---

## 🛠️ Stack Tecnológico

| Tecnología | Descripción |
|------------|-------------|
| 🐍 Python | 3.14+ |
| ⚡ FastAPI | Framework para APIs REST |
| 🚀 Uvicorn | Servidor ASGI |
| 🗄️ SQLAlchemy | ORM |
| 💾 SQLite | Base de datos local |
| ✔️ Pydantic | Validación de datos |
| 📧 email-validator | Validación de emails |

---

## 📂 Arquitectura del Proyecto

```text
api-reservas/
│
├── src/
│   ├── database.py
│   │
│   ├── models/
│   │   ├── usuario.py
│   │   └── reserva.py
│   │
│   ├── schemas/
│   │   ├── usuario.py
│   │   └── reserva.py
│   │
│   └── routers/
│       ├── usuarios.py
│       └── reservas.py
│
├── main.py
├── prueba_db.py
├── .gitignore
└── requirements.txt
```

### 📁 Descripción

| Carpeta / Archivo | Función |
|-------------------|----------|
| **src/models** | Modelos SQLAlchemy (tablas de la BD). |
| **src/schemas** | Esquemas Pydantic para validación y serialización. |
| **src/routers** | Endpoints organizados por recurso. |
| **database.py** | Configuración de la conexión y sesión con SQLite. |
| **main.py** | Punto de entrada de la aplicación. |
| **prueba_db.py** | Script para pruebas de la base de datos. |

---

# 💻 Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/api-reservas.git
cd api-reservas
```

---

## 2️⃣ Crear el entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API quedará disponible en:

```
http://127.0.0.1:8000
```

---

# 📚 Documentación de la API

FastAPI genera automáticamente la documentación.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔌 Endpoints

## 👤 Usuarios

### Crear usuario

```http
POST /usuarios/
```

Registra un nuevo usuario.

### Ejemplo de Body

```json
{
  "nombre": "Juan Pérez",
  "email": "juan@gmail.com"
}
```

---

## 📅 Reservas

### Crear reserva

```http
POST /reservas/
```

Valida:

- existencia del usuario
- fecha futura
- horarios disponibles
- solapamientos

### Ejemplo

```json
{
  "usuario_id": 1,
  "servicio": "Consulta",
  "fecha_hora": "2026-07-20T15:30:00"
}
```

---

### Obtener todas las reservas

```http
GET /reservas/
```

---

### Obtener reservas de un usuario

```http
GET /reservas/usuario/{usuario_id}
```

---

# ✔️ Reglas de Negocio

El sistema implementa varias validaciones para garantizar la integridad de la información:

- No se pueden registrar reservas en el pasado.
- Un usuario no puede tener dos reservas al mismo horario.
- Un servicio no puede reservarse dos veces para el mismo horario.
- Solo pueden reservar usuarios existentes.
- Los correos electrónicos deben tener un formato válido.
- Los emails son únicos.

---

# 📦 Dependencias principales

```txt
fastapi
uvicorn
sqlalchemy
pydantic
email-validator
```

---
