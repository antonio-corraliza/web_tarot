from flask import Flask, request, jsonify, render_template
import random
import json
import os

# Inicializa la aplicación Flask
app = Flask(__name__)

# Carga las cartas desde un archivo JSON al iniciar la aplicación
with open(os.path.join(os.path.dirname(__file__), "card_data.json"), encoding="utf-8") as f:
    data = json.load(f)
    cartas = data["cards"]

def seleccionar_cartas(cantidad):
    """
    Selecciona aleatoriamente una cantidad de cartas del mazo.
    Si la cantidad solicitada es mayor que el número de cartas disponibles,
    devuelve todas las cartas mezcladas.
    """
    return random.sample(cartas, min(cantidad, len(cartas)))

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Ruta principal que muestra el formulario y las cartas seleccionadas.
    Si la petición es POST, obtiene la cantidad de cartas solicitadas y las selecciona.
    Renderiza la plantilla 'index.html' pasando las cartas seleccionadas y la cantidad.
    """
    cartas_seleccionadas = []
    cantidad = 3  # valor por defecto
    if request.method == "POST":
        cantidad = int(request.form.get("cantidad", 3))
        cartas_seleccionadas = seleccionar_cartas(cantidad)
    return render_template("index.html", cartas=cartas_seleccionadas, cantidad=cantidad)

@app.route("/cartas")
def obtener_cartas():
    """
    Ruta API que devuelve una cantidad de cartas seleccionadas en formato JSON.
    La cantidad se obtiene del parámetro de consulta 'cantidad'.
    """
    cantidad = int(request.args.get("cantidad", 3))
    seleccionadas = seleccionar_cartas(cantidad)
    return jsonify(seleccionadas)

if __name__ == "__main__":
    app.run(debug=True, port=8000)