<template>
  <div class="home">
    <img src="@/assets/main.jpg" alt="">
    <BookTicker />
    <BooksList />
    <CookieConsent />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import '@/styles/components/common/HomePage.scss'
import BookTicker from '../help/BookTicker.vue'
import CookieConsent from '../help/CookieConsent.vue'
import BooksList from '../help/BooksList.vue'

export default defineComponent({
  name: 'HomePage',
  components: {
    BookTicker,
    CookieConsent,
    BooksList
  }
})
</script> 
