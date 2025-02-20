from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
nombres = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['POST'])
def agregar_nombre():
    nombre = request.json.get('nombre')
    if nombre:
        nombres.append(nombre)
        return jsonify({"mensaje": "Nombre agregado"})
    return jsonify({"error": "No se recibió un nombre"}), 400

@app.route('/mostrar', methods=['GET'])
def mostrar_nombres():
    return jsonify(nombres)

if __name__ == '__main__':
    app.run(debug=True)
