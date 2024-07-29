<template>
    <router-link :to="to" class="btn-link inline-block rounded-lg border-2 border-transparent bg-purple-700 text-white font-semibold py-2 px-4 m-2 text-center cursor-pointer hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 transition-transform transform hover:scale-105 active:scale-95">
      {{ msg }}
    </router-link>
  </template>
  
  <script>
  export default {
    props: {
      msg: {
        type: String,
        required: true
      },
      to: {
        type: String,
        required: true
      }
    }
  }
  </script>
