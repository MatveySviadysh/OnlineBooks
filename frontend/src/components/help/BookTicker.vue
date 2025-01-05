<template>
  <div class="book-ticker-container">
    <div class="book-ticker" :style="{ animationDuration: `${duration}s` }">
      <div class="ticker-content">
        <span v-for="(book, index) in books" :key="index" class="book-title">
          {{ book }}
        </span>
      </div>
      <div class="ticker-content" aria-hidden="true">
        <span v-for="(book, index) in books" :key="index" class="book-title">
          {{ book }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BookTicker',
  data() {
    return {
      books: [
        'Война и мир',
        'Преступление и наказание',
        'Мастер и Маргарита',
        'Евгений Онегин',
        'Идиот',
        'Анна Каренина',
        'Братья Карамазовы',
        'Герой нашего времени',
        'Тихий Дон',
        'Отцы и дети',
        'Вишневый сад',
        'Мертвые души',
        'Три сестры',
        'Обломов',
        'Бесы',
        'Капитанская дочка',
        'Ревизор',
        'Палата №6',
        'Гроза',
        'Записки охотника'
      ],
      duration: 40
    }
  }
})
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap');

.book-ticker-container {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  overflow: hidden;
  background: #f8f9fa;
  padding: 10px 0;
  user-select: none;
}

.book-ticker {
  display: flex;
  animation: ticker-scroll linear infinite;
  white-space: nowrap;
}

.ticker-content {
  display: flex;
  margin-right: 30px;
}

.book-title {
  margin: 0 10px;
  font-size: 18px;
  color: #2c3e50;
  border: 1px solid #000;
  padding: 5px 12px;
  border-radius: 12px;
  font-weight: 400;
  font-family: 'Playfair Display', serif;
  letter-spacing: 0.5px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

@keyframes ticker-scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style> 