<template>
    <div class="news-feed">
      <h1>Литературная Новостная Лента</h1>
      <div v-for="post in posts" :key="post.id" class="news-post">
        <h2>{{ post.title }}</h2>
        <img :src="post.image_url" alt="Post Image" class="post-image" />
        <p>{{ post.content }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        posts: [] // Изначально массив постов пуст
      };
    },
    async mounted() { // Загружаем данные при монтировании компонента
      await this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        try {
          const response = await fetch('http://127.0.0.1:8001/api/news_feed/news_feed/?skip=0&limit=10');
          
          if (!response.ok) {
            throw new Error('Ошибка сети');
          }
          
          const data = await response.json();
          this.posts = data; // Обновляем массив постов данными из API
        } catch (error) {
          console.error('Ошибка загрузки новостей:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .news-feed {
    max-width: 800px;
    margin: auto;
    padding: 20px;
  }
  
  .news-post {
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 20px;
    padding: 15px;
  }
  
  .post-image {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
  }
  </style>
  