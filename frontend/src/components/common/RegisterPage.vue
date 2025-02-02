<template>
  <div class="register-container">
    <div class="register-form">
      
      <div class="alert error" v-if="error">
        {{ error }}
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <input 
            type="email" 
            id="email"
            v-model="formData.email"
            required
            placeholder="E-mail"
          >
        </div>

        <div class="form-group password-group">
          <div class="header-password-toggle">
              <p class="toggle-password" @click="togglePassword">
                {{ showPassword ? 'hide' : 'show' }}
              </p>
          </div>
          <div class="password-container">
            <input 
              :type="showPassword ? 'text' : 'password'" 
              id="password"
              v-model="formData.password"
              required
              placeholder="Password"
            >
          </div>
        </div>

        <button class="register-button" type="submit" :disabled="loading">
          {{ loading ? 'Registration...' : 'Register' }}
        </button>
      </form>

      <div class="additional-links">
        <router-link to="/login">Already have an account? Login</router-link>
      </div>
    </div>

    <!-- Сообщение об успешной регистрации -->
    <div v-if="successMessage" class="success-popup">
      <p>{{ successMessage }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import '@/styles/components/common/RegisterPage.scss'

export default defineComponent({
  name: 'RegisterPage',
  data() {
    return {
      formData: {
        email: '',
        password: ''
      },
      loading: false,
      error: '',
      successMessage: '',  // Новая переменная для хранения сообщения об успешной регистрации
      showPassword: false
    }
  },
  methods: {
    async handleSubmit() {
      this.loading = true;
      this.error = '';
      this.successMessage = '';  // Очищаем сообщение при каждом новом запросе

      try {
        // Регистрация
        await axios.post('http://localhost:8001/api/users/register', {
          email: this.formData.email,
          password: this.formData.password
        });

        // Успешная регистрация
        this.successMessage = 'Registration successful!';  // Устанавливаем сообщение об успешной регистрации

        // Автоматический вход после регистрации
        await axios.post('http://localhost:8001/api/users/login', {
          email: this.formData.email,
          password: this.formData.password
        }, { withCredentials: true });

        // Переход на страницу профиля через 2 секунды
        setTimeout(() => {
          this.$router.push('/profile');
        }, 2000);

      } catch (error: any) {
        if (error.response) {
          this.error = error.response.data.detail || 'Ошибка при регистрации';
        } else {
          this.error = 'Ошибка сервера. Попробуйте позже.';
        }
      } finally {
        this.loading = false;
      }
    },
    togglePassword() {
      this.showPassword = !this.showPassword;
    }
  }
});
</script>

<style scoped>
/* Стили для всплывающего сообщения об успешной регистрации */
.success-popup {
  background-color: #fffdf8;
  color: #333;
  padding: 20px;
  border-radius: 8px;
  position: fixed;
  top: 70px; /* Сдвигаем окно на 50px ниже */
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: 300px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeIn 1s forwards, fadeOut 1s 2s forwards;
  text-align: center;
  font-size: 16px;
}

/* Анимация появления */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateX(-50%) translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
}

/* Анимация исчезновения */
@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateX(-50%) translateY(20px);
  }
}
</style>