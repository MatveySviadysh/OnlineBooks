<template>
  <div class="authors-block" style="max-width: 1200px; margin: 0 auto;">
    <div class="authors-content">
      <div class="authors-image">
        <img src="../../assets/dostoevski.jpg" alt="">
      </div>
      <div class="authors-info">
        <router-link 
          to="/authors"
          class="authors-button"
        >
          Все авторы
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthorsBlock'
}
</script>

<style scoped>
.authors-block {
  padding: 20px;
}

.authors-content {
  display: flex;
  align-items: center;
  gap: 30px;
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.authors-image {
  flex: 0 0 40%;
}

.authors-image img {
  width: 100%;
  height: auto;
  border-radius: 4px;
}

.authors-info {
  flex: 1;
  text-align: center;
}

.authors-button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #4a4a4a;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.authors-button:hover {
  background-color: #2a2a2a;
}
</style>
