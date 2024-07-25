<template>
<div class="items-center flex flex-col">
    <span class="text-3xl font-semibold"><strong class="text-decoration">Ú</strong>ltimas Apostas Feitas</span>
    <div class="mt-5 shadow-2xl flex flex-col items-center h-96 overflow-y-auto">
        
        <TopBetComponent class="mt-5 "/>
    </div>
</div>
</template>

<script>
import TopBetComponent from '../components/TopBetComponent.vue'

export default {
    components:{
        TopBetComponent
    }
}
</script>
<style scoped>
.text-decoration{
    color: #FF0096;
}
</style>