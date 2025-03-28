<template>
    <div class="all-books-container">
      <div class="header-info">
        <div><a style="margin-right: 10px; text-decoration: none; color: black;" href="/">Главная</a>><font style="margin-left: 10px; color: orange;">Все Подборки</font></div>
        
      </div>
      <div class="image-container">
        <img src="../../assets/allbooksread.jpeg" alt="" class="allbooksread-img">
      </div>
      <div class="body-info">
        <div><i class="fas fa-dollar-sign"></i> Десятки тысяч бесплатных книг</div>
        <div><i class="fas fa-book-open"></i> {{ bookCount }} книг</div>
        <div><i class="fas fa-star"></i> {{ averageRating.toFixed(1) }}</div>
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
  .body-info{
    display: flex;
    margin-top: 20px;
    margin-bottom:  40px;
    justify-content: center;
    gap: 60px;
    padding: 50px;
  }
  .all-books-container {
      max-width: 1200px;
      margin: 100px auto 40px;
      padding: 0 20px;
  }
  
  .header-info {
      margin-bottom: 40px;
  }
  
  .breadcrumbs {
      font-size: 0.9rem;
      color: #666;
      margin-bottom: 15px;
  }
  
  .breadcrumbs a {
      color: #2c3e50;
      text-decoration: none;
      transition: color 0.3s;
  }
  
  .breadcrumbs a:hover {
      color: #42b983;
  }
  
  .header-title {
      font-size: 2.5rem;
      font-weight: 600;
      color: #2c3e50;
      margin-bottom: 15px;
  }
  
  .stats-container {
      display: flex;
      gap: 25px;
      color: #666;
      font-size: 0.95rem;
      margin-bottom: 30px;
  }
  
  .image-container {
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 40px;
  }
  
  .allbooksread-img {
      width: 100%;
      height: 400px;
      object-fit: cover;
      display: block;
  }
  
  .books-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 30px;
      margin-bottom: 50px;
  }
  
  .book-card {
      background: white;
      border-radius: 10px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      border: 1px solid #eee;
  }
  
  .book-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 24px rgba(0,0,0,0.1);
  }
  
  .book-card a {
      text-decoration: none;
      color: inherit;
      display: block;
      height: 100%;
  }
  
  .book-image {
      width: 100%;
      height: 320px;
      object-fit: cover;
      border-bottom: 1px solid #f5f5f5;
  }
  
  .book-details {
      padding: 18px;
      background: white;
  }
  
  .book-title {
      font-size: 1.05rem;
      font-weight: 500;
      margin: 0 0 8px;
      color: #2c3e50;
      line-height: 1.3;
      height: 3.2em;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
  }
  
  .book-author {
      font-size: 0.9rem;
      color: #666;
      margin-bottom: 12px;
      height: 1.5em;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
  }
  
  .pagination {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px;
      margin: 40px 0;
  }
  
  .pagination-button {
      padding: 10px 25px;
      background: #f8f9fa;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      color: #2c3e50;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      gap: 8px;
  }
  
  .pagination-button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
  }
  
  .pagination-button:hover:not(:disabled) {
      background: #42b983;
      border-color: #42b983;
      color: white;
      transform: translateY(-1px);
  }
  
  .pagination-info {
      font-size: 0.95rem;
      color: #666;
      margin: 0 15px;
  }
  
  @media (max-width: 768px) {
      .all-books-container {
          margin-top: 80px;
          padding: 0 15px;
      }
      
      .header-title {
          font-size: 2rem;
      }
      
      .allbooksread-img {
          height: 250px;
      }
      
      .books-grid {
          grid-template-columns: repeat(2, 1fr);
          gap: 15px;
      }
      
      .book-image {
          height: 240px;
      }
  }
  
  @media (max-width: 480px) {
      .books-grid {
          grid-template-columns: 1fr;
      }
      
      .stats-container {
          flex-direction: column;
          gap: 8px;
      }
      
      .pagination {
          gap: 10px;
      }
      
      .pagination-button {
          padding: 8px 15px;
          font-size: 0.9rem;
      }
  }
  </style>