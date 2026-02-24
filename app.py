from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

status_dispositivo = {
    "distancia": 100.0,
    "led_verde": False,
    "led_amarelo": False,
    "led_vermelho": False,
    "buzzer": False,
    "bateu": False
}

@app.route('/')
def index():
    """Rota principal que carrega a interface do simulador."""
    return render_template('index.html')

@app.route('/atualizar_sensor', methods=['POST'])
def atualizar_sensor():
    """
    Simula o processamento do MicroPython no ESP32.
    Recebe a distância do 'sensor' (frontend) e decide o estado dos atuadores.
    """
    try:
        dados = request.json
        distancia = float(dados.get('distancia', 100))
        
        status_dispositivo["distancia"] = distancia
        
        status_dispositivo["led_verde"] = distancia > 50
        status_dispositivo["led_amarelo"] = 20 < distancia <= 50
        status_dispositivo["led_vermelho"] = distancia <= 20
        
        status_dispositivo["buzzer"] = distancia <= 10
        
        if distancia <= 2.5:
            status_dispositivo["bateu"] = True
        else:
            status_dispositivo["bateu"] = False

        return jsonify(status_dispositivo)

    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)