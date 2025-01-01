<template>
    <div>
      <h1>Авторы</h1>
      <table>
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
            <td>{{ author.birth_date }}</td>
            <td>{{ author.death_date }}</td>
            <td>{{ author.bio }}</td>
            <td><img :src="author.photo" alt="Фото автора" width="50"/></td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        authors: []
      };
    },
    created() {
      this.fetchAuthors();
    },
    methods: {
        async fetchAuthors() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/v1/authors/all/', {
      headers: {
        accept: 'application/json',
      },
    });
    console.log('Response data:', response.data); // Убедитесь, что формат данных соответствует ожиданиям
    this.authors = response.data;
  } catch (error) {
    console.error('Error fetching authors:', error);
  }
}


    }
  };
  </script>
  
  <style>
  /* Добавьте свои стили здесь */
  </style>
  