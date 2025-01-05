<template>
  <div class="splash-screen" v-if="isVisible">
    <h1 class="splash-text">текст</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

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
    }, 3000) // Заставка будет показываться 3 секунды
  }
})
</script>

<style lang="scss" scoped>
.splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  animation: fadeOut 0.5s ease 2.5s forwards;
}

.splash-text {
  font-size: 3rem;
  color: #2c3e50;
  position: relative;
  animation: textAnimation 2s ease forwards;
}

@keyframes textAnimation {
  0% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(0);
  }
  60% {
    transform: translateY(-20px);
  }
  80% {
    border-bottom: 2px solid #42b983;
  }
  100% {
    transform: translateY(-40px);
    border-bottom: 2px solid #42b983;
  }
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
    visibility: hidden;
  }
}
</style> 