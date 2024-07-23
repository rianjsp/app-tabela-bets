# Inicialização do projeto
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

# Instanciamento da aplicação
app = Flask(__name__)
load_dotenv()
CORS(app)


# Inicialização do header contendo a chave
api_key = os.getenv("API_KEY")
url = os.getenv("URI_API")


header = {
        "Authorization": f'Bearer {api_key}'
}

# Realizando a request
response = requests.get(url, headers=header)


if response.status_code == 200:
    data = response.json()
    result = data
    
    print('Conteudo retornado com sucesso!')

elif response.status_code == 404 or response.status_code == 400:
    print('Não conseguiu retorno da api')

else:
    print(f'Ocorreu um erro na requisição: {response.status_code}')
    print(response.text)



# Inicialização do endpoint -> TABELA
@app.route('/table')
def Table():
    return {
        "tabela": result['tabela']
    }


# Inicialização do endpoint -> CAMPEONATO
@app.route('/campeonato')
def Campeonato():
    return {
        "campeonato": result['campeonato']
    }


# Inicialização do endpoint -> PARTIDAS
@app.route('/partidas')
def Partidas():
    return{
        "partidas": result['partidas']
    }


if __name__ == '__main__':
    app.run(debug=True)