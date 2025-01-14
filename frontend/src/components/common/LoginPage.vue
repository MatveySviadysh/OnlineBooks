<template>
  <div class="login-container">
    <div class="login-form">
      <h2>Вход в систему</h2>
      
      <div class="alert error" v-if="error">
        {{ error }}
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="email">E-mail *</label>
          <input 
            type="email" 
            id="email"
            v-model="formData.email"
            required
            placeholder="yourname@domain.com"
          >
        </div>

        <div class="form-group">
          <label for="password">Password:</label>
          <input 
            type="password" 
            id="password"
            v-model="formData.password"
            required
            placeholder="Enter your password"
          >
        </div>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Login...' : 'Login' }}
        </button>
      </form>

      <div class="additional-links">
        <router-link to="/register">Registration</router-link>
      </div>
    </div>

    <!-- Сообщение об успешном входе -->
    <div v-if="successMessage" class="success-popup">
      <p>{{ successMessage }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import '@/styles/components/common/LoginPage.scss'

export default defineComponent({
  name: 'LoginPage',
  data() {
    return {
      formData: {
        email: '',
        password: ''
      },
      loading: false,
      error: '',
      successMessage: ''  // Новая переменная для хранения сообщения об успешном входе
    }
  },
  methods: {
    async handleSubmit() {
      this.loading = true
      this.error = ''
      this.successMessage = ''  // Очищаем сообщение при каждом новом запросе

      try {
        const response = await axios.post('http://localhost:8001/api/users/login', {
          email: this.formData.email,
          password: this.formData.password
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          withCredentials: true
        })

        if (response.status === 200) {
          // Успешный вход
          this.successMessage = 'Login successful!';  // Устанавливаем сообщение об успешном входе
          setTimeout(() => {
            this.$router.push('/profile')  // Переходим на страницу профиля
          }, 2000);  // Задержка перед переходом для отображения сообщения
        }
        
      } catch (error: any) {
        if (error.response) {
          this.error = error.response.data.detail || 'Invalid email or password'
        } else {
          this.error = 'Ошибка сервера. Попробуйте позже.'
        }
        console.error('Login error:', error)
      } finally {
        this.loading = false
      }
    }
  }
})
</script>
<style scoped>
/* Стили для всплывающего сообщения об успешном входе */
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
