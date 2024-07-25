<template>
  <div class="w-screen h-full flex flex-col gap-9 items-center justify-center">
    
    <ActionComponent/>
    <DescriptionComponent/>
    
    
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

import ActionComponent from '../components/ActionComponent.vue'
import DescriptionComponent from '../components/DescriptionComponent.vue'

@Options({
  components: {
    DescriptionComponent,
    ActionComponent
  },
})
export default class HomeView extends Vue {}
</script>

<style>

</style>