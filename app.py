from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Obtener la lista de productos de los tres supermercados
def obtener_productos(supermercado):
    url = f"http://127.0.0.1:{supermercado}/productos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        # Obtener los productos seleccionados por el usuario
        productos_seleccionados = request.form.getlist("producto")
        return redirect(url_for("comparar", productos=productos_seleccionados))
    
    # Obtener los productos de todos los supermercados
    productos_mercadona = obtener_productos(5001)
    productos_carrefour = obtener_productos(5002)
    productos_ldl = obtener_productos(5003)
    
    # Unir todos los productos en una lista para mostrar al usuario
    productos = set(p["producto"] for p in productos_mercadona + productos_carrefour + productos_ldl)
    
    return render_template("index.html", productos=productos)

@app.route("/comparar", methods=["GET"])
def comparar():
    productos_seleccionados = request.args.getlist("productos")
    
    # Comparar precios (aquí es donde incluirás la lógica de comparación)
    resultados = []
    for producto in productos_seleccionados:
        # Obtén el precio de cada supermercado
        precio_mercadona = obtener_precio(5001, producto)
        precio_carrefour = obtener_precio(5002, producto)
        precio_ldl = obtener_precio(5003, producto)
        
        # Realiza la comparación
        resultado = {
            "producto": producto,
            "mercadona": precio_mercadona,
            "carrefour": precio_carrefour,
            "ldl": precio_ldl,
        }
        resultados.append(resultado)

    # Ordenar los resultados por el precio más bajo para cada producto
    resultados_ordenados = sorted(resultados, key=lambda x: min(x["mercadona"], x["carrefour"], x["ldl"]))

    # Aquí puedes implementar la lógica para guardar en la base de datos si es necesario
    return render_template("resultados.html", resultados=resultados_ordenados)

# Función para obtener el precio de un producto en un supermercado
def obtener_precio(puerto, producto):
    url = f"http://127.0.0.1:{puerto}/producto?nombre={producto}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("precio", "No disponible")
    else:
        return "No disponible"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
