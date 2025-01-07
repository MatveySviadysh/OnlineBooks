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
          <label for="password">Пароль:</label>
          <input 
            type="password" 
            id="password"
            v-model="formData.password"
            required
            placeholder="Введите пароль"
          >
        </div>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Вход...' : 'Войти' }}
        </button>
      </form>

      <div class="additional-links">
        <router-link to="/register">Регистрация</router-link>
      </div>
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
      error: ''
    }
  },
  methods: {
    async handleSubmit() {
      this.loading = true
      this.error = ''

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
          // Успешный вход, перенаправляем на главную
          this.$router.push('/')
        }
        
      } catch (error: any) {
        if (error.response) {
          this.error = error.response.data.detail || 'Неверный email или пароль'
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
