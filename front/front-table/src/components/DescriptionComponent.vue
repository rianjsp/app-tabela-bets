<template>
    <div class="background">
        <div class="card flex flex-row  items-center justify-around">
            

                <div >
                    <h3 class="font-bold text-white">Vivêncie o melhor das apostas com seus <strong class="text-green-200">Amigos</strong>!</h3>
                    <div class="text-white">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus dolore non temporibus similique eum magni asperiores molestias iusto, quibusdam minima minus distinctio cupiditate nihil ab. A vitae quas magni fugit.</p>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem deserunt tempora modi totam quasi quaerat excepturi ea, nulla, sequi illo est labore explicabo laborum fugiat eos delectus quidem iste minima!</p>
                    </div>
                    <div class="mt-4">
                        <ButtonComponent :msg="'Mais Detalhes'" to="/about" />
                    </div>
                </div>
                <div>
                    <img src="../assets/photoJogador.png" alt="Tabela.bets" width="300px">
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
.card{
    display: flex;
    flex-wrap: wrap;
}

@media screen and (min-width: 1211px) {
    .card{
        flex-wrap: nowrap;
    }
}
</style>