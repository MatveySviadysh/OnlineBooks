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
        <div v-for="book in filteredAudioBooks" :key="book._id" :class="['book-card', viewMode]">
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
      childrenBooks: [],
      audioBooks: [], // Initialize as an empty array
      viewMode: 'grid'
    }
  },

  computed: {
    filteredAudioBooks() {
      // Ensure audioBooks is an array before applying filter
      if (Array.isArray(this.audioBooks)) {
        return this.audioBooks.filter(book => book.audio_file_path && book.audio_file_path.trim() !== ''  && book.audio_file_path.trim() !== "string");
      }
      return []; // Return an empty array if audioBooks is not an array
    }
  },

  async created() {
    try {
      const [popularResponse, recentResponse, childrenResponse, audioResponse] = await Promise.all([
        fetch('http://127.0.0.1:8001/api/books/books/popular?skip=0&limit=12'),
        fetch('http://127.0.0.1:8001/api/books/books/recent?skip=0&limit=12'),
        fetch('http://localhost:8001/api/children_and_perents/children_and_perents/'),
        fetch('http://127.0.0.1:8001/api/book/book/popular-with-audio?skip=0&limit=12') // Audiobooks API
      ]);

      this.popularBooks = await popularResponse.json();
      this.recentBooks = await recentResponse.json();
      
      const childrenData = await childrenResponse.json();
      this.childrenBooks = await Promise.all(
        childrenData.book_ids.map(async (bookId) => {
          const bookResponse = await fetch(`http://localhost:8001/api/books/books/${bookId}`);
          return bookResponse.json();
        })
      );

      // Set the audiobooks directly from the response
      this.audioBooks = await audioResponse.json();

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

  .books-list {
    display: flex;
    overflow-x: auto; /* Горизонтальная прокрутка */
    gap: 1rem;
    padding: 1rem;
    height: calc(100% - 60px); /* Высота списка книг (высота блока минус высота заголовка) */
  }

  .book-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    flex: 0 0 140px;
    height: 260px; /* Высота карточки книги */
    border-radius: 10px;
    background-color: #fff;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Тень для карточек */
  }

  .book-details-author-title {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .book-details-title {
    font-size: 16px; /* Размер шрифта для названия книги */
    font-weight: bold; /* Жирный шрифт */
  }

  .book-details-author {
    font-size: 14px; /* Размер шрифта для автора */
    color: #666;
  }

  .details-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none; /* Убираем подчеркивание */
  }

  .details-button:hover .book-image {
    transform: scale(1.05);
    transition: transform 0.3s ease;
  }

  .grid .book-card {
    flex: 0 0 160px; /* Увеличиваем размер карточки в grid */
  }

  .list .book-card {
    flex: 0 0 100%; /* Карточки в list будут занимать всю ширину */
  }

  .grid .books-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 1rem;
  }

  .list .books-list {
    display: block;
  }
  </style>
