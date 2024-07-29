<template>
  <div class="w-screen h-full flex flex-col gap-9 items-center justify-center">
    <ActionComponent class="animate__animated animate__backInUp"/>
    <DescriptionComponent class="animate__animated animate__backInUp"/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import ActionComponent from '../components/ActionComponent.vue';
import DescriptionComponent from '../components/DescriptionComponent.vue';

@Options({
  components: {
    ActionComponent,
    DescriptionComponent,
  },
})
export default class HomeView extends Vue {}
</script>

<style scoped>
:root {
  --animate-duration: 800ms;
  --animate-delay: 0.9s;
}
</style>
