<template>
    <router-link :to="to" class="rounded border-2 p-2 m-2 cursor-pointer text-white font-semibold hover:bg-rose-400 hover:text-black transition-all ease-in-out active:scale-102">
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
  
  <style scoped>
  router-link {
      display: inline-block;
      text-decoration: none;
      background-color: #A729A5;
      border-radius: 8px;
      padding: 8px;
      margin: 4px;
  }
  
  router-link:hover {
      background-color: #D63C6E;
      color: #000;
  }
  </style>
  