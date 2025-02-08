<template>
    <div class="books-row">
      <div class="header-row">
        <div class="title-container">
          <div class="title-header-row">Recomend for you</div>
          <div class="title-header-row-mini">Based on your reading history and preferences</div>
        </div>      </div>
  
      <div class="books-scroll-container">
        <div :class="['books-list', viewMode]">
          <div v-for="book in recentBooks" :key="book._id" :class="['book-card', viewMode]">
            <router-link 
              :to="{ name: 'BookDetail', params: { id: book._id } }" 
              class="details-button"
            >
              <img :src="book.image" :alt="book.title" class="book-image" />
              <StarRating :rating="book.rating" />
              <div class="book-details-author-title">
                <div class="book-details-title">{{ book.title }}</div>
                <div class="book-details-author">{{ book.author }}</div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import StarRating from '@/components/help/StarRating.vue';
  
  export default {
    name: 'BooksList',
    components: {
      StarRating,
    },
    data() {
      return {
        popularBooks: [],
        recentBooks: [],
        viewMode: 'grid',
      };
    },
    async created() {
      try {
        const [popularResponse, recentResponse] = await Promise.all([
          fetch('http://127.0.0.1:8001/api/books/books/popular?skip=0&limit=12'),
          fetch('http://127.0.0.1:8001/api/books/books/recent?skip=0&limit=12'),
        ]);
  
        this.popularBooks = await popularResponse.json();
        this.recentBooks = await recentResponse.json();
      } catch (error) {
        console.error('Ошибка при загрузке книг:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .books-row {
    width: 1200px;
    height: 400px;
    background-color: #f9f9f9;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 20px auto;
  }
  
  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .title-container {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  
  .title-header-row {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }
  
  .title-header-row-mini {
    font-size: 14px;
    color: #666;
  }
  
  .more-button {
    font-size: 16px;
    color: #007bff;
    text-decoration: none;
    transition: color 0.2s ease;
  }
  
  .more-button:hover {
    color: #0056b3;
  }
  
  .books-scroll-container {
    width: 100%;
    overflow-x: auto;
    padding-bottom: 20px; /* Для скролла */
  }
  
  .books-list {
    display: flex;
    gap: 20px;
    width: max-content;
  }
  
  .book-card {
    width: 180px;
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
  
  .book-card a {
    text-decoration: none;
    color: inherit;
  }
  
  .book-image {
    width: 100%;
    height: 220px;
    object-fit: cover;
  }
  
  .book-details-author-title {
    padding: 12px;
    text-align: center;
  }
  
  .book-details-title {
    font-size: 1rem;
    margin: 0.5rem 0;
    color: #333;
  }
  
  .book-details-author {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.5rem;
  }
  </style>