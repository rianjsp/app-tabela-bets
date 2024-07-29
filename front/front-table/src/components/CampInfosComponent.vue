<template>
    <section class="flex flex-col items-center py-10 animate__animated animate__backInRight">

      <!-- Card section -->
      <div v-if="camp_name" class="cardMain w-full max-w-4xl bg-white shadow-lg rounded-lg p-8">
        <div class="text-center mb-6">
          <h1 class="text-3xl font-bold text-green-900 mb-2">{{ camp_name.nome_popular }}</h1>
          <p class="text-gray-700 text-base">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deserunt quod cumque repellat consequuntur quae alias dolores dolore enim, deleniti aperiam nesciunt assumenda error, excepturi blanditiis ipsa exercitationem ad ex. Atque!</p>
        </div>
        <div class="flex justify-center mb-6">
          <img :src="camp_name.logo" alt="Logo" class="w-32 h-32 object-cover rounded-full border-2 border-green-500">
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-100">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Rodada</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Edição Atual</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Temporada</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Abrangência</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Tipo</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.rodada_atual.nome }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.edicao_atual.slug }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.edicao_atual.temporada }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.regiao }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.tipo }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ camp_name.status }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div v-else class="text-center mt-10">
        <p class="text-gray-500 text-lg">Carregando informações do campeonato...</p>
      </div>
    </section>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        camp_name: null
      };
    },
    methods: {
      async CreateCampInfo() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/campeonato');
          this.camp_name = response.data.campeonato;
          console.log(this.camp_name);
        } catch (error) {
          console.error('Erro ao carregar as informações do campeonato:', error);
          this.camp_name = null;
        }
      }
    },
    created() {
      this.CreateCampInfo();
    }
  }
  </script>
  
  <style scoped>
  .cardMain {
    max-width: 800px;
  }
  </style>
  