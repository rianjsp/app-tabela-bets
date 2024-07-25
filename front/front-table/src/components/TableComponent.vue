<template>
    <div class="min-h-screen from-purple-200 via-purple-300 to-purple-500 flex flex-col items-center justify-center p-4">
      
      <div class="table-name text-bold">
        <h1 class="m-5 text-3xl text-semibold text-green-900 border-b  border-b-rose-900">Brasileirão</h1>
      </div>

      <table class="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead class="bg-green-300">
          
          <tr>
            <th class="py-1 px-2">Escudo</th>
            <th class="py-1 px-2">Nome</th>
            <th class="py-1 px-2">Aproveitamento</th>
            <th class="py-1 px-2">Jogos</th>
            <th class="py-1 px-2">Pontos</th>
            <th class="py-1 px-2">Derrotas</th>
            <th class="py-1 px-2">Empates</th>
            <th class="py-1 px-2">Vitórias</th>
            <th class="py-1 px-2">Gols <strong class="text-green-900">Pro</strong></th>
            <th class="py-1 px-2">Gols <strong class="text-rose-900">Contra</strong></th>
            <th class="py-1 px-2">Saldo de Gols</th>
            <th class="py-1 px-2">Últimos Jogos</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in table" :key="item.id" class="hover:bg-purple-100">
            <td class="py-2 px-4">
              <img :src="item.time.escudo" alt="Escudo" width="40px">
            </td>
            <td class="py-2 px-4">{{ item.time.nome_popular }}</td>
            <td class="py-2 px-4">{{ item.aproveitamento }}%</td>
            <td class="py-2 px-4">{{ item.jogos }}</td>
            <td class="py-2 px-4">{{ item.pontos }}</td>
            <td class="py-2 px-4">{{ item.derrotas }}</td>
            <td class="py-2 px-4">{{ item.empates }}</td>
            <td class="py-2 px-4">{{ item.vitorias }}</td>
            <td class="py-2 px-4">{{ item.gols_pro }}</td>
            <td class="py-2 px-4">{{ item.gols_contra }}</td>
            <td class="py-2 px-4">{{ item.saldo_gols }}</td>
            <td class="py-2 px-4">
              <span class="m-1" v-for="(jogo, index) in item.ultimos_jogos" :key="index" >
                <span v-if="jogo === 'v'">
                  <i class="text-green-900 fa-solid fa-circle"></i>
                </span>
                <span v-else-if="jogo === 'e'">
                  <i class="text-yellow-900 fa-solid fa-circle"></i>
                </span>
                <span v-else>
                  <i class="text-red-900 fa-solid fa-circle"></i>
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
    components: {
      
    },
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
  
  <style>
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
  