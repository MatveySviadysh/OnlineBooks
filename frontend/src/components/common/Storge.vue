<template>
  <div class="storage-container">
    <div class="books-list">
      <div v-if="books.length === 0" class="no-books-message">
        <p>No saved books here yet.</p>
      </div>

      <div v-else class="books-grid">
        <div v-for="bookId in books" :key="bookId" class="book-item">
          <div v-if="bookDetails[bookId]" class="book-info">
            <div class="left-column">
              <div class="book-cover" :class="{'no-cover': !bookDetails[bookId].image}">
                <img v-if="bookDetails[bookId].image" :src="bookDetails[bookId].image" alt="Обложка книги" />
                <span v-else>Нет обложки</span>
              </div>
            </div>

            <div class="right-column">
              <p><strong>Название:</strong> {{ bookDetails[bookId].title }}</p>
              <p><strong>Автор:</strong> {{ bookDetails[bookId].author }}</p>
              <p><strong>Жанр:</strong> {{ bookDetails[bookId].genre }}</p>
              <p><strong>Дата публикации:</strong> {{ bookDetails[bookId].publication_date }}</p>
              <p><strong>Рейтинг:</strong>
                <span>
                  <span v-for="star in Math.floor(bookDetails[bookId].rating) || 0" :key="star" class="star">&#9733;</span>
                  <span v-if="bookDetails[bookId].rating % 1 !== 0 && bookDetails[bookId].rating >= 0.5" class="star">&#9734;</span>
                  <span v-for="emptyStar in (5 - Math.ceil(bookDetails[bookId].rating)) || 0" :key="emptyStar" class="star">&#9734;</span>
                </span>
              </p>
              <div class="buttons">
                <router-link 
                  :to="{ name: 'BookDetail', params: { id: bookId } }" 
                  class="details-button"
                >
                  <button>Просмотреть книгу</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Success popup -->
    <div v-if="showSuccessPopup" class="success-popup">
      <div class="popup-overlay" @click="closeSuccessPopup"></div>
      <div class="popup-content">
        <p>Книга успешно добавлена в хранилище!</p>
        <button @click="closeSuccessPopup">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StoragePage',
  data() {
    return {
      books: [],
      bookDetails: {},
      userEmail: '',
      showSuccessPopup: false
    };
  },
  async created() {
    await this.getUserData();
    await this.getStorageBooks();
  },
  methods: {
    async getUserData() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:8001/api/users/me', {
          headers: {
            'Authorization': `Bearer ${token}`
          },
          withCredentials: true
        });
        this.userEmail = response.data.email;
      } catch (error) {
        console.error('Error getting user data:', error);
        this.$router.push('/login');
      }
    },
    async getStorageBooks() {
      try {
        if (this.userEmail) {
          const token = localStorage.getItem('token');
          const response = await axios.get(`http://localhost:8001/api/storage/storage/books-by-email/${this.userEmail}`, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          this.books = response.data;
          await this.fetchBookDetails();
        }
      } catch (error) {
        console.error('Error getting books:', error);
        this.books = [];
      }
    },
    async fetchBookDetails() {
      try {
        const token = localStorage.getItem('token');
        for (const bookId of this.books) {
          const response = await axios.get(`http://localhost:8001/api/books/books/${bookId}`, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          this.bookDetails[bookId] = response.data;
        }
      } catch (error) {
        console.error('Error getting book details:', error);
      }
    },
    goToBookReader(bookId) {
      // Logic to go to the book reader page
    },
    goToBookListen(bookId) {
      // Logic to listen to the book's audio
    },
    likeBook(bookId) {
      // Logic to like the book
    },
    dislikeBook(bookId) {
      // Logic to dislike the book
    },
    addToStorage(bookId) {
      // Logic to add the book to the user's storage
      this.showSuccessPopup = true;
    },
    closeSuccessPopup() {
      this.showSuccessPopup = false;
    }
  }
};
</script>

<style scoped>
.storage-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.books-list {
  width: 100%;
}

.no-books-message {
  text-align: center;
  padding: 2rem;
  background: #f5f5f5;
  border-radius: 8px;
  margin-top: 2rem;
}

.books-grid {
  margin-top: 100px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

.book-item {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  transition: transform 0.2s ease;
}

.book-item:hover {
  transform: translateY(-5px);
}

.book-info {
  display: flex;
}

.left-column {
  flex: 1;
  padding-right: 1rem;
}

.book-cover {
  width: 100%;
  height: 300px;
  background-color: #f0f0f0;
  text-align: center;
  position: relative;
}

.book-cover img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

.no-cover {
  color: #777;
  font-size: 1.2rem;
}

.right-column {
  flex: 2;
}

.right-column p {
  margin: 0.5rem 0;
}

.right-column strong {
  color: #333;
}

.star {
  color: black;
}

.details-button button {
  padding: 0.7rem 1.5rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  display: block;
  margin-top: 1rem;
}

.details-button button:hover {
  background-color: #45a049;
}

.success-popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  text-align: center;
}

.popup-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
</style>
