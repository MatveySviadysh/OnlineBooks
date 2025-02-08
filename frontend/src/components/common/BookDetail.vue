<template>
  <div class="book-container">
    <h1>Детали книги: {{ book.title }}</h1>
    <div class="book-info">
      <div class="left-column">
        <img :src="book.image" alt="Обложка книги" class="book-cover" />
        <div class="buttons">
          <button @click="goToBookReader">Читать книгу</button>
          <button @click="getBookContent">Получить текст книги</button>
          <button v-if="book.audio_file_path" @click="goToBookListen">Слушать книгу</button>
          <button @click="likeBook">👍 Нравится</button>
          <button @click="dislikeBook">👎 Не нравится</button>
        </div>
      </div>
      <div class="right-column">
        <p><strong>Автор:</strong> {{ book.author }}</p>
        <p><strong>Жанр:</strong> {{ book.genre }}</p>
        <p><strong>Дата публикации:</strong> {{ book.publication_date }}</p>
        <p><strong>Язык:</strong> {{ book.language }}</p>
        <p><strong>Количество страниц:</strong> {{ book.page_count }}</p>
        <p><strong>Рейтинг:</strong> {{ book.rating }}</p>
        <p><strong>Ссылка на файл:</strong> {{ book.file_url }}</p>
        <p><strong>ID книги:</strong> {{ id }}</p>
        <p v-if="book.audio_file_path">{{ book.audio_file_path }}</p>

        <div class="comment-section">
          <h3>Оставить комментарий</h3>
          <textarea v-model="comment" placeholder="Напишите ваш комментарий здесь..." disabled></textarea>
        </div>

        <div v-if="content" class="book-content">
          <h2>Содержимое книги:</h2>
          <pre>{{ content }}</pre>
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
      book: {}, // Здесь будем хранить информацию о книге
      content: '', // Это свойство будет хранить текст книги
      comment: '', // Поле для комментария
      likes: 0,
      dislikes: 0
    }
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
    goToBookListen() {
      this.$router.push({ 
        name: 'BookListen', 
        params: { 
          id: this.id, 
        } 
      });
    },
    goToBookReader() {
      this.$router.push({ name: 'BookReader', params: { id: this.id } });
    },
    async getBookContent() {
      try {
        const response = await fetch(`http://127.0.0.1:8001/api/books/books/content/${this.id}`, {
          method: 'GET',
          headers: {
            'accept': 'application/json'
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP статус: ${response.status}`);
        }
        this.content = await response.json();
      } catch (error) {
        console.error('Ошибка при загрузке содержимого книги:', error);
      }
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
}
</script>

<style scoped>
.book-container {
  width: 1200px;
  height: 1000px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

h1 {
  font-size: 24px;
  margin-bottom: 1rem;
  text-align: center;
}

.book-info {
  margin-top: 20px;
  display: flex;
  gap: 30px;
}

.left-column {
  flex: 0 0 300px;
}

.right-column {
  flex: 1;
}

p {
  margin: 0.5rem 0;
}

.book-cover {
  width: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

button {
  width: 100%;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.book-content {
  margin-top: 20px;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
}

pre {
  white-space: pre-wrap;
  font-family: Arial, sans-serif;
  line-height: 1.5;
}

.comment-section {
  margin-top: 20px;
}

textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  resize: vertical;
  background-color: #f0f0f0;
}

textarea:disabled {
  cursor: not-allowed;
}
</style>