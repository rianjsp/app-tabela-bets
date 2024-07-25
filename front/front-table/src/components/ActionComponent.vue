<template>
    <div class="background">
        <div class="flex flex-row">
            <div>
                <div>
                    <img src="../assets/icons/1-Photoroom.png" alt="Tabela.bets" width="900px">
                </div>
                
                <div class="btDesciption">
                        <ButtonComponent :msg="'Tabela'" to="/table" />
                        <ButtonComponent :msg="'Bets '" to="/bets"/>
                </div>

            </div>
            <div class="description">
                <div class="text-description text-white">
                    <h3 class="font-bold">Veja a tabela do seu <strong class="text-green-200">Campeonato</strong></h3>
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nesciunt suscipit repellat nostrum corporis laudantium inventore. Assumenda deleniti illum blanditiis quam eligendi. Distinctio ratione deleniti iusto nesciunt rem culpa ab vel.</p>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, magnam animi perspiciatis asperiores, iure voluptatum explicabo alias quia fuga aliquid maiores dolore beatae officia ad perferendis ullam impedit sequi. Consectetur.</p>
                </div>
                <div class="flex flex-col justify-center items-center">
                    <img src="../assets/jogadores-removebg-preview.png" alt="jogadores" width="300px">
                    <div>
                        <ButtonComponent :msg="'Bets'" to="/bets"/>
                        <ButtonComponent :msg="'Campeonato Brasileiro - Serie A'" to="/table"/>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import ButtonComponent from './buttons/ButtonComponent.vue'

export default {
    components:{
        ButtonComponent
    }
}
</script>

<style scoped>
.background{
    background-color: #4F345A;
    padding: 50px;
    width: 90%;
    border-radius: 20px;
}
.description{
    margin-left: 50px;
    font-size: 1.2rem;
    display: none;
    text-align: center;
    align-items: center;

}

@media screen and (min-width: 1211px) {
    .description{
        display: block;
    }
    .btDesciption{
        display: none;
    }
}
</style>