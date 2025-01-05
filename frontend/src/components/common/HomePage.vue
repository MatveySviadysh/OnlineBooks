<template>
  <div class="home">
    <h1>Главная страница</h1>
    <BookTicker />
    <CookieConsent />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import '@/styles/components/common/HomePage.scss'
import BookTicker from '../help/BookTicker.vue'
import CookieConsent from '../help/CookieConsent.vue'

export default defineComponent({
  name: 'HomePage',
  components: {
    BookTicker,
    CookieConsent
  }
})
</script> 