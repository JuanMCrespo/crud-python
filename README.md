# CRUD Clientes - Juan M. Crespo

Sistema de gestión de clientes desarrollado en Python con SQLite como base de datos y Tkinter para la interfaz gráfica.

---

## Estructura del proyecto

```
crud_python/
│
├── main.py         → Punto de entrada del programa
├── conexion.py     → Conexión a la base de datos
├── init_db.py      → Creación de tablas
├── cliente.py      → Clase Clientes con los métodos CRUD
├── interfaz.py     → Interfaz gráfica con Tkinter
└── README.md       → Documentación del proyecto
```

---

## Librerias utilizadas

- Python 3.x
- SQLite3 (incluido en Python)
- Tkinter (incluido en Python)
- Pillow (para la imagen de fondo)

### Instalación de Pillow

```bash
pip install Pillow
```

---

## Base de datos

**Archivo:** `clientesBD.db`  
**Tabla:** `cliente`

| Campo        | Tipo    | Restricciones                          | Descripción                                              |
|--------------|---------|----------------------------------------|----------------------------------------------------------|
| id_cliente   | INTEGER | PRIMARY KEY AUTOINCREMENT              | Identificador único del cliente                          |
| tipo_cliente | TEXT    | NOT NULL, CHECK (Particular/Empresa)   | Tipo de cliente                                          |
| dni          | TEXT    | NOT NULL, UNIQUE                       | Número de documento (obligatorio siempre)                |
| nombre       | TEXT    | NOT NULL                               | Nombre de la persona de contacto                         |
| apellido     | TEXT    | NOT NULL                               | Apellido de la persona de contacto                       |
| nacionalidad | TEXT    |                                        | Nacionalidad del cliente                                 |
| cod_postal   | TEXT    |                                        | Código postal del domicilio                              |
| telefono     | TEXT    |                                        | Número de teléfono                                       |
| email        | TEXT    | UNIQUE                                 | Correo electrónico                                       |
| domicilio    | TEXT    |                                        | Dirección del cliente                                    |
| cuit         | TEXT    | UNIQUE                                 | CUIT (obligatorio si es Empresa, validado desde Python)  |
| razon_social | TEXT    |                                        | Razón social (obligatoria si es Empresa)                 |

### Reglas de negocio

- El **DNI** es obligatorio para todos los clientes (Particular y Empresa).
- El **CUIT** y la **razón social** son obligatorios solo si `tipo_cliente = "Empresa"`. Esta validación se realiza desde Python, no desde la base de datos.

---

## Descripción de archivos

### `conexion.py`
Contiene la clase `Conexion` con el método estático `conexionBD()` que establece y retorna la conexión a la base de datos SQLite.

### `init_db.py`
Contiene la función `crear_tablas()` que crea la tabla `cliente` si no existe. Se ejecuta al iniciar el programa.

### `cliente.py`
Contiene la clase `Clientes` con los atributos del cliente y todos los métodos CRUD.

### `interfaz.py`
Contiene la clase `Aplicacion` con toda la interfaz gráfica construida con Tkinter.

### `main.py`
Punto de entrada del programa. Llama a `crear_tablas()` e inicia la interfaz.

---

## Métodos de la clase `Clientes`

### `__init__()`
Inicializa un objeto Cliente con todos sus atributos:
`tipo_cliente`, `dni`, `nombre`, `apellido`, `nacionalidad`, `cod_postal`, `telefono`, `email`, `domicilio`, `cuit`, `razon_social`.

---

### `insertar()` — CREATE
Inserta un nuevo cliente en la base de datos con los datos del objeto.

```python
cliente = Clientes("Particular", "12345678", "Juan", "Perez",
                   "Argentina", "1234", "1134567890", "juan@email.com",
                   "Calle Falsa 123", None, None)
cliente.insertar()
```

---

### `listar()` — READ
Retorna todos los clientes de la base de datos como una lista de tuplas.

```python
clientes = Clientes.listar()
for c in clientes:
    print(c)
```

---

### `buscar(campo, valor)` — SEARCH
Busca clientes por cualquier campo usando coincidencia parcial (LIKE).
Retorna una lista de clientes encontrados o imprime "Cliente inexistente" si no hay resultados.

```python
clientes = Clientes.buscar("nombre", "Juan")
if clientes:
    for c in clientes:
        print(c)
```

---

### `actualizar(campo, valor)` — UPDATE
Busca un cliente, lo muestra, solicita confirmación y permite modificar el valor de un campo.

```python
Clientes.actualizar("nombre", "Juan")
```

---

### `eliminar(campo, valor)` — DELETE
Busca un cliente, lo muestra, solicita confirmación y lo elimina de la base de datos.

```python
Clientes.eliminar("nombre", "Juan")
```

---

## Interfaz gráfica

Construida con Tkinter. Estructura de la ventana principal:

```
╔═══════════════════════════════════════════════╗
║              GESTIÓN DE CLIENTES              ║
╠═══════════╦═══════════════════════════════════╣
║           ║                                   ║
║ Agregar   ║                                   ║
║ Listar    ║        Área de contenido          ║
║ Buscar    ║        (imagen de fondo)          ║
║ Actualizar║                                   ║
║ Eliminar  ║                                   ║
║           ║                                   ║
╚═══════════╩═══════════════════════════════════╝
```

- **Panel izquierdo** → botones de navegación
- **Panel derecho** → área de contenido con imagen de fondo, donde se muestran formularios y resultados según la operación seleccionada

---

## Cómo ejecutar

```bash
python3 main.py
```

---

*Proyecto Crud PythonJuan M. Crespo — 2026*
