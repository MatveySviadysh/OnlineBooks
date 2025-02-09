<template>
  <div>
    <!-- Индикатор загрузки -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-spinner">
        <div class="fancy-book">
          <div class="cover">
            <div class="spine"></div>
            <div class="pages-container">
              <div class="page"></div>
              <div class="page"></div>
              <div class="page"></div>
              <div class="page"></div>
              <div class="page"></div>
            </div>
            <div class="glare"></div>
          </div>
        </div>
        <p class="loading-text">Идет загрузка книги...</p>
      </div>
    </div>

    <!-- Контент после загрузки -->
    <div v-else class="book-reader">
      <div class="content-container">
        <h1>Детали книги: {{ book.title }}</h1>
        <p><strong>Автор:</strong> {{ book.author }}</p>

        <!-- Блок с содержимым книги -->
        <div v-if="content">
          <pre>{{ currentPageContent }}</pre>
          
          <!-- Пагинация -->
          <div class="pagination">
            <button 
              :disabled="currentPage === 1" 
              @click="currentPage--"
              class="pagination-btn"
            >
              Предыдущая
            </button>
            <span class="page-info">
              Страница {{ currentPage }} из {{ totalPages }}
            </span>
            <button 
              :disabled="currentPage === totalPages" 
              @click="currentPage++"
              class="pagination-btn"
            >
              Следующая
            </button>
          </div>
        </div>

        <!-- Сообщение об ошибке -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      book: {},
      content: '',
      isLoading: true,
      errorMessage: '',
      currentPage: 1,
      linesPerPage: 50
    }
  },
  computed: {
    contentLines() {
      return this.content.split('\n');
    },
    totalPages() {
      return Math.ceil(this.contentLines.length / this.linesPerPage);
    },
    currentPageContent() {
      const start = (this.currentPage - 1) * this.linesPerPage;
      const end = start + this.linesPerPage;
      return this.contentLines.slice(start, end).join('\n');
    }
  },
  async created() {
    try {
      const bookResponse = await fetch(`http://127.0.0.1:8001/api/books/books/${this.id}`);
      if (!bookResponse.ok) throw new Error('Ошибка загрузки данных книги');
      this.book = await bookResponse.json();

      await this.getBookContent();

    } catch (error) {
      this.errorMessage = `Ошибка: ${error.message}`;
      console.error(error);
    } finally {
      this.isLoading = false;
    }
  },
  methods: {
    async getBookContent() {
      const response = await fetch(`http://127.0.0.1:8001/api/books/books/content/${this.id}`, {
        method: 'GET',
        headers: { 'accept': 'application/json' }
      });
      if (!response.ok) throw new Error('Ошибка загрузки содержимого');
      this.content = await response.json();
    }
  }
}
</script>

<style scoped>
.book-reader {
  margin-top: 100px;
  display: flex;
  justify-content: center;
}

.content-container {
  width: 1200px;
  text-align: center;
}

