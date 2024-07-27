from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import requests
import os

# Carregar variáveis de ambiente
load_dotenv()

# Instanciação da aplicação
app = Flask(__name__)
CORS(app)

# Configuração do MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_default_database()
collection = db.bets  

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
        response.raise_for_status()
        data = response.json()
        print('Conteudo retornado com sucesso!')
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
        data_list = list(collection.find())
        for item in data_list:
            item["_id"] = str(item["_id"])  # Converte ObjectId para string
        return jsonify(data_list)
    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/data/post', methods=['POST'])
def post_data():
    try:
        # Receber dados JSON
        data = request.json

        # Validar e processar os dados
        new_bet = {
            "_id": data.get('bet_id'),
            "data": data.get('data'),
            "horario": data.get('horario'),
            "times": data.get('times'),
            "participantes": data.get('participantes'),
            "tipo_aposta": data.get('tipo_aposta'),
            "palpites": data.get('palpites')
        }

        resultado = collection.insert_one(new_bet)
        print('Bet inserida com sucesso')
        return jsonify({"message": "Bet inserida com sucesso", "id": str(resultado.inserted_id)}), 201

    except Exception as e:
        print(f"Erro ao inserir bet: {e}")
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
