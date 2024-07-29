<template>
  <div class="min-h-screen bg-gradient-to-r from-gray-200 via-gray-300 to-green-200 flex flex-col items-center justify-center p-4 rounded-xl">
    <!-- Tabela -->
    <div class="text-center mb-6">
      <h1 class="text-3xl font-bold text-green-900 border-b-2 border-green-900 pb-2">Tabela</h1>
    </div>

    <table class="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
      <thead class="bg-gray-100">
        <tr>
          <th class="py-2 px-4 text-left">Escudo</th>
          <th class="py-2 px-4 text-left">Nome</th>
          <th class="py-2 px-4 text-left">Aproveitamento</th>
          <th class="py-2 px-4 text-left">Jogos</th>
          <th class="py-2 px-4 text-left">Pontos</th>
          <th class="py-2 px-4 text-left">Derrotas</th>
          <th class="py-2 px-4 text-left">Empates</th>
          <th class="py-2 px-4 text-left">Vitórias</th>
          <th class="py-2 px-4 text-left">Gols <strong class="text-green-600">Pro</strong></th>
          <th class="py-2 px-4 text-left">Gols <strong class="text-red-600">Contra</strong></th>
          <th class="py-2 px-4 text-left">Saldo de Gols</th>
          <th class="py-2 px-4 text-left">Últimos Jogos</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in table" :key="item.id" class="hover:bg-gray-50">
          <td class="py-3 px-4">
            <img :src="item.time.escudo" alt="Escudo" class="w-10 h-10 object-cover rounded-full">
          </td>
          <td class="py-3 px-4">{{ item.time.nome_popular }}</td>
          <td class="py-3 px-4">{{ item.aproveitamento }}%</td>
          <td class="py-3 px-4">{{ item.jogos }}</td>
          <td class="py-3 px-4">{{ item.pontos }}</td>
          <td class="py-3 px-4">{{ item.derrotas }}</td>
          <td class="py-3 px-4">{{ item.empates }}</td>
          <td class="py-3 px-4">{{ item.vitorias }}</td>
          <td class="py-3 px-4">{{ item.gols_pro }}</td>
          <td class="py-3 px-4">{{ item.gols_contra }}</td>
          <td class="py-3 px-4">{{ item.saldo_gols }}</td>
          <td class="py-3 px-4">
            <span class="flex justify-center space-x-1">
              <span v-for="(jogo, index) in item.ultimos_jogos" :key="index" class="inline-block">
                <i :class="['fa-solid fa-circle', {
                  'text-green-600': jogo === 'v',
                  'text-gray-500': jogo === 'e',
                  'text-red-600': jogo === 'd'
                }]" ></i>
              </span>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      table: []
    };
  },
  created() {
    this.BuscarDados();
  },
  methods: {
    async BuscarDados() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/table');
        this.table = response.data.tabela;
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    }
  }
};
</script>

<style scoped>
.text-green-900 {
  color: #15803d;
}
.text-yellow-900 {
  color: #ffbc5e;
}
.text-red-900 {
  color: #b91c1c;
}
</style>
