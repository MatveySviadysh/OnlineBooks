<template>
  <footer class="main-footer">
    <div class="footer-content">
      <div class="footer-section customer-service">
        <h3>Customer Service</h3>
        <div class="working-hours">
          <p>Mon-Fri: 9:00 - 17:00</p>
          <p>Sat: 10:00 - 16:00</p>
          <p>Dec 24: 10:00 - 14:00</p>
        </div>
        <div class="contact-info">
          <a href="/contact_us" class="email">
            <i class="far fa-envelope"></i> Email Us
          </a>
          <a href="/comments/write_comments" class="email">
            <i class="far fa-envelope"></i> Write Com..
          </a>
        </div>
      </div>

      <div class="footer-section newsletter">
        <h3>Newsletter</h3>
        <p>Receive our newsletter and discover our stories, collections, and surprises.</p>
        <form @submit.prevent="handleSubscribe" class="subscribe-form">
          <input 
            v-model="email" 
            type="email" 
            placeholder="Your email" 
            required
          />
          <button type="submit">Subscribe</button>
        </form>
        <p v-if="message" :class="{'success-message': isSuccess, 'error-message': !isSuccess}">
          {{ message }}
        </p>
      </div>

      <div class="footer-section social-media">
        <h3>Follow Us</h3>
        <div class="social-links">
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Telegram">
            <i class="fab fa-telegram"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            <i class="fab fa-x-twitter"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <i class="fab fa-youtube"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p class="copyright">&copy; {{ currentYear }} Online Library. All Free Book.</p>
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
    const message = ref('')
    const isSuccess = ref(true)

    const handleSubscribe = async () => {
      try {
        const response = await fetch('http://localhost:8888/subscribe', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ recipient_email: email.value }),
        });

        const result = await response.json();

        if (result.success) {
          message.value = 'The invitation has been sent to your email!';
          isSuccess.value = true;
        } else if (result.message) {
          message.value = result.message; // Получаем сообщение об ошибке от сервера
          isSuccess.value = false;
        } else {
          message.value = 'Something went wrong. Please try again.';
          isSuccess.value = false;
        }
      } catch (error) {
        message.value = 'Error during subscription. Please try again later.';
        isSuccess.value = false;
      }

      email.value = '';

      setTimeout(() => {
        message.value = '';
      }, 60000); // 60000ms = 1 minute
    };

    return {
      email,
      handleSubscribe,
      currentYear: new Date().getFullYear(),
      message,
      isSuccess
    }
  }
})
</script>

<style scoped>
.success-message {
  color: green;
}

.error-message {
  color: red;
}
</style>
