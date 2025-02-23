<template>
  <div class="app-info-container">
    <div class="app-info-text">
      <h2>Read and Listen</h2>
      <p>Your favorite books at home and on the go, even without the internet</p>
      <button class="download-btn">Download the App</button>
    </div>
    <div class="app-image">
      <img class="app-photo" src="@/assets/Мобилка.png" alt="Main Image" />
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'AppInfo'
}
</script>

<style scoped>
.app-info-container {
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 50px;
  position: relative;
}

.app-info-text {
  text-align: center; /* Центрируем текст */
  margin-bottom: 40px; /* Увеличиваем отступ между текстом и картинкой */
}

.app-info-text h2 {
  font-size: 28px;
  font-weight: 700;
  color: #333;
  margin-bottom: 10px;
}

.app-info-text p {
  font-size: 18px;
  color: #666;
  margin-bottom: 20px;
}

.highlight {
  color: #4caf50;
  font-weight: bold;
}

.download-btn {
  padding: 12px 25px;
  background-color: transparent;
  color: black;
  font-size: 16px;
  border: 2px solid black; /* Черная рамка */
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease; /* Плавное изменение при наведении */
  font-weight: 600;
}

.download-btn:hover {
  background-color: black; /* При наведении кнопка становится черной */
  color: white; /* Текст становится белым */
}

.app-image {
  display: flex;
  justify-content: center;
  margin-top: 30px; /* Добавляем отступ сверху, чтобы изображение было ниже */
}

.app-photo {
  width: 700px; /* Увеличиваем размер изображения */
  height: auto;
  animation: bounce 1.5s ease-in-out infinite; /* Анимация прыжка */
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
</style>
