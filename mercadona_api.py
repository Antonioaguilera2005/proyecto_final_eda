from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Cargar datos de productos
with open("datos.eda/mercadona.json.json", "r") as f:
    productos = json.load(f)

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API de Mercadona",
        "rutas": {
            "/productos": "Devuelve la lista de productos",
            "/producto?nombre=<nombre>": "Busca un producto por su nombre (reemplaza <nombre>)"
        }
    })

@app.route("/producto", methods=["GET"])
def obtener_producto():
    """Busca un producto específico por su nombre."""
    nombre = request.args.get("nombre")  # Obtener el parámetro `nombre` de la URL
    if not nombre:
        return jsonify({"error": "El parámetro 'nombre' es obligatorio"}), 400
    # Buscar el producto por nombre
    for producto in productos:
        if producto["producto"].lower() == nombre.lower():  # Comparar ignorando mayúsculas/minúsculas
            return jsonify(producto)  # Si se encuentra, devolver los datos del producto
    return jsonify({"error": "Producto no encontrado"}), 404  # Si no se encuentra, devolver error 404
    
@app.route("/productos", methods=["GET"])
def obtener_productos():
    """Devuelve la lista de productos disponibles"""
    return jsonify(productos)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
