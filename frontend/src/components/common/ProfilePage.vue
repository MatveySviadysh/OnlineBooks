<template>
  <div class="profile-container">
    <div class="menu-block">
      <div class="profile-actions">
        <a href="/account" class="word-Account">Account</a><br>
        <a href="/all_books" class="word-History">Books</a><br>
        <a href="/account/storege" class="word-History">Storage</a><br>
        <a href="/authors" class="word-History">Authors</a><br>
        <a href="/news/news_feed" class="word-History-last">News Feed</a><br>
        <hr class="menu-line">
        <a @click="logout" class="logout-button" role="button">Sign Out</a>
      </div>
    </div>

    <div v-if="loading" class="loading">
      Loading...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
      <div class="error-actions">
        <router-link to="/login" class="login-link">Login</router-link>
      </div>
    </div>

    <div v-else-if="user" class="profile-content">
      <div class="profile-info">
        <div class="header-info">
          <div class="title-info">Profile Information</div>
          <div class="around-circle">
            <i class="fas fa-pencil-alt icon-info"></i>
          </div>
        </div>
        <hr class="line-info">
        <div class="info-item">
          <span class="label">Email:</span>
          <span class="value">{{ user.email }}</span>
        </div>
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
          this.error = 'Failed to load user data'
        }
      } catch (error: any) {
        if (error.response?.status === 401) {
          this.$router.push('/login')
          return
        } else {
          this.error = 'Error loading profile'
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
