
# `Tabela.bets`

Tabela.bets é um aplicativo divertido para você e seus amigos competirem em apostas fictícias de futebol.

Nota: Este aplicativo é destinado exclusivamente para diversão entre amigos e familiares. Não incentivamos o uso de dinheiro real em apostas.

# `Sobre`

Criado utilizando Vue.js e Python, o aplicativo conta com uma API desenvolvida em Flask para fornecer endpoints que podem ser consumidos por outras tecnologias. O Flask é conhecido por sua simplicidade, e combinado com a forma eficiente de manipulação de dados do Vue.js, criamos um aplicativo fácil de usar e divertido.

Apesar de ser simples, o Tabela.bets oferece acesso às tabelas dos principais campeonatos de futebol do Brasil e permite acompanhar em tempo real os placares das partidas em andamento.


# `Tecs Utilizadas`

![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)


## `API's`

#### PRINCIPAIS ENDPOINTS DA API-PYTHON

```http
  GET /data
  POST /data/post
  GET /table
  GET /campeonato
  GET /partidas
```

### RESUMO

```
  1° Óbtem todos os tickets bet feitos no banco de dados.
  2° Realiza a criação dos tickets no banco de dados.
  3° Óbtem a tabela do campeonato apresentado 'Brasileirão 2024 - Série A'.
  4° Óbtem as informações relacionados ao Campeonato apresentado 'Brasileirão 2024 - Série A'.
  5° Óbtem informações sobre as partidas do Campeonato apresentado 'Brasileirão 2024 - Série A'.
```

#### API DE REFERENCIA UTILIZADA PARA O PYTHOM TRANSMITIR 
`https://dashboard.api-futebol.com.br/`
```http
    GET https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela
    GET https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}
    etc...
```


### WORKING ON PROGRESS
