<template>
  <div class="profile">
    <h1>Профиль пользователя</h1>
    
    <div v-if="loading" class="loading">
      Загрузка...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
      <div class="error-actions">
        <router-link to="/login" class="login-link">Войти</router-link>
      </div>
    </div>

    <div v-else-if="user" class="profile-content">
      <div class="profile-info">
        <h2>Личные данные</h2>
        <div class="info-item">
          <span class="label">Email:</span>
          <span class="value">{{ user.email }}</span>
        </div>
        <!-- Здесь можно добавить другие поля пользователя -->
      </div>

      <div class="profile-actions">
        <button @click="logout" class="logout-button">Выйти из аккаунта</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import '@/styles/components/common/ProfilePage.scss'

interface User {
  email: string;
  // Добавьте другие поля пользователя при необходимости
}

export default defineComponent({
  name: 'ProfilePage',
  data() {
    return {
      user: null as User | null,
      loading: true,
      error: ''
    }
  },
  created() {
    this.fetchUserProfile()
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await axios.get('http://localhost:8001/api/users/me', {
          withCredentials: true
        })
        
        if (response.status === 200 && response.data.email) {
          this.user = response.data
          this.error = ''
        } else {
          this.error = 'Не удалось загрузить данные пользователя'
        }
      } catch (error: any) {
        if (error.response?.status === 401) {
          this.error = 'Необходимо войти в систему'
        } else {
          this.error = 'Ошибка при загрузке профиля'
        }
        console.error('Profile error:', error)
      } finally {
        this.loading = false
      }
    },
    async logout() {
      try {
        await axios.post('http://localhost:8001/api/users/logout', {}, {
          withCredentials: true
        })
        this.user = null
        this.$router.push('/login')
      } catch (error) {
        console.error('Logout error:', error)
      }
    }
  }
})
</script>
