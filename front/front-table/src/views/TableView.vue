<template>
    <div class="w-screen h-full flex flex-col gap-9 items-center justify-center">
      
      <TableComponent/>
      
    </div>
  </template>
  
  <script lang="ts">
  import { Options, Vue } from 'vue-class-component';
  import TableComponent from '../components/TableComponent.vue'

  @Options({
    components: {
      TableComponent
      
    },
  })
  export default class TableView extends Vue {}
  </script>
  
  <style>
  
  </style>