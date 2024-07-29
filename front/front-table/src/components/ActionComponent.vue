<template>
    <div class="bg-purple-900 p-12 rounded-lg w-11/12 mx-auto">
      <div class="flex flex-col md:flex-row items-center">
        <div class="md:w-1/2 flex flex-col items-center md:items-start">
          <div>
            <img src="../assets/icons/1-Photoroom.png" alt="Tabela.bets" class="w-full max-w-2xl">
          </div>
          <div class="flex flex-col md:flex-row gap-4 mt-4">
            <ButtonComponent :msg="'Tabela'" to="/table" />
            <ButtonComponent :msg="'Bets'" to="/bets" />
          </div>
        </div>
        <div class="md:w-1/2 mt-8 md:mt-0 md:ml-12 text-white text-center md:text-left">
          <div class="text-description">
            <h3 class="font-bold text-2xl">
              Veja a tabela do seu <strong class="text-green-200">Campeonato</strong>
            </h3>
            <p class="mt-4">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nesciunt suscipit repellat nostrum corporis laudantium inventore. Assumenda deleniti illum blanditiis quam eligendi. Distinctio ratione deleniti iusto nesciunt rem culpa ab vel.</p>
            <p class="mt-2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, magnam animi perspiciatis asperiores, iure voluptatum explicabo alias quia fuga aliquid maiores dolore beatae officia ad perferendis ullam impedit sequi. Consectetur.</p>
          </div>
          <div class="flex flex-col items-center mt-8">
            <img src="../assets/jogadores-removebg-preview.png" alt="jogadores" class="w-72">
            <div class="flex flex-col md:flex-row gap-4 mt-4">
              <ButtonComponent :msg="'Bets'" to="/bets" />
              <ButtonComponent :msg="'Campeonato Brasileiro - Serie A'" to="/table" />
            </div>
          </div>
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

  