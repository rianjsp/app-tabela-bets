<template>
    <div class="about-page p-6 bg-gray-100 h-screen">
      <h1 class="text-3xl font-bold mb-4">Sobre a Página</h1>
      <p class="mb-4">
        Bem-vindo à nossa página dedicada ao Tabela.bets, um projeto que consome a api-futebol e mostra em tempo real a tabela do Campeonato Brasileiro Série A 2024! Aqui você encontrará informações atualizadas sobre a classificação dos times, incluindo pontos, vitórias, empates, derrotas, gols marcados e sofridos, e muito mais.
      </p>
      <h2 class="text-2xl font-semibold mb-3">Objetivo</h2>
      <p class="mb-4">
        Nosso objetivo é fornecer uma visão clara e fácil de entender sobre o andamento do campeonato, permitindo que os fãs acompanhem o desempenho de seus times favoritos ao longo da temporada com um simples 'clique'.
      </p>
      <h2 class="text-2xl font-semibold mb-3">Funcionalidades</h2>
      <ul class="list-disc list-inside mb-4">
        <li>Classificação atualizada em tempo real</li>
        <li>Estatísticas de aproveitamento dos times</li>
        <li>Detalhamento sobre gols, pro/contras, vitorias, derrotas...</li>
        <li>Histórico de jogos e resultados passados</li>
      </ul>
      <h2 class="text-2xl font-semibold mb-3">Tecnologias Utilizadas</h2>
      <p class="mb-4">
        Esta página foi desenvolvida utilizando as seguintes tecnologias:
      </p>
      <ul class="list-disc list-inside mb-4">
        <li><strong>Frontend:</strong> Vue.js e Tailwind CSS</li>
        <li><strong>Backend:</strong> Python com Flask</li>
        <li><strong>API:</strong> Dados retornados de uma API feita em Python onde faz as requisições à: <strong> <a href="https://dashboard.api-futebol.com.br/">Api Futebol <i class="text-green-900 fa-solid fa-circle"></i></a></strong></li>
        <li><strong>Design:</strong> Tailwind CSS para estilização e layout responsivo</li>
      </ul>
      <h2 class="text-2xl font-semibold mb-3">Contato</h2>
      <p>
        Se você tiver alguma dúvida, sugestão ou feedback, sinta-se à vontade para entrar em contato.
      </p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutPage'
  }
  </script>
  
  <style scoped>
  .about-page {
    max-width: 800px;
    margin: 0 auto;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  </style>
  