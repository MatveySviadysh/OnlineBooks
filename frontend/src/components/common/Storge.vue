<template>
    <div class="storage-container">
      <header class="storage-header">
        <h1>Хранилище Сохранённых Книг</h1>
        <button @click="addBook" class="add-book-btn">Добавить Книгу</button>
      </header>
  
      <div class="books-list">
        <div v-if="books.length === 0" class="no-books-message">
          <p>Здесь пока нет сохранённых книг.</p>
        </div>
  
        <div v-else class="books-grid">
          <div v-for="(book, index) in books" :key="index" class="book-item">
            <div class="book-cover">
              <img :src="book.coverImage" alt="Book Cover">
            </div>
            <div class="book-details">
              <h3>{{ book.title }}</h3>
              <p>{{ book.author }}</p>
              <button @click="removeBook(index)" class="remove-book-btn">Удалить</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StoragePage',  // Измените на составное имя компонента
    data() {
      return {
        books: [
          {
            title: 'Книга 1',
            author: 'Автор 1',
            coverImage: 'https://via.placeholder.com/100x150'
          },
          {
            title: 'Книга 2',
            author: 'Автор 2',
            coverImage: 'https://via.placeholder.com/100x150'
          }
        ]
      };
    },
    methods: {
      addBook() {
        // Логика добавления книги
        const newBook = {
          title: 'Новая Книга',
          author: 'Новый Автор',
          coverImage: 'https://via.placeholder.com/100x150'
        };
        this.books.push(newBook);
      },
      removeBook(index) {
        this.books.splice(index, 1);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Стили */
  </style>
  