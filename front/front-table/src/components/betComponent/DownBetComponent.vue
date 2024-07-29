<template>
  <section class="p-10 m-10 bg-white shadow-md rounded-lg w-full max-w-2xl mx-auto">
    <div>
      <fieldset class="space-y-6">
        <form @submit.prevent="getFormValues" method="POST" class="space-y-6">
          <div>
            <label for="data" class="block text-sm font-medium text-gray-700">Data da aposta</label>
            <input
              required
              v-model="data"
              name="data"
              id="data"
              type="date"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            >
          </div>
          
          <div>
            <label for="times" class="block text-sm font-medium text-gray-700">Times</label>
            <input
              required
              v-model="times"
              name="times"
              type="text"
              id="times"
              placeholder="Separe por vírgula os times!"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            >
          </div>
          
          <div>
            <label for="participantes" class="block text-sm font-medium text-gray-700">Participantes</label>
            <input
              required
              v-model="participantes"
              name="participantes"
              type="text"
              id="participantes"
              placeholder="Separe por vírgula os participantes!"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            >
          </div>
          
          <div>
            <label for="tp_aposta" class="block text-sm font-medium text-gray-700">Tipo de aposta</label>
            <select
              required
              v-model="tp_aposta"
              name="tp_aposta"
              id="tp_aposta"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            >
              <option value="Quem_Ganha">Quem Ganha?</option>
              <option value="Quem_Perde">Quem Perde?</option>
              <option value="Mais_Gols">Mais Gols na partida?</option>
            </select>
          </div>

          <div>
            <label for="palpites" class="block text-sm font-medium text-gray-700">Diga os palpites</label>
            <textarea
              required
              v-model="palpites"
              name="palpites"
              id="palpites"
              cols="30"
              rows="5"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            ></textarea>
          </div>
          
          <button
            type="submit"
            @click="reloadPage()"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Enviar
          </button>
        </form>
      </fieldset>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      bet_id: 0,
      data: '',
      horario: '',
      times: '',
      participantes: '',
      tp_aposta: 'Quem_Ganha',
      palpites: ''
    };
  },
  methods: {
    reloadPage() {
      window.location.reload();
    },
    async getFormValues() {
      try {
        const timesArray = this.times.split(',').map(item => item.trim());
        const participantesArray = this.participantes.split(',').map(item => item.trim());
        const timeElapsed = Date.now();
        const today = new Date(timeElapsed);
        this.horario = today.toUTCString();
        this.bet_id = Math.floor(Math.random() * 5000000);
        this.palpites = this.palpites.trim();

        const newBet = {
          bet_id: this.bet_id,
          data: this.data,
          horario: this.horario,
          times: timesArray,
          participantes: participantesArray,
          tipo_aposta: this.tp_aposta,
          palpites: this.palpites
        };

        const response = await axios.post('http://127.0.0.1:5000/data/post', newBet, {
          headers: {
            'Content-Type': 'application/json'
          }
        });

        console.log('Bet inserida com sucesso:', response.data);
        alert('Bet inserida com sucesso!');
      } catch (error) {
        console.error('Erro ao inserir bet:', error.response?.data || error.message);
        alert('Erro ao inserir bet. Tente novamente.');
      }
    }
  }
};
</script>
