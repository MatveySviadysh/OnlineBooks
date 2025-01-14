<template>
  <div class="books-container">
    <div class="books-row">
      <div class="header-row">
        <div class="left-section">
          <h2>Популярные книги</h2>
          <div class="view-toggles">
            <button 
              :class="['view-button', { active: viewMode === 'grid' }]"
              @click="viewMode = 'grid'"
            >
              <i class="fas fa-th-large"></i>
            </button>
            <button 
              :class="['view-button', { active: viewMode === 'list' }]"
              @click="viewMode = 'list'"
            >
              <i class="fas fa-list"></i>
            </button>
          </div>
        </div>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'popular' }}" 
          class="more-button"
        >
          Показать все →
        </router-link>
      </div>
      <div :class="['books-list', viewMode]">
        <div v-for="book in popularBooks" 
             :key="book._id" 
             :class="['book-card', viewMode]">
          <img :src="book.cover" :alt="book.title" />
          <div class="book-info">
            <h3>{{ book.title }}</h3>
            <StarRating :rating="book.rating" />
            <router-link 
              :to="{ name: 'BookDetail', params: { id: book._id } }" 
              class="details-button"
            >
              Подробнее
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <div class="books-row">
      <div class="header-row">
        <h2>Новинки</h2>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'recent' }}" 
          class="more-button"
        >
          Показать все →
        </router-link>
      </div>
      <div class="books-list">
        <div v-for="book in recentBooks" :key="book.id" class="book-card">
          <img :src="book.cover" :alt="book.title" />
          <h3>{{ book.title }}</h3>
          <StarRating :rating="book.rating" />
          <router-link 
            :to="{ name: 'BookDetail', params: { id: book._id } }" 
            class="details-button"
          >
            Подробнее
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from '@/components/help/StarRating.vue'

export default {
  name: 'BooksList',
  components: {
    StarRating
  },
  data() {
    return {
      popularBooks: [],
      recentBooks: [],
      viewMode: 'grid'
    }
  },
  async created() {
    try {
      const [popularResponse, recentResponse] = await Promise.all([
        fetch('http://127.0.0.1:8001/api/books/books/popular?skip=0&limit=6'),
        fetch('http://127.0.0.1:8001/api/books/books/recent?skip=0&limit=6')
      ]);

      this.popularBooks = await popularResponse.json();
      this.recentBooks = await recentResponse.json();
    } catch (error) {
      console.error('Ошибка при загрузке книг:', error);
    }
  }
}
</script>

<style scoped>
/* Ваши стили остаются без изменений */
.books-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1rem;
}

.more-button {
  text-decoration: none;
  color: #007bff;
  font-weight: 500;
}

.more-button:hover {
  text-decoration: underline;
}

.books-row {
  width: 100%;
}

.books-list {
  display: flex;
  overflow-x: auto;
  gap: 1rem;
  padding: 1rem;
}

.book-card {
  min-width: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.details-button {
  margin-top: 0.5rem;
  text-decoration: none;
  color: #007bff;
}

.details-button:hover {
  text-decoration: underline;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.view-toggles {
  display: flex;
  gap: 0.5rem;
}

.view-button {
  padding: 0.5rem;
  border: 1px solid #ddd;
  background: white;
  cursor: pointer;
  border-radius: 4px;
}

.view-button.active {
  background: #007bff;
  color: white;
  border-color: #007bff;
}

.books-list.list {
  flex-direction: column;
  gap: 1rem;
}

.book-card.list {
  min-width: 100%;
  flex-direction: row;
  gap: 1rem;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.book-card.list img {
  width: 100px;
  height: 150px;
  object-fit: cover;
}

.book-card.list .book-info {
  text-align: left;
  flex-grow: 1;
}

.book-card.grid {
  min-width: 200px;
}
</style>
