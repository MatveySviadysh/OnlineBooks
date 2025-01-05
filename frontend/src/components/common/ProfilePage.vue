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

<style scoped>
.profile {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}

.error {
  text-align: center;
  padding: 20px;
  background-color: #fee;
  border-radius: 8px;
  color: #e74c3c;
  margin-top: 20px;
}

.error-actions {
  margin-top: 15px;
}

.profile-content {
  margin-top: 20px;
}

.profile-info {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.info-item {
  margin: 15px 0;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.label {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 10px;
}

.value {
  color: #42b983;
}

.profile-actions {
  margin-top: 20px;
  text-align: center;
}

.logout-button {
  padding: 10px 20px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c0392b;
}

.login-link {
  display: inline-block;
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.login-link:hover {
  background-color: #3aa876;
}
</style> 