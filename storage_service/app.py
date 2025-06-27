from flask import Flask, request, jsonify

app = Flask(__name__)
datos_por_barrio = {}

@app.route('/guardar', methods=['POST'])
def guardar():
    data = request.get_json()
    barrio = data['barrio']

    if barrio not in datos_por_barrio:
        datos_por_barrio[barrio] = []
    datos_por_barrio[barrio].append(data)

    print(f"Guardado en {barrio}: {data}")
    return jsonify({"status": "guardado"})

@app.route('/barrio/<barrio>', methods=['GET'])
def obtener_datos(barrio):
    return jsonify(datos_por_barrio.get(barrio, []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
