<template>
  <div class="book-container">
    <div class="book-info">
      <div class="left-column">
        <div class="book-cover" :class="{'no-cover': !book.image}">
          <img v-if="book.image" :src="book.image" alt="Обложка книги" />
          <span v-else>Нет обложки</span>
        </div>
        <div class="buttons">
          <button @click="goToBookReader">Читать книгу</button>
          <button v-if="book.audio_file_path && book.audio_file_path !== '' && book.audio_file_path !== 'string'" @click="goToBookListen">Слушать книгу</button>
        </div>
      </div>
      <div class="right-column">
        <p><strong>название:</strong> {{ book.title }}</p>
        <p><strong>Автор:</strong> {{ book.author }}</p>
        <p><strong>Жанр:</strong> {{ book.genre }}</p>
        <p><strong>Дата публикации:</strong> {{ book.publication_date }}</p>
        <p><strong>Рейтинг:</strong>
          <span>
            <span v-for="star in Math.floor(book.rating) || 0" :key="star" class="star">&#9733;</span>
            <span v-if="book.rating % 1 !== 0 && book.rating >= 0.5" class="star">&#9734;</span>
            <span v-for="emptyStar in (5 - Math.ceil(book.rating)) || 0" :key="emptyStar" class="star">&#9734;</span>
          </span>
        </p>
        <div class="like-dislike-buttons">
          <button class="like-button" @click="likeBook">Нравится</button>
          <button class="dislike-button" @click="dislikeBook">Не нравится</button>
          <button class="storage-button" @click="addToStorage">Добавить в хранилище</button>
        </div>
      </div>
    </div>

    <!-- Модальное окно с сообщением об успешном добавлении -->
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
  props: {
    id: {
      type: String,
      required: true
    },
    userEmail: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      book: {},
      likes: 0,
      dislikes: 0,
      showSuccessPopup: false // Управление отображением попапа
    };
  },
  async created() {
    try {
      const response = await fetch(`http://127.0.0.1:8001/api/books/books/${this.id}`);
      if (!response.ok) {
        throw new Error(`HTTP статус: ${response.status}`);
      }
      this.book = await response.json();
    } catch (error) {
      console.error('Ошибка при загрузке деталей книги:', error);
    }
  },
  methods: {
    async addToStorage() {
      try {
        const response = await axios.get('http://localhost:8001/api/users/me', { withCredentials: true });
        const userEmail = response.data.email;
        console.log('User Email:', userEmail);

        const storageResponse = await axios.get(`http://localhost:8001/api/storage/storage/storage-id-by-email/${userEmail}`);
        if (storageResponse.status !== 200 || !storageResponse.data) {
          throw new Error(`Storage not found for user: ${userEmail}`);
        }

        const storageId = storageResponse.data;
        console.log('Storage ID:', storageId);

        const addBookResponse = await axios.post(
          `http://localhost:8001/api/storage/storage/${storageId}/add-book/${this.book._id}`,
          {},
          { withCredentials: true }
        );

        if (addBookResponse.status === 200) {
          console.log('Book successfully added to storage');
          this.showSuccessPopup = true; // Показываем попап при успешном добавлении
        } else {
          throw new Error('Failed to add book to storage');
        }
      } catch (error) {
        console.error('Error:', error.message);
      }
    },

    closeSuccessPopup() {
      this.showSuccessPopup = false; // Закрываем попап
    },

    goToBookReader() {
      this.$router.push({ name: 'BookReader', params: { id: this.id } });
    },

    likeBook() {
      this.likes++;
      localStorage.setItem(`book_${this.id}_likes`, this.likes);
    },

    dislikeBook() {
      this.dislikes++;
      localStorage.setItem(`book_${this.id}_dislikes`, this.dislikes);
    }
  }
};
</script>

<style scoped>
/* Стили для модального окна */
.success-popup {
  background-color: #fffdf8;
  color: #333;
  padding: 20px;
  border-radius: 8px;
  position: fixed;
  top: 70px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: 300px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeIn 1s forwards, fadeOut 1s 2s forwards;
  text-align: center;
  font-size: 16px;
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

.popup-content {
  padding: 20px;
  background: white;
  border-radius: 8px;
  text-align: center;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateX(-50%) translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateX(-50%) translateY(20px);
  }
}


.book-container {
  width: 1200px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #e2e2e2;
  border-radius: 10px;
  overflow-y: auto;
  margin-top: 8%;
  margin-bottom: 60px;
}

.book-info {
  display: flex;
  gap: 30px;
}

.left-column {
  flex: 0 0 300px;
  text-align: center;
}

.right-column {
  flex: 1;
  text-align: left;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.book-cover {
  width: 100%;
  height: 400px; /* Устанавливаем фиксированную высоту */
  border-radius: 10px;
  margin-bottom: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.book-cover img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

.book-cover.no-cover {
  background-color: #dcdcdc; /* Цвет фона для отсутствующей обложки */
}

.book-cover.no-cover span {
  color: #888;
  font-size: 18px;
  font-weight: bold;
}

.book-cover-placeholder {
  width: 100%;
  height: 200px; /* Set a fixed height to maintain structure */
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  color: #888;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

button {
  padding: 8px 16px;
  background-color: #000;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  text-align: center;
}

button:hover {
  background-color: #3f3f3f;
}

.like-dislike-buttons {
  display: flex;
  gap: 12px;
  margin-top: 15px;
}

.like-button,
.dislike-button {
  background: #f8f4ef;
  color: #000;
  border: 2px solid #000;
  width: 100px;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-radius: 4px;
  padding: 6px;
}

.like-button:hover,
.dislike-button:hover {
  background-color: #000;
  color: white;
}

.storage-button {
  background: #000;
  color: white;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-radius: 4px;
  width: 120px;
  padding: 6px;
  margin-top: 12px;
}

.storage-button:hover {
  background-color: #3f3f3f;
}

.book-details p {
  font-size: 14px;
  margin: 6px 0;
  color: #555;
}

.book-details strong {
  font-weight: bold;
}

.star {
  color: black;
  font-size: 16px;
}
</style>
