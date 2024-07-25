<template>
    <div class="h-screen bg-gray-100 p-6">
      <!-- Título da seção -->
      <div class="text-center mb-10">
        <p class="text-4xl font-bold text-gray-800"> 
          <span class="text-impact">U</span>ltimas Apostas
        </p>
      </div>
  
      <!-- Seção de apostas feitas -->
      <div class="h-96 overflow-y-auto overflow-x-hidden mb-10">
        <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div 
            v-for="bet in BetsList" 
            :key="bet._id"
            class="card-main bg-white shadow-lg rounded-lg overflow-hidden flex flex-col justify-between p-6 transform transition duration-200 hover:scale-105"
          >
            <div class="card-header mb-4">
              <h2 class="text-xl font-semibold text-gray-800">{{ bet.times.join(' vs ') }}</h2>
              <p class="text-sm text-gray-500">{{ new Date(bet.data).toLocaleDateString() }} - {{ bet.horario }}</p>
            </div>
            <div class="card-content flex flex-col">
              <div class="mb-4">
                <h3 class="text-lg font-medium text-gray-700">Participantes:</h3>
                <ul class="list-disc ml-5">
                  <li v-for="(participant, idx) in bet.participantes" :key="idx" class="text-gray-600">{{ participant }}</li>
                </ul>
              </div>
              <div>
                <h3 class="text-lg font-medium text-gray-700">Tipos de Aposta:</h3>
                <ul class="list-disc ml-5">
                  <li v-for="(type, idx) in bet.tipo_aposta" :key="idx" class="text-gray-600">{{ type }}</li>
                </ul>
              </div>
            </div>
          </div>
        </section>
      </div>
  
      <!-- Seção de fazer apostas -->
      <div class="bg-rose-600 w-full text-white font-semibold rounded-lg p-6">
        <div class="text-center mb-6">
          <p class="text-4xl font-bold"> 
            <span class="text-impact">F</span>azer Apostas
          </p>
        </div>
        <div class="bg-white rounded-lg shadow-md p-6 text-gray-800">
          <!-- Formulário de aposta pode ser adicionado aqui -->
          <form @submit.prevent="submitBet">
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Data</label>
              <input type="date" v-model="newBet.data" class="mt-1 p-2 w-full border rounded-md">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Times</label>
              <input type="text" v-model="newBet.times" placeholder="Time A vs Time B" class="mt-1 p-2 w-full border rounded-md">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Participantes</label>
              <input type="text" v-model="newBet.participantes" placeholder="Participante A, Participante B" class="mt-1 p-2 w-full border rounded-md">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Tipo de Aposta</label>
              <select v-model="newBet.tipo_aposta" class="mt-1 p-2 w-full border rounded-md">
                <option value="Quem ganha">Quem ganha</option>
                <option value="Quem perde">Quem perde</option>
                <option value="Mais gols">Mais gols</option>
              </select>
            </div>
            <button type="submit" class="w-full bg-green-600 text-white py-2 rounded-md hover:bg-green-700 transition duration-200">Fazer Aposta</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'BetsComponent',
    data() {
      return {
        BetsList: [],
        newBet: {
          data: '',
          times: '',
          participantes: '',
          tipo_aposta: ''
        }
      };
    },
    created() {
      this.MountCards();
    },
    methods: {
      async MountCards() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/data');
          if (Array.isArray(response.data)) {
            this.BetsList = response.data;
          } else {
            console.error('Dados da resposta não são um array');
          }
        } catch (error) {
          console.error('Erro ao buscar dados:', error);
        }
      },
      async submitBet() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/data', this.newBet);
          console.log('Aposta realizada com sucesso:', response.data);
          this.BetsList.push(response.data);
          this.newBet = {
            data: '',
            times:'',
            participantes: '',
            tipo_aposta: ''
          };
        } catch (error) {
          console.error('Erro ao realizar aposta:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .card-main {
    transition: transform 0.2s;
  }
  .card-main:hover {
    transform: scale(1.05);
  }
  .card-header {
    border-bottom: 1px solid #e2e8f0;
  }
  .text-impact {
    color: black;
  }
  </style>
  