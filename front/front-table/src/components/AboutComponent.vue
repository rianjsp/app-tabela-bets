<template>
  <div class="about-page p-8 bg-white rounded-lg shadow-lg max-w-4xl mx-auto mt-10">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Sobre a Página</h1>
    <p class="mb-6 text-gray-700 leading-relaxed">
      Bem-vindo à nossa página dedicada ao Tabela.bets, um projeto que consome a API Futebol e mostra em tempo real a tabela do Campeonato Brasileiro Série A 2024! Aqui você encontrará informações atualizadas sobre a classificação dos times, incluindo pontos, vitórias, empates, derrotas, gols marcados e sofridos, e muito mais.
    </p>
    <h2 class="text-2xl font-semibold mb-4 text-gray-800">Objetivo</h2>
    <p class="mb-6 text-gray-700 leading-relaxed">
      Nosso objetivo é fornecer uma visão clara e fácil de entender sobre o andamento do campeonato, permitindo que os fãs acompanhem o desempenho de seus times favoritos ao longo da temporada com um simples 'clique'.
    </p>
    <h2 class="text-2xl font-semibold mb-4 text-gray-800">Funcionalidades</h2>
    <ul class="list-disc list-inside mb-6 text-gray-700 leading-relaxed">
      <li>Classificação atualizada em tempo real</li>
      <li>Estatísticas de aproveitamento dos times</li>
      <li>Detalhamento sobre gols, pró/contras, vitórias, derrotas...</li>
      <li>Histórico de jogos e resultados passados</li>
    </ul>
    <h2 class="text-2xl font-semibold mb-4 text-gray-800">Tecnologias Utilizadas</h2>
    <p class="mb-6 text-gray-700 leading-relaxed">
      Esta página foi desenvolvida utilizando as seguintes tecnologias:
    </p>
    <ul class="list-disc list-inside mb-6 text-gray-700 leading-relaxed">
      <li><strong>Frontend:</strong> Vue.js e Tailwind CSS</li>
      <li><strong>Backend:</strong> Python com Flask</li>
      <li><strong>API:</strong> Dados retornados de uma API feita em Python que faz as requisições à: <strong><a href="https://dashboard.api-futebol.com.br/" class="text-green-700 hover:text-green-900">API Futebol <i class="fa-solid fa-circle"></i></a></strong></li>
      <li><strong>Design:</strong> Tailwind CSS para estilização e layout responsivo</li>
    </ul>
    <h2 class="text-2xl font-semibold mb-4 text-gray-800">Contato</h2>
    <p class="text-gray-700 leading-relaxed">
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
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
