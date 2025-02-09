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
        searchQuery: '',
        quotes: []
      };
    },
    async created() {
      try {
        const response = await fetch('http://localhost:8000/v1/quotes/all');
        this.quotes = await response.json();
      } catch (error) {
        console.error('Error fetching quotes:', error);
      }
    }
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
