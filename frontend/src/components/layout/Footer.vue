<template>
  <footer class="main-footer">
    <div class="footer-content">
      <!-- Навигация -->
      <div class="footer-section">
        <h3>Навигация</h3>
        <nav>
          <ul>
            <li><router-link to="/services">Услуги</router-link></li>
            <li><router-link to="/offers">Предложения</router-link></li>
            <li><router-link to="/artists">Художники</router-link></li>
            <li><router-link to="/list">Каталог</router-link></li>
          </ul>
        </nav>
      </div>

      <!-- Служба поддержки -->
      <div class="footer-section customer-service">
        <h3>Служба поддержки</h3>
        <div class="working-hours">
          <p>Пн-Пт: 9:00 - 17:00</p>
          <p>Сб: 10:00 - 16:00</p>
          <p>24 декабря: 10:00 - 14:00</p>
        </div>
        <div class="contact-info">
          <a href="tel:+74004414546" class="phone">+7 (400) 441-45-46</a>
          <a href="mailto:support@example.com" class="email">
            <i class="far fa-envelope"></i> Написать нам
          </a>
        </div>
      </div>

      <!-- Рассылка -->
      <div class="footer-section newsletter">
        <h3>Новости и акции</h3>
        <p>Подпишитесь на нашу рассылку, чтобы быть в курсе новых коллекций и специальных предложений</p>
        <form @submit.prevent="handleSubscribe" class="subscribe-form">
          <input 
            v-model="email" 
            type="email" 
            placeholder="Ваш email" 
            required
          />
          <button type="submit">Подписаться</button>
        </form>
      </div>

      <!-- Социальные сети -->
      <div class="footer-section social-media">
        <h3>Мы в соцсетях</h3>
        <div class="social-links">
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Pinterest">
            <i class="fab fa-pinterest"></i>
          </a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <a href="#" class="location-link">
        <i class="fas fa-map-marker-alt"></i> Россия
      </a>
      <p class="copyright">&copy; {{ currentYear }} Art Gallery. Все права защищены.</p>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import '@/styles/components/layout/Footer.scss'

export default defineComponent({
  name: 'AppFooter',
  setup() {
    const email = ref('')

    const handleSubscribe = () => {
      console.log('Подписка на email:', email.value)
      email.value = ''
    }

    return {
      email,
      handleSubscribe,
      currentYear: new Date().getFullYear()
    }
  }
})
</script>

