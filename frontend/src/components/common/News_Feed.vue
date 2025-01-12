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
      <div v-for="(post, index) in posts" :key="post.id" class="news-post">
        <img :src="post.image_url" alt="Post Image" class="post-image" />
        <p class="post-date">{{ formatDate(post.created_at) }}</p>
        <h2>{{ post.title }}</h2>
        <button 
          @click="togglePost(post.id)"
          :class="{'no-border-line': index === 1}"
        >
          {{ expandedPosts[post.id] ? 'Collapse' : 'Read' }}
        </button>
        <div 
          v-show="expandedPosts[post.id]" 
          class="post-content"
          :style="expandedPosts[post.id] ? { height: 'auto' } : { height: '0' }"
        >
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
      expandedPosts: {},
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
    togglePost(postId) {
      this.expandedPosts[postId] = !this.expandedPosts[postId];
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

button {
  background: #f8f4ef;
  color: black;
  border: 1px solid black;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: 10px;
  border-radius: 0;
  font-size: 15px;
  text-align: center;
}

button:hover {
  padding: 10px 20px; /* Removed extra padding on hover */
  border-left: 1px solid black;
  border-right: 1px solid black;
}

/* Remove the button hover animations */
button:before, button:after {
  content: none;
}


.post-content {
  margin-top: 15px;
  text-align: justify;
  font-size: 16px;
  color: #333;
  line-height: 1.6;
  max-width: 100%;
  overflow: hidden;
  white-space: pre-wrap;
  height: 0;
  transition: height 0.5s ease;
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

/* Style to remove the border line for the second post */
.no-border-line:before, .no-border-line:after {
  content: none;
}

</style>
