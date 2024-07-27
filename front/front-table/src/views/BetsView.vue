<template>
<div class="items-center flex flex-col">

    <div class="w-1/2">
        <span class="text-3xl items-center flex justify-center text-center font-semibold mt-5"><strong class="text-decoration">R</strong>ealizar Aposta</span>
        <div class="h-full">

            <DownBetComponent class="mt-5" />
        </div>
    </div>

<div class="w-2/2 mb-10 ">

    <span class="text-3xl font-semibold items-center flex justify-center text-center font-semibold mt-5"><strong class="text-decoration">Ú</strong>ltimas Apostas Feitas</span>
    <div class="rounded-xl mt-5 shadow-2xl flex flex-col items-center h-96 overflow-y-auto border-rose-600 mx-20">
        
        <TopBetComponent class="mt-5 "/>
        
    </div>

</div>
</div>
</template>

<script>
import DownBetComponent from '@/components/DownBetComponent.vue';
import TopBetComponent from '../components/TopBetComponent.vue'

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
</style>