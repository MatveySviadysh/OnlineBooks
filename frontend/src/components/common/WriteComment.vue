<template>
    <div class="comment-form">
      <h2>Добавить комментарий</h2>
      <form @submit.prevent="submitComment">
        <textarea v-model="text" placeholder="Введите комментарий" required></textarea>
        <button type="submit">Отправить</button>
      </form>
  
      <!-- Сообщение об успешной отправке -->
      <div v-if="successMessage" class="success-popup">
        <p>{{ successMessage }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AddComment',
    data() {
      return {
        text: '',  // Текст комментария
        successMessage: ''  // Сообщение об успешной отправке
      };
    },
    methods: {
      async submitComment() {
        const currentDateTime = new Date().toISOString();  // Получаем текущее время в ISO формате
  
        const commentData = {
          text: this.text,
          created_at: currentDateTime  // Отправляем дату и время создания комментария
        };
  
        try {
          const response = await fetch('http://127.0.0.1:8001/api/comments/comments/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(commentData)
          });
  
          if (response.ok) {
            const data = await response.json();
            console.log('Комментарий успешно создан:', data);
  
            // Показываем сообщение об успешной отправке
            this.successMessage = 'Комментарий успешно отправлен!';
  
            // Очищаем поле ввода
            this.text = '';
  
            // Через 3 секунды скрываем сообщение
            setTimeout(() => {
              this.successMessage = '';
            }, 3000);
          } else {
            console.error('Ошибка при создании комментария');
          }
        } catch (error) {
          console.error('Ошибка сети:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Стили для всплывающего сообщения */
  .success-popup {
    background-color: white;
    color: #333;
    padding: 20px;
    border-radius: 8px;
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    width: 300px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    opacity: 0;
    animation: fadeIn 1s forwards, fadeOut 1s 2s forwards;
    text-align: center;
    font-size: 16px;
  }
  
  /* Анимация появления */
  @keyframes fadeIn {
    0% {
      opacity: 0;
      transform: translateX(-50%) translateY(20px);
    }
    100% {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
  }
  
  /* Анимация исчезновения */
  @keyframes fadeOut {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
      transform: translateX(-50%) translateY(20px);
    }
  }
  </style>
  