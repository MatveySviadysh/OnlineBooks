<template>
  <div class="authors-list">
    <h1>Список авторов</h1>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else class="authors-table">
      <thead>
        <tr>
          <th>Имя</th>
          <th>Фамилия</th>
          <th>Отчество</th>
          <th>Дата рождения</th>
          <th>Дата смерти</th>
          <th>Биография</th>
          <th>Фото</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="author in authors" :key="author.id">
          <td>{{ author.first_name }}</td>
          <td>{{ author.last_name }}</td>
          <td>{{ author.patronymic }}</td>
          <td>{{ formatDate(author.birth_date) }}</td>
          <td>{{ formatDate(author.death_date) }}</td>
          <td>{{ truncateText(author.bio, 100) }}</td>
          <td>
            <img 
              v-if="author.photo" 
              :src="author.photo" 
              :alt="`Фото ${author.first_name} ${author.last_name}`" 
              width="50"
            />
            <span v-else>Нет фото</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'

interface Author {
  id: number;
  first_name: string;
  last_name: string;
  patronymic: string;
  birth_date: string;
  death_date: string;
  bio: string;
  photo: string;
}

export default defineComponent({
  name: 'AuthorsList',
  data() {
    return {
      authors: [] as Author[],
      loading: true,
      error: '' as string | null
    }
  },
  created() {
    this.fetchAuthors()
  },
  methods: {
    async fetchAuthors() {
      try {
        this.loading = true
        const response = await axios.get('http://127.0.0.1:8000/v1/authors/all/', {
          headers: {
            accept: 'application/json',
          },
        })
        this.authors = response.data
        this.error = null
      } catch (error: any) {
        console.error('Error fetching authors:', error)
        this.error = 'Ошибка при загрузке списка авторов'
      } finally {
        this.loading = false
      }
    },
    formatDate(date: string) {
      if (!date) return 'Не указано'
      return new Date(date).toLocaleDateString('ru-RU')
    },
    truncateText(text: string, length: number) {
      if (!text) return 'Нет описания'
      return text.length > length ? text.substring(0, length) + '...' : text
    }
  }
})
</script>

<style scoped>
.authors-list {
  padding: 20px;
}

.authors-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.authors-table th,
.authors-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.authors-table th {
  background-color: #f4f4f4;
}

.authors-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.authors-table tr:hover {
  background-color: #f5f5f5;
}

.error {
  color: red;
  padding: 10px;
  margin: 10px 0;
}

img {
  object-fit: cover;
  border-radius: 4px;
}
</style>
  