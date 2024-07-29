<template>
  <div class="w-screen h-full flex flex-col gap-9 items-center justify-center">
    <TableComponent class="animate__animated animate__backInLeft" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import TableComponent from '../components/TableComponent.vue';

@Options({
  components: {
    TableComponent,
  },
})
export default class TableView extends Vue {}
</script>

<style scoped>
:root {
  --animate-duration: 800ms;
  --animate-delay: 0.9s;
}
</style>
