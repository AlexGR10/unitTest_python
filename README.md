# Ejemplos de Pruebas Unitarias y Web en Python

Este repositorio contiene ejemplos de pruebas unitarias y pruebas web en Python utilizando `pytest` y Flask. El propósito es demostrar cómo escribir y ejecutar pruebas unitarias y pruebas web para diferentes funciones y clases en Python.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:


. ├── src │ ├── main.py # Contiene funciones de suma, resta y división │ ├── main2.py # Contiene la clase ShoppingCart │ ├── app.py # Aplicación Flask para pruebas web │ └── test │ ├── test_main.py # Pruebas unitarias para main.py │ ├── test_main2.py # Pruebas unitarias para main2.py │ └── test_app.py # Pruebas unitarias para la aplicación Flask ├── README.md # Este archivo └── venv # Entorno virtual para aislar dependencias


## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

### Ejecutar Pruebas Unitarias

Para ejecutar las pruebas unitarias, usa el siguiente comando:
```sh
pytest

Ejecutar la Aplicación Flask
Para ejecutar la aplicación Flask, usa el siguiente comando:

flask --app src/app.py run

Pruebas Web con Postman
Puedes usar Postman para realizar pruebas web en los endpoints de la aplicación Flask. Asegúrate de que la aplicación Flask esté en ejecución y luego usa Postman para enviar solicitudes HTTP a los endpoints definidos.

Descripción de los Archivos
main.py
Contiene funciones básicas de suma, resta y división:

sum(x, y): Retorna la suma de x e y.
sub(x, y): Retorna la resta de x menos y.
div(x, y): Retorna la división de x entre y, lanza una excepción si y es 0.
test_main.py
Contiene pruebas unitarias para las funciones en main.py:

test_sum(): Verifica que la suma es correcta.
test_sub(): Verifica que la resta es correcta.
test_div(): Verifica que la división es correcta y maneja la excepción de división por cero.
main2.py
Contiene la clase ShoppingCart que permite agregar ítems a un carrito de compras, obtener el tamaño del carrito y obtener una copia de los ítems en el carrito.

test_main2.py
Contiene pruebas unitarias para la clase ShoppingCart:

test_add_item(): Verifica que se pueden agregar ítems al carrito.
test_size(): Verifica que el tamaño del carrito se actualiza correctamente.
test_get_items(): Verifica que se puede obtener una copia de los ítems en el carrito.
test_empty_cart(): Verifica que un carrito nuevo está vacío.
app.py
Contiene una aplicación Flask simple con un endpoint:

hello_world(): Retorna un mensaje “Hello, World!”.
test_app.py
Contiene pruebas unitarias para la aplicación Flask:

test_hello_world(): Verifica que el endpoint / retorna el mensaje “Hello, World!”.
