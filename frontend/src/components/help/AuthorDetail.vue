<template>
    <div class="author-detail">
      <div v-if="loading" class="loading">Loading...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else class="detail-content">
        <div class="author-header">
          <div class="author-photo">
            <img v-if="author.photo" :src="author.photo" :alt="`Photo of ${author.first_name} ${author.last_name}`" />
            <span v-else>No photo available</span>
          </div>
          <div class="author-info">
            <h2>{{ author.first_name }} {{ author.last_name }}</h2>
            <p><strong>Patronymic:</strong> {{ author.patronymic }}</p>
            <p><strong>Birth Date:</strong> {{ author.birth_date }}</p>
            <p><strong>Death Date:</strong> {{ author.death_date || 'N/A' }}</p>
          </div>
        </div>
        <div class="author-bio">
          <h3>Biography</h3>
          <p>{{ author.bio }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import axios from 'axios';
  
  interface Author {
    id: number;
    first_name: string;
    last_name: string;
    patronymic: string;
    birth_date: string;
    death_date: string | null;
    bio: string;
    photo: string;
  }
  
  export default defineComponent({
    name: 'AuthorDetail',
    data() {
      return {
        author: {} as Author,
        loading: true,
        error: '' as string | null,
      };
    },
    created() {
      this.fetchAuthorDetails();
    },
    methods: {
      async fetchAuthorDetails() {
        const fixedAuthorId = 4; // Use the fixed ID you mentioned
        try {
          this.loading = true;
          const response = await axios.get(`http://localhost:8000/v1/authors/${fixedAuthorId}`);
          this.author = response.data;
          this.error = null;
        } catch (error) {
          this.error = 'Error loading author details';
        } finally {
          this.loading = false;
        }
      }
    }
  });
  </script>
  
  <style scoped>
  .author-detail {
    padding: 20px;
    background-color: #f7f7f7;
    max-width: 800px;
    margin: 20px auto;
  }
  
  .loading {
    text-align: center;
    font-size: 18px;
  }
  
  .error {
    color: red;
    font-size: 16px;
    text-align: center;
  }
  
  .detail-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .author-header {
    display: flex;
    gap: 20px;
  }
  
  .author-photo {
    width: 120px;
    height: 120px;
    border-radius: 8px;
    overflow: hidden;
    background-color: #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .author-photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .author-info {
    flex-grow: 1;
  }
  
  .author-info h2 {
    font-size: 24px;
    margin: 0;
    color: #333;
  }
  
  .author-bio h3 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .author-bio p {
    font-size: 16px;
    color: #666;
  }
  </style>
  