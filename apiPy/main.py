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
        data_list = list(collection.find())
        for item in data_list:
            item["_id"] = str(item["_id"])  # Converte ObjectId para string
        return jsonify(data_list)
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
