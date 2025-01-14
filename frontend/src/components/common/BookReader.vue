<template>
    <div>
      <h1>Детали книги: {{ book.title }}</h1>
      <p><strong>Автор:</strong> {{ book.author }}</p>
      <p><strong>Жанр:</strong> {{ book.genre }}</p>
      <p><strong>Дата публикации:</strong> {{ book.publication_date }}</p>
      <p><strong>Язык:</strong> {{ book.language }}</p>
      <p><strong>Количество страниц:</strong> {{ book.page_count }}</p>
      <p><strong>Рейтинг:</strong> {{ book.rating }}</p>
      <p><strong>Ссылка на файл:</strong> {{ book.file_url }}</p>
      <p><strong>ID книги:</strong> {{ id }}</p>
      
      <div v-if="content">
        <h2>Содержимое книги:</h2>
        <pre>{{ content }}</pre>
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
        content: '' // Это свойство будет хранить текст книги
      }
    },
    async created() {
      try {
        // Получить информацию о книге
        const response = await fetch(`http://127.0.0.1:8001/api/books/books/${this.id}`);
        if (!response.ok) {
          throw new Error(`HTTP статус: ${response.status}`);
        }
        this.book = await response.json();
        
        // Получить содержимое книги
        await this.getBookContent(); // Загрузить текст книги сразу при создании компонента
      } catch (error) {
        console.error('Ошибка при загрузке деталей книги:', error);
      }
    },
    methods: {
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
      }
    }
  }
  </script>
  
  <style scoped>
  h1 {
    font-size: 24px;
    margin-bottom: 1rem;
  }
  p {
    margin: 0.5rem 0;
  }
  button {
    margin-top: 1rem;
  }
  </style>
  