<template>
  <div class="books-row">
    <div class="header-row">
      <div class="title-container">
        <div class="title-header-row">Recommended for you</div>
        <div class="title-header-row-mini">Based on your reading history and preferences</div>
      </div>
    </div>

    <div :class="['books-list', viewMode]">
      <div v-for="book in books" :key="book._id" :class="['book-card', viewMode]">
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
</template>

<script>
import axios from 'axios';
import StarRating from '@/components/help/StarRating.vue'

export default {
  name: 'BooksList',
  components: {
    StarRating
  },
  data() {
    return {
      books: [],
      viewMode: 'grid',
    };
  },
  async created() {
    try {
      const userResponse = await axios.get('http://localhost:8001/api/users/me', {
        withCredentials: true
      });
      
      const userData = userResponse.data;

      if (!userData.email) {
        console.error('Не удалось получить email пользователя');
        return;
      }

      const recommendationsResponse = await axios.get(`http://localhost:8001/api/recomend/recommend/?email=${encodeURIComponent(userData.email)}`);
      const recommendationsData = recommendationsResponse.data;

      if (!Array.isArray(recommendationsData) || recommendationsData.length === 0) {
        console.error('Рекомендации отсутствуют');
        return;
      }

      const bookIds = recommendationsData[0].book_ids;
      this.books = await Promise.all(
        bookIds.map(async (bookId) => {
          const bookResponse = await axios.get(`http://localhost:8001/api/books/books/${bookId}`);
          return bookResponse.data;
        })
      );

    } catch (error) {
      console.error('Ошибка при загрузке рекомендаций:', error);
    }
  },
};
</script>

<style scoped>
.book-image {
  width: 123px;
  height: 176px;
  object-fit: cover;
  border-radius: 5px;
}

.books-row {
  margin: 100px auto;
  width: 1200px;
  height: 393px;
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 1rem;
  overflow: hidden;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.header-row {
  height: 73px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.title-container {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.title-header-row {
  font-size: 20px;
  font-weight: bold;
}

.title-header-row-mini {
  font-size: 14px;
  color: #666;
}

.more-button {
  font-size: 16px;
  color: #000000;
  font-weight: 500;
  text-decoration: none;
}

.books-list {
  display: flex;
  overflow-x: auto;
  gap: 1rem;
  padding: 1rem;
  height: calc(100% - 60px);
  width: 100%;
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

.book-details-author-title {
  margin: 0;
  padding: 0;
  text-align: left;
}

.book-details-author-title div {
  margin: 0;
  padding: 2px;
  line-height: 1.2;
}

.book-details-title {
  color: rgb(0, 0, 0);
}

.book-details-author {
  color: rgb(178, 159, 159);
}
</style>
