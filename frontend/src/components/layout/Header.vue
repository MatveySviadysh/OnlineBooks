<template>
  <!-- Добавляем top-bar перед main-header -->
  <div class="top-bar">
    <div class="top-bar-content">
      <div class="top-links">
        <a href="/store-locator">Find a Store</a>
        <a href="/contact">Contact Us</a>
        <a href="/exhibitions">Current Exhibitions</a>
      </div>
    </div>
  </div>
  
  <header class="main-header">
    <!-- Боковая панель меню -->
    <div class="side-menu" :class="{ 'is-open': isMenuOpen }">
      <div class="menu-header">
        <button class="close-menu" @click="toggleMenu">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <nav class="menu-links">
        <a href="#" class="menu-link">Text 1</a>
        <a href="#" class="menu-link">Text 2</a>
        <a href="#" class="menu-link">Text 3</a>
        <a href="#" class="menu-link">Text 4</a>
        <a href="#" class="menu-link">Text 5</a>
        <a href="#" class="menu-link">Text 6</a>
        <a href="#" class="menu-link">Text 7</a>
        <a href="#" class="menu-link">Text 8</a>
        <a href="#" class="menu-link">Text 9</a>
        <a href="#" class="menu-link">Text 10</a>
      </nav>
    </div>

    <!-- Затемнение фона при открытом меню -->
    <div class="menu-overlay" :class="{ 'is-visible': isMenuOpen }" @click="toggleMenu"></div>

    <div class="header-content">
      <!-- Левая часть -->
      <div class="left-actions">
        <div class="menu-wrapper" @click="toggleMenu">
          <i class="fas fa-bars"></i>
          <span>Menu</span>
        </div>
        <div class="search-wrapper">
          <input 
            type="text" 
            class="search-input" 
            placeholder="Search" 
            @focus="isSearchFocused = true"
            @blur="isSearchFocused = false"
          >
        </div>
      </div>

      <!-- Лого по центру -->
      <div class="logo" :class="{ 'hide': isSearchFocused }">
        <a href="/" class="logo-link">Art Gallery</a>
      </div>

      <!-- Правая часть -->
      <div class="right-actions">
        <div class="account-wrapper">
          <router-link to="/profile" class="account-link">
            <i class="far fa-user"></i>
            <span>Account</span>
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import '@/styles/components/layout/Header.scss'

export default defineComponent({
  name: 'AppHeader',
  setup() {
    const isMenuOpen = ref(false)
    const isSearchFocused = ref(false)

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value
      document.body.style.overflow = isMenuOpen.value ? 'hidden' : ''
    }

    return {
      isMenuOpen,
      isSearchFocused,
      toggleMenu
    }
  }
})
</script>
