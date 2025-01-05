<template>
  <div class="splash-screen" v-if="isVisible">
    <h1 class="splash-text">текст</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import '@/styles/components/help/SplashScreen.scss'

export default defineComponent({
  name: 'SplashScreen',
  data() {
    return {
      isVisible: true
    }
  },
  mounted() {
    setTimeout(() => {
      this.isVisible = false
    }, 3000)
  }
})
</script> 