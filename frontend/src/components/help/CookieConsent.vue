<template>
  <div v-if="!accepted" class="cookie-consent">
    <div class="cookie-content">
      <div class="cookie-text">
        <h3>🍪 Мы используем файлы cookie</h3>
        <p>Мы используем файлы cookie и другие технологии отслеживания для улучшения вашего просмотра на нашем веб-сайте, 
          чтобы показывать вам персонализированный контент, целевую рекламу и анализировать наш трафик. 
          Прочтите нашу Политику использования файлов cookie, чтобы узнать больше о том, как мы используем файлы cookie.</p>
      </div>
      <div class="cookie-buttons">
        <button @click="acceptCookies" class="consent-button accept-button">Принять все cookies</button>
        <button @click="declineCookies" class="consent-button decline-button">Только необходимые</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'CookieConsent',
  data() {
    return {
      accepted: false
    }
  },
  created() {
    // Проверяем, было ли уже принято согласие
    this.accepted = localStorage.getItem('cookieConsent') === 'true'
  },
  methods: {
    acceptCookies() {
      this.accepted = true
      localStorage.setItem('cookieConsent', 'true')
    },
    declineCookies() {
      this.accepted = true
      localStorage.setItem('cookieConsent', 'false')
    }
  }
})
</script>

<style lang="scss" scoped>
.cookie-consent {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #000000;
  color: white;
  padding: 1.5rem;
  z-index: 1000;
  animation: slideUp 0.5s ease-out;
  box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.1);
}

.cookie-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.cookie-text {
  flex: 1;
  min-width: 300px;
  
  h3 {
    margin: 0 0 1rem 0;
    font-family: 'Playfair Display', serif;
    font-weight: 400;
    font-size: 1.5rem;
  }
  
  p {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.6;
    font-weight: 300;
    opacity: 0.9;
    font-family: 'Roboto', sans-serif;
    letter-spacing: 0.3px;
  }
}

.cookie-buttons {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.consent-button {
  padding: 0.8rem 1.8rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: #000000;
  color: white;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 300;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
  font-family: 'Roboto', sans-serif;
  border-radius: 4px;
  
  &:hover {
    border-color: rgba(255, 255, 255, 0.8);
    background: #1a1a1a;
  }
  
  &.accept-button {
    border-color: rgba(255, 255, 255, 0.5);
    
    &:hover {
      border-color: white;
    }
  }
  
  &.decline-button {
    background: transparent;
    
    &:hover {
      background: rgba(255, 255, 255, 0.1);
    }
  }
}

@keyframes slideUp {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@media (max-width: 768px) {
  .cookie-consent {
    padding: 1rem;
  }

  .cookie-content {
    flex-direction: column;
    text-align: center;
  }
  
  .cookie-buttons {
    width: 100%;
    flex-direction: column;
    
    button {
      width: 100%;
    }
  }
  
  .cookie-text {
    h3 {
      font-size: 1.3rem;
    }
    
    p {
      font-size: 0.9rem;
    }
  }
}
</style>