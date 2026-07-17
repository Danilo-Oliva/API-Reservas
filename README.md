# 📅 API de Reservas y Gestión de Turnos

Una API REST moderna, modular y robusta para la gestión automatizada de turnos y reservas, construida con **FastAPI** y **SQLAlchemy**. El sistema implementa reglas de negocio avanzadas para garantizar la consistencia de los datos, evitando solapamientos de horarios de manera inteligente.

---

## 🗿 Características Clave

*   **Arquitectura Limpia:** Estructura de carpetas modular que separa modelos, esquemas de validación, rutas de la API y lógica de negocio.
*   **Gestión de Relaciones (ORM):** Base de datos relacional modelada con SQLAlchemy, aplicando claves foráneas e integridad referencial (Cascading Deletes).
*   **Reglas de Negocio Inteligentes:**
    *   **Validación Temporal:** Bloqueo automático de intentos de reserva en fechas u horas pasadas utilizando compatibilidad de zonas horarias (UTC).
    *   **Prevención de Solapamientos (Usuario):** Validación en base de datos que impide que un mismo usuario tenga más de una reserva activa en el mismo minuto exacto.
    *   **Prevención de Solapamientos (Servicio):** Control de concurrencia que bloquea el agendamiento del mismo servicio a la misma hora por diferentes usuarios (ideal para turnos individuales).
*   **Validación de Datos Estricta:** Implementación de esquemas con Pydantic para asegurar tipos de datos correctos y validación de correo electrónico en tiempo real.
*   **Documentación Interactiva:** Autogenerada en tiempo real mediante Swagger UI.

---

## 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.14+
*   **Framework Web:** FastAPI (ASGI)
*   **Servidor Web:** Uvicorn
*   **Mapeador Relacional (ORM):** SQLAlchemy
*   **Motor de Base de Datos:** SQLite (Local)
*   **Validación de Datos:** Pydantic (con `email-validator`)

---

## 📂 Arquitectura del Proyecto

El proyecto sigue una estructura desacoplada para facilitar el mantenimiento y la escalabilidad:

```text
api-reservas/
│
├── src/                        # Código fuente de la aplicación
│   ├── database.py             # Configuración del motor y sesión de SQLAlchemy
│   │
│   ├── models/                 # Modelos de base de datos (Tablas SQL)
│   │   ├── usuario.py          # Tabla de Usuarios y relación con Reservas
│   │   └── reserva.py          # Tabla de Reservas y Clave Foránea (FK)
│   │
│   ├── schemas/                # Modelos de validación (Pydantic)
│   │   ├── usuario.py          # Esquemas de entrada/salida para Usuarios
│   │   └── reserva.py          # Esquemas de entrada/salida para Reservas
│   │
│   └── routers/                # Controladores / Rutas (Endpoints)
│       ├── usuarios.py         # Rutas bajo el prefijo /usuarios
│       └── reservas.py         # Rutas bajo el prefijo /reservas
│
├── main.py                     # Punto de entrada de la aplicación e inicialización
├── prueba_db.py                # Script aislado de testing de base de datos
├── .gitignore                  # Exclusión de entornos virtuales y archivos temporales
└── requirements.txt            # Lista de dependencias del proyecto