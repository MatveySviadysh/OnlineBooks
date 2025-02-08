<template>
  <div>
    <div class="side-menu" :class="{ 'is-open': isMenuOpen }">
      <div class="menu-header">
        <h1>Menu</h1>
        <p class="close-menu" @click="toggleMenu">
          <i class="fas fa-times"></i>
        </p>
      </div>
      <div class="menu-overlay" :class="{ 'is-visible': isMenuOpen }" @click="toggleMenu"></div>

      <nav class="menu-links">
        <div class="menu-category">
          <a href="#" class="menu-link" @click="toggleCategory('books')">
            Books <span class="expand-icon">{{ openCategory === 'books' ? '-' : '+' }}</span>
          </a>
          <div v-if="openCategory === 'books'" class="submenu">
            <a href="#" class="submenu-link">Книга 1</a>
            <a href="#" class="submenu-link">Книга 2</a>
            <a href="#" class="submenu-link">Книга 3</a>
          </div>
        </div>
        <div class="menu-category">
          <a href="#" class="menu-link" @click="toggleCategory('authors')">
            Authors <span class="expand-icon">{{ openCategory === 'authors' ? '-' : '+' }}</span>
          </a>
          <div v-if="openCategory === 'authors'" class="submenu">
            <a href="#" class="submenu-link">Автор 1</a>
            <a href="#" class="submenu-link">Автор 2</a>
            <a href="#" class="submenu-link">Автор 3</a>
          </div>
        </div>
      </nav>

      <div class="menu-footer">
        <div class="menu-text-links">
          <a href="/store-locator" class="menu-link"><i class="fas fa-store"></i> Find a store</a><br>
          <a href="/profile" class="menu-link"><i class="far fa-user"></i> Account</a><br>
          <a href="/contact_us" class="menu-link"><i class="far fa-envelope"></i> Contact Us</a><br>
        </div>
      </div>    
    </div>

    <header class="main-header">
      <div class="top-bar">
        <div class="top-bar-content">
          <div class="top-links">
            <a href="/store-locator">Find a Store</a>
            <a href="/contact_us">Contact Us</a>
            <a href="/news/news_feed">News Feed</a>
          </div>
        </div>
      </div>

      <div class="menu-overlay" :class="{ 'is-visible': isMenuOpen }" @click="toggleMenu"></div>

      <div class="header-content">
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

        <div class="logo" :class="{ 'hide': isSearchFocused }">
          <a href="/" class="logo-link">Online Book</a>
        </div>

        <div class="right-actions">
          <div class="account-wrapper">
            <router-link to="/profile" class="account-link">
              <i class="far fa-user"></i>
              <span>Account</span>
            </router-link>
            <a href="/account/storege" class="storage-link">
              <i class="fas fa-book fa-sm"></i><span>Storage</span>
            </a>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import '@/styles/components/layout/Header.scss'

export default defineComponent({
  name: 'AppHeader',
  setup() {
    const isMenuOpen = ref(false)
    const isSearchFocused = ref(false)
    const openCategory = ref<string | null>(null)

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value
      document.body.classList.toggle('no-scroll', isMenuOpen.value)
    }

    const toggleCategory = (category: string) => {
      openCategory.value = openCategory.value === category ? null : category
    }

    return {
      isMenuOpen,
      isSearchFocused,
      toggleMenu,
      openCategory,
      toggleCategory
    }
  }
})
</script>


