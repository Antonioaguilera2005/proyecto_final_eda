Descripción
Este proyecto es una aplicación web que permite comparar precios de productos en tres supermercados: Mercadona, Carrefour y LDL. Los usuarios pueden seleccionar los productos que necesitan, y la aplicación les recomendará dónde es más barato comprar cada uno. Además, los resultados se almacenan en una base de datos SQLite para futuras consultas, optimizando tiempo y recursos.

Características Principales
APIs independientes para cada supermercado

Cada supermercado tiene su propia API que expone dos rutas:
/productos: Devuelve una lista de productos disponibles en ese supermercado.
/producto?nombre=<nombre>: Devuelve el precio de un producto específico.
Comparación de precios

Los usuarios seleccionan productos desde una lista unificada generada a partir de las APIs de los supermercados.
La aplicación consulta los precios de cada producto en los tres supermercados y genera una tabla comparativa.
Ordenación de resultados

Los resultados se presentan en una tabla, ordenados por supermercado o por el precio más bajo utilizando algoritmos de ordenación como Merge Sort o Quick Sort.

Estructura del Proyecto

Proyecto.final.eda/
├── datos.eda/                   # Archivos JSON con productos y precios
│   ├── mercadona.json
│   ├── carrefour.json
│   └── ldl.json
├── mercadona_api.py             # API para Mercadona
├── carrefour_api.py             # API para Carrefour
├── ldl_api.py                   # API para LDL
├── run_all.py                   # Script para ejecutar todas las APIs
├── app.py                       # Aplicación Flask principal
├── templates/                   # Archivos HTML para la interfaz web
│   ├── index.html               # Página principal con la lista de productos
│   └── resultados.html          # Página de resultados con la tabla comparativa
└── README.md                    # Este archivo

Cómo Usar el Proyecto
Ejecutar las APIs de los supermercados

Ejecuta el script run_all.py para iniciar las tres APIs:

Ejecuta el script app.py para iniciar la lista de la compra

Navegar en la aplicación

Abre un navegador y accede a la dirección:
arduino
Copiar código
http://127.0.0.1:5000

Seleccionar productos y comparar precios

Marca los productos que deseas comparar y haz clic en "Comparar Precios".
La aplicación mostrará una tabla con los precios en cada supermercado, recomendando el lugar más barato para comprar cada producto.

Rutas y APIs Disponibles
Mercadona API:

http://127.0.0.1:5001/productos
http://127.0.0.1:5001/producto?nombre=<nombre>
Carrefour API:

http://127.0.0.1:5002/productos
http://127.0.0.1:5002/producto?nombre=<nombre>
LDL API:

http://127.0.0.1:5003/productos
http://127.0.0.1:5003/producto?nombre=<nombre>
Aplicación Principal:

http://127.0.0.1:5000
Mejoras Futuras
Agregar más supermercados y APIs.
Integrar autenticación de usuarios para guardar listas de compras personalizadas.
Mejorar la interfaz de usuario con herramientas como Bootstrap o React.
Implementar una API REST para consultar resultados directamente desde otras aplicaciones.
