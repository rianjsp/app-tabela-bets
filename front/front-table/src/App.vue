<template>
  <nav class="font-semibold pt-10">
    <router-link class="nav-link" to="/">HOME</router-link>
    <router-link class="nav-link" to="/about">ABOUT</router-link>
    <router-link class="nav-link" to="/bets">BETS</router-link>
  </nav>
  <router-view/>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.nav-link {
  padding: 0.5rem 1rem;
  color: #2c3e50;
  text-decoration: none;
  transition: color 0.3s, transform 0.3s;
}

.nav-link:hover {
  color: #FF0096;
  transform: scale(1.05);
}

nav a.router-link-exact-active {
  color: #FF0096;
  font-weight: bold;
}
footer{
  color: #FF0096;
}
:root {
  --animate-duration: 800ms;
  --animate-delay: 0.9s;
}
</style>
