<template>
  <!-- Card de exibição das apostas -->
  <section class="p-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-5 w-full">
    <div v-for="(bet) in BetList" :key="bet._id" class="hover:scale-105 transition-transform ease-in-out bg-gradient-to-r from-gray-200 via-white to-gray-100 rounded-lg shadow-lg overflow-hidden">
      <div class="p-6">
        <h2 class="text-xl font-semibold text-gray-900 mb-3">Bet ID: {{ bet._id }}</h2>
        <p class="text-gray-700 mb-3">
          Data da aposta: 
          <span v-if="bet.data" class="font-bold text-gray-800">{{ bet.data }}</span>
          <span v-else class="font-bold text-red-600">Não incluiu Data</span>
        </p>
        
        <p class="text-gray-700 mb-3">
          Horário da aposta: 
          <span v-if="bet.horario" class="font-bold text-gray-800">{{ bet.horario }}</span>
          <span v-else class="font-bold text-red-600">Não incluiu horário</span>
        </p>

        <hr class="my-4 border-gray-300">

        <div class="mb-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Times:</h3>
          <ul class="list-disc pl-5 text-gray-700">
            <li v-for="(time, tIndex) in bet.times" :key="'time-' + bet._id + '-' + tIndex">{{ time }}</li>
          </ul>
        </div>

        <div class="mb-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Participantes:</h3>
          <ul class="list-disc pl-5 text-gray-700">
            <li v-for="(participante, pIndex) in bet.participantes" :key="'participante-' + bet._id + '-' + pIndex">{{ participante }}</li>
          </ul>
        </div>

        <div class="mb-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Tipo de Aposta:</h3>
          <span class="text-gray-800">{{ bet.tipo_aposta }}</span>
        </div>

        <div class="mb-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Palpite:</h3>
          <span v-if="bet.palpites" class="text-gray-800">{{ bet.palpites }}</span>
          <span v-else class="font-bold text-red-600">Não incluiu Palpites</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      BetList: []
    }
  },
  methods: {
    async CardsLoaded() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/data')
        this.BetList = response.data
      } catch (error) {
        console.error('Ocorreu um erro ao obter os dados da API: ', error)
      }
    }
  },
  created() {
    this.CardsLoaded()
  }
}
</script>

<style scoped>
/* Estilos personalizados para o card */
section {
  background: #f5f5f5; 
}

h2, h3 {
  color: #333333; 
}

hr {
  border-top-width: 2px;
  border-top-color: #e5e7eb; 
}
</style>
