<template>
  <div class="books-container">
    <!-- Popular Block -->
    <div class="books-row">
      <div class="header-row">
        <div class="title-container">
          <div class="title-header-row">Popular Books</div>
          <div class="title-header-row-mini">most popular books on the site</div>
        </div>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'popular' }}" 
          class="more-button"
        >
          more >
        </router-link>
      </div>
      <div :class="['books-list', viewMode]">
        <div v-for="book in popularBooks" :key="book._id" :class="['book-card', viewMode]">
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
    <!-- New Releases Block -->
    <div class="books-row">
      <div class="header-row">
        <div class="title-container">
          <div class="title-header-row">New Releases</div>
          <div class="title-header-row-mini">recently uploaded books to the site</div>
        </div>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'recent' }}" 
          class="more-button"
        >
          more >
        </router-link>
      </div>

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

    <!-- Audiobooks Block -->
    <div class="books-row">
      <div class="header-row">
        <div class="title-container">
          <div class="title-header-row">Audiobooks</div>
          <div class="title-header-row-mini">books available in audio format</div>
        </div>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'audio' }}" 
          class="more-button"
        >
          more >
        </router-link>
      </div>

      <div :class="['books-list', viewMode]">
        <div v-for="book in audioBooks" :key="book._id" :class="['book-card', viewMode]">
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

    <!-- Children and Parents Block -->
    <div class="books-row">
      <div class="header-row">
        <div class="title-container">
          <div class="title-header-row">Children and Parents</div>
          <div class="title-header-row-mini">books for children and their parents</div>
        </div>
        <router-link 
          :to="{ name: 'AllBooks', query: { type: 'children' }}" 
          class="more-button"
        >
          more >
        </router-link>
      </div>

      <div :class="['books-list', viewMode]">
        <div v-for="book in childrenBooks" :key="book._id" :class="['book-card', viewMode]">
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
    </div>  </div>
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
        fetch('http://127.0.0.1:8001/api/books/books/popular?skip=0&limit=12'),
        fetch('http://127.0.0.1:8001/api/books/books/recent?skip=0&limit=12')
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
.book-image{
  width: 123px;
  height: 176px;
  object-fit: cover;
  border-radius: 5px;
}
.books-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 1200px; /* Фиксированная ширина контейнера */
  margin: 0 auto;
  margin-top: 100px;
  margin-bottom: 100px; /* Центрирование контейнера */
}

.books-row {
  width: 100%;
  height: 393px; /* Фиксированная высота блока */
  background-color: #f9f9f9; /* Фон блока */
  border-radius: 10px; /* Скругление углов */
  padding: 1rem; /* Внутренние отступы */
  overflow: hidden; /* Скрываем содержимое, выходящее за пределы блока */
}

.header-row {
  height: 73px;
  display: flex;
  justify-content: space-between;
  align-items: center; /* Выравниваем элементы по вертикали */
}

.title-container {
  display: flex;
  flex-direction: column; /* Размещаем заголовок и подзаголовок вертикально */
  gap: 4px; /* Расстояние между заголовком и подзаголовком */
}

.title-header-row {
  font-size: 20px; /* Размер шрифта для заголовка */
  font-weight: bold; /* Жирный шрифт для заголовка */
}

.title-header-row-mini {
  font-size: 14px; /* Размер шрифта для подзаголовка */
  color: #666; /* Цвет подзаголовка */
}

.more-button {
  font-size: 16px;
  color: #000000; /* Цвет кнопки "more" */
  font-weight: 500;
  text-decoration: none; /* Убираем подчеркивание */
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

.books-list {
  display: flex;
  overflow-x: auto; /* Горизонтальная прокрутка */
  gap: 1rem;
  padding: 1rem;
  height: calc(100% - 60px); /* Высота списка книг (высота блока минус высота заголовка) */
}

.book-card {
  width: 111px;
  height: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
}

.details-button {
  margin-top: 0.5rem;
  text-decoration: none;
  color: #007bff;
}

.details-button:hover {
  text-decoration: underline;
}



.book-card.list {
  min-width: 100%;
  flex-direction: row;
  gap: 1rem;
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

.book-details-author-title {
  margin: 0; /* Убираем внешние отступы у контейнера */
  padding: 0;
  text-align: left; /* Убираем внутренние отступы у контейнера */
}

.book-details-author-title div {
  margin: 0; /* Убираем отступы у элементов */
  padding: 2px; /* Убираем внутренние отступы у элементов */
  line-height: 1.2; 
}
.book-details-title{
  color:rgb(0, 0, 0)
}
.book-details-author{
  color:rgb(178, 159, 159)
}
</style>