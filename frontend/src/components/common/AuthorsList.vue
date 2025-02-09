<!-- Only changing the v-model.lazy to v-model and adding debounce to the @input event -->
<template>
  <div class="authors-container">
    <h1 class="authors-title">Authors</h1>
    
    <!-- Controls Section -->
    <div class="controls-section">
      <div class="search-container">
        <input
          v-model.trim="searchQuery"
          type="text"
          placeholder="Search authors..."
          class="search-input"
          @input="debounceSearch"
        >
        <svg class="search-icon" viewBox="0 0 24 24">
          <path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 0 0 1.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 0 0-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 0 0 5.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
        </svg>
      </div>

      <div class="sort-container">
        <button class="sort-button" @click="toggleSortMenu">
          <span>{{ sortOption }}</span>
          <svg :class="['dropdown-icon', { 'open': isSortMenuVisible }]" viewBox="0 0 24 24">
            <path d="M7 10l5 5 5-5z"/>
          </svg>
        </button>
        <transition name="fade">
          <div v-if="isSortMenuVisible" class="sort-menu">
            <button 
              v-for="option in sortOptions" 
              :key="option.key"
              @click="sortAuthors(option.key)"
              :class="{ 'active': sortOption === option.label }"
            >
              {{ option.label }}
            </button>
          </div>
        </transition>
      </div>
    </div>

    <!-- Content -->
    <div class="content">
      <div v-if="loading" class="loading-container">
        <div v-for="i in 3" :key="i" class="skeleton-card"></div>
      </div>
      
      <template v-else>
        <div v-if="error" class="error-message">
          ⚠️ {{ error }}
        </div>

        <div v-else-if="filteredAuthors.length" class="authors-grid">
          <router-link 
            v-for="author in filteredAuthors" 
            :key="author.id" 
            :to="`/authors/details/${author.id}`"
            class="author-card"
          >
            <div class="author-avatar">
              <template v-if="author.photo">
                <img :src="author.photo" :alt="`${author.first_name} ${author.last_name}`">
              </template>
              <div v-else class="avatar-placeholder">
                {{ getInitials(author) }}
              </div>
            </div>
            <div class="author-info">
              <h3>{{ fullName(author) }}</h3>
              <p v-if="author.birth_date" class="birthdate">
                {{ formatDate(author.birth_date) }}
              </p>
            </div>
          </router-link>
        </div>

        <div v-else class="empty-state">
          <svg class="empty-icon" viewBox="0 0 24 24">
            <path d="M12 5.99L19.53 19H4.47L12 5.99M12 2L1 21h22L12 2zm1 14h-2v2h2v-2zm0-6h-2v4h2v-4z"/>
          </svg>
          <p>No authors found</p>
        </div>
      </template>
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
  patronymic?: string;
  birth_date?: string;
  death_date?: string;
  bio?: string;
  photo?: string;
}

interface SortOption {
  key: string;
  label: string;
}

