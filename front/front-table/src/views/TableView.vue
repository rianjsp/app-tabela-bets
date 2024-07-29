<template>
  <div class="w-full h-full flex flex-col gap-9 items-center justify-center">
    <CampInfosComponent/>
    <TableComponent class="animate__animated animate__backInLeft" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import TableComponent from '../components/TableComponent.vue';
import CampInfosComponent from '../components/CampInfosComponent.vue';


@Options({
  components: {
    TableComponent,
    CampInfosComponent
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
