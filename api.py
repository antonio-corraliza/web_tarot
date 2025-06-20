from flask import Flask, request, jsonify, render_template
import random
import json
import os

app = Flask(__name__)

# Cargar las cartas desde el archivo JSON
with open(os.path.join(os.path.dirname(__file__), "card_data.json"), encoding="utf-8") as f:
    data = json.load(f)
    cartas = data["cards"]  # <-- Aquí accedes a la lista de cartas

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cartas")
def obtener_cartas():
    cantidad = int(request.args.get("cantidad", 3))
    seleccionadas = random.sample(cartas, min(cantidad, len(cartas)))
    return jsonify(seleccionadas)

if __name__ == "__main__":
    app.run(debug=True, port=8000)