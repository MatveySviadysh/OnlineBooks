<template>
    <div class="all-books-container">
      <div class="header-info">
        <div>Главная>Все подборки>читать</div>
        <div>Десятки тысяч бесплатных книг</div>
        <div>{{ bookCount }} книг</div>
        <div>{{ averageRating }}</div>
      </div>
      <div class="image-container">
        <img src="../../assets/allbooksread.jpeg" alt="" class="allbooksread-img">
      </div>
      
      <div class="books-grid">
        <div v-for="book in paginatedBooks" :key="book._id" class="book-card">
          <router-link :to="{ name: 'BookDetail', params: { id: book._id } }">
            <img :src="book.image" :alt="book.title" class="book-image" />
            <div class="book-details">
              <h3 class="book-title">{{ book.title }}</h3>
              <div class="book-author">{{ book.author }}</div>
              <StarRating :rating="book.rating" />
            </div>
          </router-link>
        </div>
      </div>
  
      <!-- Пагинация -->
      <div class="pagination">
        <button 
          @click="prevPage"
          :disabled="currentPage === 1"
          class="pagination-button"
        >
          Назад
        </button>
        <span class="pagination-info">Страница {{ currentPage }} из {{ totalPages }}</span>
        <button 
          @click="nextPage" 
          :disabled="currentPage === totalPages"
          class="pagination-button"
        >
          Вперед
        </button>
      </div>
    </div>
  </template>
  <script>
  import StarRating from '@/components/help/StarRating.vue';
  
  export default {
    name: 'AllReadBooks',
    components: {
      StarRating,
    },
    data() {
      return {
        books: [], // Все книги, загруженные с сервера
        currentPage: 1, // Текущая страница
        limit: 12, // Количество книг на странице
        bookCount: 0, // Количество книг
        averageRating: 0, // Средний рейтинг
      };
    },
    computed: {
      // Общее количество страниц
      totalPages() {
        return Math.ceil(this.books.length / this.limit);
      },
      // Книги для текущей страницы
      paginatedBooks() {
        const start = (this.currentPage - 1) * this.limit;
        const end = start + this.limit;
        return this.books.slice(start, end);
      },
    },
    async created() {
      await this.fetchBooks();
      await this.fetchBookCount();
      await this.fetchAverageRating();
    },
    methods: {
      // Загрузка всех книг с сервера
      async fetchBooks() {
        try {
          const response = await fetch('http://localhost:8001/api/books/books/all');
          this.books = await response.json();
        } catch (error) {
          console.error('Ошибка при загрузке книг:', error);
        }
      },
      // Загрузка количества книг
      async fetchBookCount() {
        try {
          const response = await fetch('http://localhost:8001/api/books/books/count');
          const data = await response.json();
          this.bookCount = data;
        } catch (error) {
          console.error('Ошибка при загрузке количества книг:', error);
        }
      },
      // Загрузка среднего рейтинга
      async fetchAverageRating() {
        try {
          const response = await fetch('http://localhost:8001/api/books/books/average_rating');
          const data = await response.json();
          this.averageRating = data;
        } catch (error) {
          console.error('Ошибка при загрузке среднего рейтинга:', error);
        }
      },
      // Переход на предыдущую страницу
      prevPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },
      // Переход на следующую страницу
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  .allbooksread-img{
    height: 480px;
  }

  .all-books-container {
    margin-top: 100px;
    padding: 2rem;
    max-width: 1200px;
    margin: 100px auto 0;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2rem;
    color: #333;
  }
  
  .books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
  }
  
  .book-card {
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
    height: 300px;
    object-fit: cover;
  }
  
  .book-details {
    padding: 1rem;
    text-align: center;
  }
  
  .book-title {
    font-size: 1.1rem;
    margin: 0.5rem 0;
    color: #333;
  }
  
  .book-author {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.5rem;
  }
  
  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    margin-top: 2rem;
  }
  
  .pagination-button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  
  .pagination-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .pagination-button:hover:not(:disabled) {
    background-color: #0056b3;
  }
  
  .pagination-info {
    font-size: 1rem;
    color: #333;
  }
  </style>