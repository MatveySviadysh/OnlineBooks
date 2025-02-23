<template>
  <div class="splash-screen" v-if="isVisible">
    <div class="splash-container">
      <h1 class="splash-text">OnlineBook</h1>
      <div class="splash-line"></div>
    </div>
    <div class="lines-container"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import '@/styles/components/help/SplashScreen.scss';

export default defineComponent({
  name: 'SplashScreen',
  data() {
    return {
      isVisible: true,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isVisible = false;
    }, 5000); // Increased time for better viewing
  },
});
</script>

<style scoped>
.splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  overflow: hidden;
  animation: fadeOut 1s ease-out 4s forwards; /* Fade out after some time */
}

.splash-container {
  text-align: center;
  animation: fadeIn 2s ease-in-out; /* Smooth appearance */
}

.splash-text {
  font-size: 120px;
  font-weight: bold;
  color: #333;
  text-transform: uppercase;
  letter-spacing: 5px;
  animation: textAnimation 4s ease-in-out forwards;
}

.splash-line {
  width: 0;
  height: 2px;
  background-color: #333;
  margin-top: 20px;
  animation: drawLine 4s 2s forwards;
}

/* New fade-out animation for splash screen */
@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

/* Animation for the text */
@keyframes textAnimation {
  0% {
    opacity: 0;
    transform: translateY(-30px);
  }
  50% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 1;
  }
}

/* Line animation */
@keyframes drawLine {
  0% {
    width: 0;
  }
  100% {
    width: 100%;
  }
}

/* Lines container */
.lines-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 9980;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  animation: randomBookMovement 5s ease-in-out infinite;
}

.line {
  position: absolute;
  border-top: 2px solid black;
  animation: drawBook 4s ease-in-out infinite;
}

@keyframes drawBook {
  0% {
    width: 0;
    left: 50%;
    top: 50%;
    opacity: 0;
  }
  25% {
    width: 80px;
    left: 50%;
    top: 50%;
    opacity: 1;
  }
  50% {
    width: 80px;
    left: 50%;
    top: 50%;
    opacity: 1;
  }
  75% {
    width: 200px;
    left: 40%;
    top: 50%;
    opacity: 1;
  }
  100% {
    width: 200px;
    left: 40%;
    top: 50%;
    opacity: 0;
  }
}

/* Random movement of the books */
@keyframes randomBookMovement {
  0% {
    top: 0%;
    left: 0%;
  }
  25% {
    top: 20%;
    left: 30%;
  }
  50% {
    top: 60%;
    left: 50%;
  }
  75% {
    top: 80%;
    left: 80%;
  }
  100% {
    top: 100%;
    left: 100%;
  }
}
</style>