.pagination {
  margin: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.pagination-btn {
  padding: 8px 16px;
  background-color: #2c3e50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.pagination-btn:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.pagination-btn:hover:not(:disabled) {
  background-color: #34495e;
}

.page-info {
  font-size: 1.1em;
  color: #2c3e50;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.98);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  perspective: 1000px;
}

.loading-spinner {
  text-align: center;
  transform-style: preserve-3d;
}

.fancy-book {
  position: relative;
  width: 220px;
  height: 300px;
  transform-style: preserve-3d;
  animation: bookFloat 4s ease-in-out infinite;
}

.cover {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #2c3e50 0%, #34495e 100%);
  border-radius: 6px 10px 10px 6px;
  transform-style: preserve-3d;
  box-shadow: 
    0 20px 50px rgba(0,0,0,0.3),
    0 0 0 1px rgba(255,255,255,0.1) inset,
    0 -5px 10px rgba(0,0,0,0.1) inset;
}

.spine {
  position: absolute;
  left: 0;
  width: 14px;
  height: 100%;
  background: linear-gradient(to right, #1a252f 0%, #2c3e50 100%);
  transform: translateZ(-8px);
  border-radius: 6px 0 0 6px;
  box-shadow: 
    -2px 0 5px rgba(0,0,0,0.2),
    0 0 5px rgba(0,0,0,0.1) inset;
}

.pages-container {
  position: absolute;
  top: 12px;
  left: 18px;
  right: 18px;
  bottom: 12px;
  overflow: hidden;
  background: #f5f5f5;
  box-shadow: 
    0 0 5px rgba(0,0,0,0.1) inset,
    0 0 15px rgba(0,0,0,0.05);
}

.page {
  position: absolute;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    #fff 0px, 
    #fff 24px, 
    #e0e0e0 25px
  );
  transform-origin: left center;
  animation: pageFlip 5s cubic-bezier(0.25, 0.1, 0.25, 1) infinite;
  filter: drop-shadow(-2px 0 2px rgba(0,0,0,0.02));
}

.page:nth-child(1) { animation-delay: 0.2s; z-index: 5; }
.page:nth-child(2) { animation-delay: 0.4s; z-index: 4; }
.page:nth-child(3) { animation-delay: 0.6s; z-index: 3; }
.page:nth-child(4) { animation-delay: 0.8s; z-index: 2; }
.page:nth-child(5) { animation-delay: 1.0s; z-index: 1; }

.glare {
  position: absolute;
  top: -50%;
  right: -30%;
  width: 60%;
  height: 200%;
  background: linear-gradient(45deg, 
    rgba(255,255,255,0) 0%,
    rgba(255,255,255,0.1) 50%,
    rgba(255,255,255,0) 100%
  );
  transform: rotateZ(30deg);
  animation: glare 6s ease-in-out infinite;
}

@keyframes pageFlip {
  0%, 25% {
    transform: rotateY(0) translateX(0) scale(1);
    opacity: 1;
  }
  30% {
    transform: rotateY(-15deg) translateX(-2px) scale(1.02);
  }
  40%, 60% {
    transform: rotateY(-160deg) translateX(-25px) scale(0.97);
    opacity: 0.7;
  }
  70% {
    transform: rotateY(-170deg) translateX(-30px) scale(0.95);
    opacity: 0;
  }
  75%, 100% {
    transform: rotateY(0) translateX(0) scale(1);
    opacity: 1;
  }
}

@keyframes bookFloat {
  0%, 100% { 
    transform: 
      translateY(0px) 
      rotateX(2deg) 
      rotateY(-2deg)
      rotateZ(-1deg);
  }
  50% { 
    transform: 
      translateY(-15px) 
      rotateX(-2deg) 
      rotateY(2deg)
      rotateZ(1deg);
  }
}

@keyframes textPulse {
  0%, 100% { 
    opacity: 0.9; 
    transform: translateY(0) scale(0.98);
    text-shadow: 0 0 10px rgba(44,62,80,0.1);
  }
  50% { 
    opacity: 1; 
    transform: translateY(-5px) scale(1.02);
    text-shadow: 0 5px 15px rgba(44,62,80,0.2);
  }
}

@keyframes glare {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.1; }
}

.loading-text {
  margin-top: 40px;
  font-size: 1.4em;
  color: #2c3e50;
  font-weight: 400;
  letter-spacing: 1.5px;
  animation: textPulse 2.5s ease-in-out infinite;
  font-family: 'Arial', sans-serif;
  text-transform: uppercase;
}

h1 {
  font-size: 2em;
  margin-bottom: 1rem;
  color: #2c3e50;
}

p {
  margin: 0.5rem 0;
  font-size: 1.1em;
  color: #34495e;
}

pre {
  background: #f8f8f8;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  font-family: monospace;
  white-space: pre-wrap;
  word-wrap: break-word;
  text-align: left;
}

.error-message {
  color: #e74c3c;
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #e74c3c;
  border-radius: 4px;
  background: #f8d7da;
}
</style>