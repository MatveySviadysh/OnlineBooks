<template>
  <div id="app">
    <splash-screen />
    <AppHeader />
    <nav>
      <router-link to="/">Главная</router-link> |
      <router-link to="/login">Вход</router-link> |
      <router-link to="/register">Регистрация</router-link> |
      <router-link to="/authors">Авторы</router-link> |
      <router-link to="/profile">Профиль</router-link>
    </nav>
    
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>

    <AppFooter />
  </div>
</template>

<script lang="ts">
  import { defineComponent } from 'vue'
  import SplashScreen from '@/components/help/SplashScreen.vue'
  import AppFooter from '@/components/layout/Footer.vue'
  import AppHeader from '@/components/layout/Header.vue'
  
  export default defineComponent({
    name: 'App',
    components: {
      SplashScreen,
      AppFooter,
      AppHeader
    }
  })
</script>

<style lang="scss">
nav {
  padding: 30px;
  background-color: #f8f9fa;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  
  a {
    font-weight: bold;
    color: #2c3e50;
    text-decoration: none;
    margin: 0 10px;
    padding: 5px 10px;
    border-radius: 4px;
    transition: all 0.3s ease;
    
    &.router-link-exact-active {
      color: #42b983;
      background-color: rgba(66, 185, 131, 0.1);
    }

    &:hover {
      color: #42b983;
    }
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
