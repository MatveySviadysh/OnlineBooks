<template>
    <div class="storage-container">
      <div class="books-list">
        <div v-if="books.length === 0" class="no-books-message">
          <p>No saved books here yet.</p>
        </div>
  
        <div v-else class="books-grid">
          <div v-for="(bookId) in books" :key="bookId" class="book-item">
            <div class="book-details" v-if="bookDetails[bookId]">
              <h3>{{ bookDetails[bookId].title }}</h3>
              <p>Author: {{ bookDetails[bookId].author }}</p>
              <p>Genre: {{ bookDetails[bookId].genre }}</p>
              <p>Description: {{ bookDetails[bookId].description }}</p>
            </div>
          </div>
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
        userEmail: ''
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
      async addBook() {
        console.log('Adding book...');
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

  .book-details {
    color: #333;
  }

  .book-details h3 {
    margin: 0 0 1rem 0;
    color: #2c3e50;
    font-size: 1.4rem;
  }

  .book-details p {
    margin: 0.5rem 0;
    line-height: 1.4;
    color: #666;
  }
  </style>
