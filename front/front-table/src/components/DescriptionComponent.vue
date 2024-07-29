<template>
    <div class="bg-purple-900 p-12 rounded-lg w-11/12 mx-auto">
      <div class="flex flex-col md:flex-row items-center justify-around space-y-8 md:space-y-0">
        <div class="md:w-1/2 text-white text-center md:text-left">
          <h3 class="font-bold text-2xl mb-4">
            Vivencie o melhor das apostas com seus <strong class="text-green-200">Amigos</strong>!
          </h3>
          <p class="mb-4">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus dolore non temporibus similique eum magni asperiores molestias iusto, quibusdam minima minus distinctio cupiditate nihil ab. A vitae quas magni fugit.
          </p>
          <p class="mb-4">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem deserunt tempora modi totam quasi quaerat excepturi ea, nulla, sequi illo est labore explicabo laborum fugiat eos delectus quidem iste minima!
          </p>
          <ButtonComponent :msg="'Mais Detalhes'" to="/about" class="mt-4" />
        </div>
        <div class="md:w-1/2 flex justify-center">
          <img src="../assets/photoJogador.png" alt="Tabela.bets" class="w-full max-w-md">
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import ButtonComponent from './buttons/ButtonComponent.vue';
  
  export default {
    components: {
      ButtonComponent
    }
  };
  </script>
  