<template>
<div class="items-center  flex flex-col justify-center animate__animated animate__backInRight">

    <div class="w-3/4 flex flex-col">
        <span class="text-3xl items-center flex justify-center text-center font-semibold mt-5"><strong class="text-decoration">R</strong>ealizar Aposta</span>
        <div class="h-full">

            <DownBetComponent class="mt-5" />
        </div>
    </div>

<div class="w-2/2 mb-10 betView animate__animated animate__backInUp">

    <span class="text-3xl font-semibold items-center flex justify-center text-center font-semibold mt-5"><strong class="text-decoration">Ú</strong>ltimas Apostas Feitas</span>
    <div class="topbet rounded-xl mt-5 shadow-2xl flex flex-col items-center overflow-y-auto border-rose-600 mx-20">
        
        <TopBetComponent class="mt-5 "/>
        
    </div>

</div>
</div>
</template>

<script>
import DownBetComponent from '@/components/betComponent/DownBetComponent.vue';
import TopBetComponent from '@/components/betComponent/TopBetComponent.vue'

export default {
    components:{
        TopBetComponent,
        DownBetComponent
    }
}
</script>
<style scoped>
.text-decoration{
    color: #FF0096;
}
.topbet{
    height: 600px !important;
}
</style>