<template>
  <div class="news-feed">
    <div v-if="isLoading" class="loading-screen">
      <div class="cube-loader">
        <div class="cube">
          <div class="face front"></div>
          <div class="face back"></div>
          <div class="face left"></div>
          <div class="face right"></div>
          <div class="face top"></div>
          <div class="face bottom"></div>
        </div>
      </div>
    </div>

    <div v-else>
      <div v-for="post in posts" :key="post.id" class="news-post">
        <img :src="post.image_url" alt="Post Image" class="post-image" />
        <p class="post-date">{{ formatDate(post.created_at) }}</p>
        <h2>{{ post.title }}</h2>
        <div class="post-content">
          {{ post.content }}
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import '@/styles/components/common/News_Feed.scss';

export default {
  data() {
    return {
      posts: [],
      isLoading: true,
    };
  },
  async mounted() {
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
        this.posts = data;
      } catch (error) {
        console.error('Ошибка загрузки новостей:', error);
      } finally {
        setTimeout(() => {
          this.isLoading = false;
        }, 1000);
      }
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    },
  },
};
</script>

<style scoped>
.news-feed {
  margin: 50px auto 0;
  max-width: 680px;
  padding: 20px;
  text-align: center;
  box-sizing: border-box;
}

h2 {
  font-size: 38px;
  font-weight: 600;
  color: rgb(36, 36, 36);
  margin-bottom: 10px;
  letter-spacing: -0.2px;
  word-wrap: break-word;
  overflow-wrap: break-word;
  text-align: left;
}

.news-post {
  margin-bottom: 20px;
  padding: 20px;
  text-align: center;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.post-date {
  font-size: 12px;
  color: gray;
  text-align: left;
  font-style: italic;
}

.post-image {
  max-width: 100%;
  height: auto;
}

.post-content {
  margin-top: 15px;
  text-align: justify;
  font-size: 16px;
  color: #333;
  line-height: 1.6;
  max-width: 100%;
  white-space: pre-wrap;
}

.loading-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.cube-loader {
  perspective: 1400px;
}

.cube {
  position: relative;
  width: 140px;
  height: 140px;
  transform-style: preserve-3d;
  animation: rotate-cube 3s infinite linear;
}

.face {
  position: absolute;
  width: 140px;
  height: 140px;
  background: rgba(255, 255, 255, 1);
  border: 2px solid #000;
}

.front { transform: rotateY(0deg) translateZ(70px); }
.back { transform: rotateY(180deg) translateZ(70px); }
.left { transform: rotateY(-90deg) translateZ(70px); }
.right { transform: rotateY(90deg) translateZ(70px); }
.top { transform: rotateX(90deg) translateZ(70px); }
.bottom { transform: rotateX(-90deg) translateZ(70px); }

@keyframes rotate-cube {
  0% {
    transform: rotateX(0deg) rotateY(0deg);
  }
  100% {
    transform: rotateX(360deg) rotateY(360deg);
  }
}
</style>
