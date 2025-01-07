<template>
    <div class="all-books-container">
      <h1>{{ pageTitle }}</h1>
      <div class="books-grid">
        <div v-for="book in books" :key="book.id" class="book-card">
          <img :src="book.cover" :alt="book.title" />
          <h3>{{ book.title }}</h3>
          <StarRating :rating="book.rating" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import StarRating from '@/components/help/StarRating.vue'
  
  export default {
    name: 'AllBooks',
    components: {
      StarRating
    },
    data() {
      return {
        books: [],
        type: ''
      }
    },
    computed: {
      pageTitle() {
        return this.type === 'popular' ? 'Популярные книги' : 'Новинки'
      }
    },
    async created() {
      this.type = this.$route.query.type
      try {
        const response = await fetch(
          `http://127.0.0.1:8001/api/books/books/${this.type}?skip=0&limit=100`
        )
        this.books = await response.json()
      } catch (error) {
        console.error('Ошибка при загрузке книг:', error)
      }
    }
  }
  </script>
  
  <style scoped>
  .all-books-container {
    padding: 2rem;
  }
  
  .books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }
  
  .book-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 10px;
  }
  
  .book-card img {
    width: 150px;
    height: 220px;
    object-fit: cover;
    margin-bottom: 10px;
  }
  
  .book-card h3 {
    font-size: 1rem;
    margin: 5px 0;
  }
  </style>