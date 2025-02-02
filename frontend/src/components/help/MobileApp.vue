<template>
    <div class="app-info-container">
      <div class="app-info-content">
        <!-- Left Section: App Description -->
        <div class="app-description">
          <h2>О нашем приложении</h2>
          <p>Наше приложение — это удобный и быстрый способ управления вашими задачами. Мы создали его, чтобы вы могли легко планировать, отслеживать и завершать важные дела прямо со своего мобильного устройства.</p>
          <p>Скачайте наше приложение и начните улучшать свой рабочий процесс сегодня!</p>
          <button class="download-button">Скачать приложение</button>
        </div>
  
        <!-- Right Section: Phone Image with App Screenshot -->
        <div class="app-image">
          <img src="https://via.placeholder.com/250x500.png?text=App+Screenshot" alt="App Screenshot on Phone" class="phone-image" />
        </div>
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
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f7f7f7;
    padding: 40px;
  }
  
  .app-info-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1200px;
    width: 100%;
  }
  
  .app-description {
    flex: 1;
    padding-right: 30px;
  }
  
  .app-description h2 {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .app-description p {
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 15px;
  }
  
  .download-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }
  
  .download-button:hover {
    background-color: #0056b3;
  }
  
  .app-image {
    flex: 1;
    display: flex;
    justify-content: center;
  }
  
  .phone-image {
    max-width: 100%;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  </style>
  