# Preentrega – Automatización QA

## Propósito del proyecto

Este proyecto automatiza pruebas de **regresión** sobre el sitio de práctica [Sauce Demo](https://www.saucedemo.com/). Las pruebas de regresión son aquellas que se repiten cada vez que se hacen cambios en el código, para asegurarse de que lo que ya funcionaba no se rompió.

La idea es ahorrar tiempo evitando repetir siempre las mismas pruebas de forma manual, y dejar el testing manual para lo que realmente necesita ser observado por una persona.

### Casos de prueba automatizados

| Módulo | Prueba | Qué valida |
|---|---|---|
| Login | `test_login_exitoso` | Que con credenciales correctas se acceda al catálogo |
| Login | `test_login_credenciales_invalidas` | Que se muestre el mensaje de error con credenciales incorrectas |
| Login | `test_login_campos_vacios` | Que se muestre el error al intentar ingresar sin completar los campos |
| Inventory | `test_visualizacion_productos` | Que el catálogo muestre productos con su nombre y precio |
| Inventory | `test_visualizacion_elementos` | Que estén presentes el menú, el filtro y el ícono del carrito |
| Cart | `test_agregar_producto_al_carrito` | Que se pueda agregar un producto al carrito |
| Cart | `test_verificar_item_carrito` | Que el producto agregado aparezca en el carrito |
| Cart | `test_eliminar_producto_del_carrito` | Que se pueda eliminar un producto del carrito |

## Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías y herramientas:

- **Python**: lenguaje utilizado para desarrollar los scripts de automatización.
- **Selenium WebDriver**: herramienta utilizada para automatizar la interacción con el navegador.
- **Pytest**: framework utilizado para ejecutar las pruebas y verificar si pasan o fallan.
- **pytest-html**: plugin utilizado para generar un reporte HTML con los resultados de las pruebas.
- **Firefox**: navegador donde se ejecutan las pruebas.
- **Visual Studio Code**: entorno de desarrollo utilizado para crear y ejecutar el proyecto.

## Estructura del proyecto

```
preentrega/
├── pytest.ini          # Configuración de pytest
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
└── reports/
    └── reporte.html    # Reporte generado al ejecutar las pruebas
```

### Descripción de los archivos y carpetas

**pytest.ini**
Contiene la configuración de Pytest utilizada en el proyecto. Permite definir el patrón de nombres de los archivos y funciones de prueba y configurar la generación automática del reporte HTML.

**tests/**
Carpeta que contiene los scripts de pruebas automatizadas:

- **test_login.py**: contiene pruebas para validar el inicio de sesión correcto, el ingreso con credenciales inválidas y el intento de inicio de sesión con campos vacíos.
- **test_inventory.py**: contiene pruebas para verificar la visualización de productos y la presencia de elementos importantes de la interfaz del catálogo.
- **test_cart.py**: contiene pruebas para agregar un producto al carrito, verificar que el producto se encuentre en el carrito y eliminarlo.

**reports/**
Carpeta que contiene el archivo **reporte.html**, generado por Pytest mediante pytest-html, con el resultado de la ejecución de las pruebas.

> Las carpetas `__pycache__` y `.pytest_cache` se crean automáticamente al ejecutar pytest.

## Requisitos previos

- Tener **Python** instalado (se puede verificar con `python --version`).
- Tener **Firefox** instalado. **NOTA**: si no se tiene el navegador Firefox instalado, puede modificar la configuración del driver de `driver = webdriver.Firefox()`  a `driver = webdriver.Chrome()` o su navegador de preferencia.

## Instalación de dependencias

1. Clonar o descargar el proyecto y abrir una terminal dentro de la carpeta `preentrega`.
2. Instalar las dependencias:

Para instalar pytest:

```bash
pip install pytest
```

Para instalar la herramienta que genera reportes HTML:

```bash
pip install pytest-html
```

Para instalar Selenium:

```bash
pip install selenium
```

## Ejecución de las pruebas

Desde la carpeta raíz `preentrega`, ejecutar:

Para ejecutar todos los tests:

```bash
pytest -v
```

Para ejecutar un archivo en particular:

```bash
pytest tests/test_login.py
```

Para ejecutar una sola prueba:

```bash
pytest tests/test_login.py::test_login_exitoso
```

La configuración de `pytest.ini` ya incluye las opciones para mostrar el detalle de cada test (`-v -s`) y generar el reporte automáticamente.

## Reporte de resultados

Al finalizar la ejecución se genera el archivo `reports/reporte.html`. Para verlo, abrirlo con cualquier navegador: muestra qué pruebas pasaron, cuáles fallaron y el detalle de cada una.