export default defineComponent({
  name: 'AuthorsList',
  data() {
    return {
      authors: [] as Author[],
      loading: true,
      error: null as string | null,
      searchQuery: '',
      filteredAuthors: [] as Author[],
      isSortMenuVisible: false,
      sortOptions: [
        { key: 'first_name', label: 'First Name' },
        { key: 'last_name', label: 'Last Name' },
        { key: 'birth_date', label: 'Birth Date' }
      ] as SortOption[],
      sortOption: 'First Name',
      debounceTimeout: null as ReturnType<typeof setTimeout> | null
    };
  },
  computed: {
    currentSortOption(): SortOption {
      return this.sortOptions.find(opt => opt.label === this.sortOption) || this.sortOptions[0];
    }
  },
  created() {
    this.fetchAuthors();
  },
  methods: {
    debounceSearch: function() {
      if (this.debounceTimeout) {
        clearTimeout(this.debounceTimeout);
      }
      this.debounceTimeout = setTimeout(() => {
        this.filterAuthors();
      }, 300);
    },

    async fetchAuthors() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/v1/authors/all/');
        this.authors = response.data;
        this.filteredAuthors = [...this.authors];
      } catch (error) {
        this.error = 'Failed to load authors. Please try again later.';
        console.error('Error fetching authors:', error);
      } finally {
        this.loading = false;
      }
    },

    filterAuthors() {
      const query = this.searchQuery.toLowerCase().trim();
      if (!query) {
        this.filteredAuthors = [...this.authors];
      } else {
        this.filteredAuthors = this.authors.filter(author => {
          const fullName = `${author.first_name} ${author.last_name} ${author.patronymic || ''}`.toLowerCase();
          return fullName.includes(query);
        });
      }
      
      this.sortAuthors(this.currentSortOption.key);
    },

    toggleSortMenu() {
      this.isSortMenuVisible = !this.isSortMenuVisible;
    },

    sortAuthors(key: string) {
      const option = this.sortOptions.find(opt => opt.key === key);
      if (!option) return;

      this.sortOption = option.label;
      this.isSortMenuVisible = false;

      this.filteredAuthors.sort((a, b) => {
        const valA = a[key as keyof Author] || '';
        const valB = b[key as keyof Author] || '';
        
        if (key === 'birth_date') {
          return new Date(valA).getTime() - new Date(valB).getTime();
        }
        return String(valA).localeCompare(String(valB));
      });
    },

    fullName(author: Author): string {
      return [author.first_name, author.last_name].join(' ').trim();
    },

    getInitials(author: Author): string {
      return `${author.first_name[0]}${author.last_name[0]}`.toUpperCase();
    },

    formatDate(dateString: string): string {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    }
  }
});
</script>
<style scoped>
.authors-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.authors-title {
  font-size: 2.5rem;
  font-weight: 600;
  color: #1a1a1a;
  text-align: center;
  margin-bottom: 2.5rem;
}

.controls-section {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-container {
  position: relative;
  max-width: 500px;
}

.search-input {
  width: 100%;
  padding: 0.8rem 2.5rem 0.8rem 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #6b7280;
  box-shadow: 0 0 0 2px rgba(107, 114, 128, 0.1);
}

.search-icon {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 1.25rem;
  height: 1.25rem;
  fill: #6b7280;
}

.sort-container {
  position: relative;
}

.sort-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1rem;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
}

.sort-button:hover {
  background: #f8f8f8;
}

.dropdown-icon {
  width: 1rem;
  height: 1rem;
  fill: #4b5563;
  transition: transform 0.2s;
}

.dropdown-icon.open {
  transform: rotate(180deg);
}

.sort-menu {
  position: absolute;
  right: 0;
  top: calc(100% + 0.5rem);
  min-width: 160px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  z-index: 10;
}

.sort-menu button {
  width: 100%;
  padding: 0.75rem 1rem;
  text-align: left;
  background: none;
  border: none;
  cursor: pointer;
  transition: background 0.2s;
}

.sort-menu button:hover {
  background: #f8f8f8;
}

.sort-menu button.active {
  background: #f3f4f6;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s, transform 0.15s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-0.5rem);
}

.content {
  margin-top: 1.5rem;
}

.authors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.author-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem;
  background: white;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  transition: transform 0.2s, box-shadow 0.2s;
  text-decoration: none;
  color: inherit;
}

.author-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.author-avatar {
  flex-shrink: 0;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  overflow: hidden;
  background: #f3f4f6;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  color: #6b7280;
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.author-info h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
}

.birthdate {
  margin: 0.25rem 0 0;
  font-size: 0.875rem;
  color: #6b7280;
}

.loading-container {
  display: grid;
  gap: 1rem;
}

.skeleton-card {
  height: 80px;
  background: #f8f8f8;
  border-radius: 12px;
  animation: pulse 1.5s infinite;
}

.error-message {
  padding: 2rem;
  text-align: center;
  color: #dc2626;
  background: #fef2f2;
  border-radius: 8px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 3rem 1rem;
  color: #6b7280;
}

.empty-icon {
  width: 64px;
  height: 64px;
  fill: #e5e7eb;
}

@keyframes pulse {
  0%, 100% { opacity: 1 }
  50% { opacity: 0.5 }
}

@media (max-width: 640px) {
  .controls-section {
    grid-template-columns: 1fr;
  }

  .authors-title {
    font-size: 2rem;
  }
}
</style>