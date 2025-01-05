<template>
  <div class="register-container">
    <div class="register-form">
      <h2>Регистрация</h2>
      
      <div class="alert error" v-if="error">
        {{ error }}
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="email">Email:</label>
          <input 
            type="email" 
            id="email"
            v-model="formData.email"
            required
            placeholder="Введите email"
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
          {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
        </button>
      </form>

      <div class="additional-links">
        <router-link to="/login">Уже есть аккаунт? Войти</router-link>
      </div>
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
      error: ''
    }
  },
  methods: {
    async handleSubmit() {
      this.loading = true
      this.error = ''

      try {
        // Регистрация
        await axios.post('http://localhost:8001/api/users/register', {
          email: this.formData.email,
          password: this.formData.password
        })

        // Автоматический вход после регистрации
        await axios.post('http://localhost:8001/api/users/login', {
          email: this.formData.email,
          password: this.formData.password
        }, {
          withCredentials: true
        })

        // Перенаправление на профиль
        this.$router.push('/profile')
        
      } catch (error: any) {
        if (error.response) {
          this.error = error.response.data.detail || 'Ошибка при регистрации'
        } else {
          this.error = 'Ошибка сервера. Попробуйте позже.'
        }
        console.error('Registration error:', error)
      } finally {
        this.loading = false
      }
    }
  }
})
</script>
