from flask import Flask, jsonify, request  # Importar request aqui
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import requests
import os

# Carregar variáveis de ambiente
load_dotenv()

# Instanciamento da aplicação
app = Flask(__name__)
CORS(app)

# Configuração do MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_default_database()
collection = db.bets  # Supondo que a coleção se chama 'bets'

# Inicialização do header contendo a chave
api_key = os.getenv("API_KEY")
url = os.getenv("URI_API")

header = {
    "Authorization": f'Bearer {api_key}'
}

# Função para fazer a requisição
def fetch_data():
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()  # Lança um erro para códigos de status HTTP >= 400
        data = response.json()
        print('Conteúdo retornado com sucesso!')
        return data
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro na requisição: {e}')
        return None

# Fazer a requisição e armazenar os dados
data = fetch_data()
if data:
    result = data
else:
    result = {}

# Inicialização dos endpoints
@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find())
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['POST'])
def post_data():
    try:
        data_bet = request.form.get('data')
        times_bet = request.form.getlist('times')
        participantes_bet = request.form.getlist('participantes')
        tipo_aposta_bet = request.form.getlist('tipo_aposta')

        # Criando a nova aposta
        new_bet = {
            "data": data_bet,
            "times": times_bet,
            "participantes": participantes_bet,
            "tipo_aposta": tipo_aposta_bet
        }

        # Inserção no MongoDB
        result = collection.insert_one(new_bet)

        # Verificação do resultado da inserção
        if result.acknowledged:
            return jsonify({"message": "Aposta registrada com sucesso!", "id": str(result.inserted_id)}), 201
        else:
            return jsonify({"error": "Erro ao registrar aposta"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/table', methods=['GET'])
def table():
    if result:
        return jsonify({"tabela": result.get('tabela', [])})
    return jsonify({"error": "Dados não encontrados"}), 404

@app.route('/campeonato', methods=['GET'])
def campeonato():
    if result:
        return jsonify({"campeonato": result.get('campeonato', {})})
    return jsonify({"error": "Dados não encontrados"}), 404

@app.route('/partidas', methods=['GET'])
def partidas():
    if result:
        return jsonify({"partidas": result.get('partidas', [])})
    return jsonify({"error": "Dados não encontrados"}), 404

if __name__ == '__main__':
    app.run(debug=True)
