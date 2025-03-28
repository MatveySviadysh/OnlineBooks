<template>
  <div class="all-books-container">
    <h1>{{ pageTitle }}</h1>
    <div class="books-grid">
      <div v-for="book in displayBooks" :key="book._id" class="book-card">
        <router-link :to="{ name: 'BookDetail', params: { id: book._id || book } }">
          <img :src="getBookImage(book)" :alt="book.title" class="book-image" />
          <div class="book-details">
            <h3 class="book-title">{{ book.title }}</h3>
            <div class="book-author">{{ book.author }}</div>
            <StarRating :rating="book.rating" />
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from '@/components/help/StarRating.vue';

export default {
  name: 'AllBooks',
  components: {
    StarRating,
  },
  data() {
    return {
      books: {},
      type: '',
      childrenBooks: {},
    };
  },
  computed: {
    pageTitle() {
      switch (this.type) {
        case 'popular':
          return 'Popular books';
        case 'recent':
          return 'New books';
        case 'audio':
          return 'Audiobooks';
        case 'children':
          return 'Books for children and their parents';
        default:
          return 'Все книги';
      }
    },
    displayBooks() {
      if (this.type === 'children' && this.books.book_ids) {
        return this.books.book_ids.map(id => this.childrenBooks[id] || { _id: id });
      }
      return this.books.book_ids || this.books;
    }
  },
  methods: {
    getBookImage(book) {
      if (this.type === 'children' && this.childrenBooks[book._id]) {
        return this.childrenBooks[book._id].image;
      }
      return book.image;
    },
    async fetchChildrenBookDetails(bookId) {
      try {
        const response = await fetch(`http://localhost:8001/api/books/books/${bookId}`);
        const bookData = await response.json();
        this.childrenBooks[bookId] = bookData;
      } catch (error) {
        console.error('Ошибка при загрузке детской книги:', error);
      }
    },
    async loadBooks() {
      try {
        if (this.type === 'children') {
          const response = await fetch('http://localhost:8001/api/children_and_perents/children_and_perents/');
          this.books = await response.json();
        } else {
          const response = await fetch(`http://localhost:8001/api/books/books/${this.type}`);
          this.books = await response.json();
        }

        if (this.type === 'children' && this.books.book_ids) {
          await Promise.all(
            this.books.book_ids.map(bookId => this.fetchChildrenBookDetails(bookId))
          );
        }
      } catch (error) {
        console.error('Ошибка при загрузке книг:', error);
      }
    }
  },
  async created() {
    this.type = this.$route.query.type || '';
    await this.loadBooks();
  }
};
</script>


<style scoped>
.all-books-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 100px auto 0;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #333;
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 2rem;
}

.book-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.book-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.book-card a {
  text-decoration: none;
  color: inherit;
}

.book-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.book-details {
  padding: 1rem;
  text-align: center;
}

.book-title {
  font-size: 1.1rem;
  margin: 0.5rem 0;
  color: #333;
}

.book-author {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}
</style>
