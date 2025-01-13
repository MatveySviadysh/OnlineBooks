<template>
    <div class="quotes-container">
      <h1>Цитатник</h1>
      <input type="text" v-model="searchQuery" placeholder="Поиск цитат..." class="search-input" />
      <div v-for="quote in quotes" :key="quote.id" class="quote">
        <p>"{{ quote.text }}"</p>
        <small>- {{ quote.author }}</small>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '', // Добавленная переменная для хранения поискового запроса
        quotes: [
          { id: 1, text: 'Всё, что мы есть — это результат того, что мы думали.', author: 'Будда' },
          { id: 2, text: 'Сложности — это просто возможность начать заново, более мудро.', author: 'Генри Форд' },
          { id: 3, text: 'Мы не можем изменить прошлое, но мы можем изменить будущее.', author: 'Дейл Карнеги' },
          // Добавьте больше цитат здесь
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .quotes-container {
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .search-input {
    padding: 10px;
    margin-bottom: 20px;
    width: 100%;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .quote {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    background-color: #f9f9f9;
  }
  </style>
  