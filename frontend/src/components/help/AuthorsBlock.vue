<template>
  <div class="authors-block" style="max-width: 1200px; margin: 0 auto;">
    <div class="authors-content">
      <div class="authors-image">
        <img src="../../assets/dostoevski.jpg" alt="Author Image">
      </div>
      <div class="authors-info">
        <h3 class="title">
           Discover Great Authors
        </h3>
        <p class="description">Dive into the world of literature. Explore books from timeless authors.</p>
        <router-link 
          to="/authors"
          class="authors-button"
        >
          Explore All Authors
        </router-link>
      </div>
    </div>
    <p class="footer-text">By OnlineBook</p>
  </div>
</template>

<script>
export default {
  name: 'AuthorsBlock'
}
</script>

<style scoped>
.authors-block {
  padding: 100px;
  position: relative;
}

.authors-content {
  display: flex;
  align-items: center;
  gap: 30px;
  background-color: #f5f5f5;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  position: relative;
}

.authors-content:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  transform: translateY(-5px);
}

.authors-content::before {
  content: "";
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 50px;
  height: 5px;
  background-color: #333;
  border-radius: 5px;
}

.authors-image {
  flex: 0 0 35%;
}

.authors-image img {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  object-fit: cover;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.authors-image img:hover {
  transform: scale(1.05);
}

.authors-info {
  flex: 1;
  text-align: left;
  animation: fadeIn 1s ease-in-out;
}

.title {
  font-size: 28px;
  font-weight: 700;
  color: #333;
  margin-bottom: 10px;
  line-height: 1.4;
}

.description {
  font-size: 18px;
  color: #666;
  margin-bottom: 20px;
  line-height: 1.6;
}

.authors-button {
  display: inline-block;
  padding: 14px 28px;
  background-color: #000;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  font-size: 18px;
  text-transform: uppercase;
  border: 1px solid transparent;
  width: 200px; /* initial width */
  transition: background-color 0.3s ease, transform 0.3s ease, width 0.3s ease;
}

.authors-button:hover {
  background-color: #4a4a4a;
  transform: scale(1.1);
}




.additional-text {
  font-size: 16px;
  color: #444;
  margin-top: 20px;
  line-height: 1.6;
}

.footer-text {
  position: absolute;
  bottom: 20px;
  right: 20px;
  font-size: 18px;
  font-style: italic;
  color: #666;
}

@media (max-width: 768px) {
  .authors-content {
    flex-direction: column;
    padding: 20px;
  }

  .authors-image {
    flex: 0 0 100%;
    margin-bottom: 20px;
  }

  .title {
    font-size: 24px;
  }

  .description {
    font-size: 16px;
  }

  

  .additional-text {
    font-size: 14px;
  }

  .footer-text {
    font-size: 16px;
  }
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
