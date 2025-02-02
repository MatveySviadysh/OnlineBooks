<template>
  <h1 class="authors-title">Authors</h1>
  
  <!-- Search Input -->
  <div class="search">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Search by first name, last name, or patronymic..." 
        @input="filterAuthors"
      />
  </div>

  <!-- Sorting Dropdown -->
  <div class="sort-dropdown">
    <button @click="toggleSortMenu" class="sort-button">
      Sort by: {{ sortOption }}
    </button>
    <div v-if="isSortMenuVisible" class="sort-menu">
      <button @click="sortAuthors('first_name')">First Name (A-Z)</button>
      <button @click="sortAuthors('last_name')">Last Name (A-Z)</button>
      <button @click="sortAuthors('birth_date')">Birth Date (Oldest First)</button>
    </div>
  </div>

  <!-- Authors List -->
  <div class="authors-list">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="authors-grid">
      <div v-for="author in filteredAuthors" :key="author.id" class="author-card">
        <router-link :to="`/authors/details/${author.id}`" class="author-link">
          <div class="author-photo">
            <img v-if="author.photo" :src="author.photo" :alt="`Photo of ${author.first_name} ${author.last_name}`" />
            <span v-else>No photo</span>
          </div>
          <div class="author-details">
            <h3>{{ author.first_name }} {{ author.last_name }}</h3>
            <p>{{ author.patronymic }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

interface Author {
  id: number;
  first_name: string;
  last_name: string;
  patronymic: string;
  birth_date: string;
  death_date: string;
  bio: string;
  photo: string;
}

export default defineComponent({
  name: 'AuthorsList',
  data() {
    return {
      authors: [] as Author[],
      loading: true,
      error: '' as string | null,
      searchQuery: '' as string,
      filteredAuthors: [] as Author[],
      isSortMenuVisible: false,
      sortOption: 'First Name' as string,
    };
  },
  created() {
    this.fetchAuthors();
  },
  methods: {
    async fetchAuthors() {
      try {
        this.loading = true;
        const response = await axios.get('http://127.0.0.1:8000/v1/authors/all/');
        this.authors = response.data;
        this.filteredAuthors = this.authors;
        this.error = null;
      } catch (error) {
        this.error = 'Error loading authors list';
      } finally {
        this.loading = false;
      }
    },
    filterAuthors() {
      if (!this.searchQuery) {
        this.filteredAuthors = this.authors;
      } else {
        this.filteredAuthors = this.authors.filter(author =>
          author.first_name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          author.last_name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          author.patronymic.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    },
    toggleSortMenu() {
      this.isSortMenuVisible = !this.isSortMenuVisible;
    },
    sortAuthors(criteria: string) {
      if (criteria === 'first_name') {
        this.filteredAuthors.sort((a, b) => a.first_name.localeCompare(b.first_name));
        this.sortOption = 'First Name';
      } else if (criteria === 'last_name') {
        this.filteredAuthors.sort((a, b) => a.last_name.localeCompare(b.last_name));
        this.sortOption = 'Last Name';
      } else if (criteria === 'birth_date') {
        this.filteredAuthors.sort((a, b) => new Date(a.birth_date).getTime() - new Date(b.birth_date).getTime());
        this.sortOption = 'Birth Date';
      }
      this.isSortMenuVisible = false; // Close the menu after selecting an option
    }
  }
});
</script>

<style scoped>
.authors-list {
  text-align: center;
  padding: 20px;
  background-color: #f7f7f7;
}

.search {
  margin: 20px auto;
  display: flex;
  justify-content: center;
}

.search input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: center;
}

/* Sorting Dropdown Styles */
.sort-dropdown {
  position: relative;
  margin-top: 10px;
}

.sort-button {
  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.sort-button:hover {
  background-color: #0056b3;
}

.sort-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  width: 180px;
  text-align: left;
  margin-top: 5px;
}

.sort-menu button {
  padding: 8px;
  font-size: 14px;
  width: 100%;
  text-align: left;
  background-color: white;
  border: none;
  cursor: pointer;
}

.sort-menu button:hover {
  background-color: #f1f1f1;
}

/* Authors Grid Styles */
.authors-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 5px;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  max-width: 620px;
  margin-left: auto;
  margin-right: auto;
}

.author-card {
  width: 300px;
  height: 50px;
  display: flex;
  align-items: center;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 5px;
  justify-content: flex-start;
}

.author-photo {
  width: 40px;
  height: 40px;
  border-radius: 4px;
  overflow: hidden;
  margin-right: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ddd;
}

.author-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.author-details {
  text-align: left;
  flex-grow: 1;
}

.author-details h3 {
  font-size: 16px;
  color: #333;
  margin: 0;
}

.authors-title {
  margin-top: 100px;
}
</style>
