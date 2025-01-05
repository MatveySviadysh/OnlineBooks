<template>
  <div class="login-container">
    <div class="login-form">
      <h2>Вход в систему</h2>
      
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

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 20px;
}

.login-form {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #2c3e50;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

input:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.1);
}

button {
  width: 100%;
  padding: 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #3aa876;
}

button:disabled {
  background-color: #a8d5c2;
  cursor: not-allowed;
}

.alert.error {
  background-color: #fee;
  color: #e74c3c;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
  text-align: center;
}

.additional-links {
  margin-top: 20px;
  text-align: center;
  display: flex;
  justify-content: space-between;
}

.additional-links a {
  color: #42b983;
  text-decoration: none;
}

.additional-links a:hover {
  text-decoration: underline;
}
</style> 