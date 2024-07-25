<template>
  <!-- Card de exibição das apostas -->
  <section class=" p-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-5">
    <div v-for="(bet) in BetList" :key="bet._id" class="hover:scale-105 transition-all easy-in-out bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="p-4 ">
        <h2 class="text-xl font-semibold text-gray-800 mb-2">Bet ID: {{ bet._id }}</h2>
        <p class="text-gray-600 mb-2">Data da aposta: 
          <span v-if="bet.data"><span class="font-bold">{{ bet.data }}</span></span>
          <span v-else><span class="font-bold text-rose-600">Não incluiu Data</span></span>

        </p>
        
        <p class="text-gray-600 mb-2">Horário da aposta: 
          <span v-if="bet.horario"><span class="font-bold">{{ bet.horario }}</span></span>
          <span v-else><span class="font-bold text-rose-600">Não incluiu horário</span></span>
        </p>

        <hr class="my-4">

        <div>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Times:</h3>
          <ul class="list-disc pl-5 text-gray-600">
            <li v-for="(time, tIndex) in bet.times" :key="'time-' + bet._id + '-' + tIndex">{{ time }}</li>
          </ul>
        </div>

        <div class="mt-4">
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Participantes:</h3>
          <ul class="list-disc pl-5 text-gray-600">
            <li v-for="(participante, pIndex) in bet.participantes" :key="'participante-' + bet._id + '-' + pIndex">{{ participante }}</li>
          </ul>
        </div>

        <div class="mt-4">
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Tipo de Aposta:</h3>
          <ul class="list-disc pl-5 text-gray-600">
            <li v-for="(tipo, tpIndex) in bet.tipo_aposta" :key="'tipo-' + bet._id + '-' + tpIndex">{{ tipo }}</li>
          </ul>
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

<style>
</style>
