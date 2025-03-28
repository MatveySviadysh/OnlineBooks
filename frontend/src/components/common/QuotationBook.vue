<template>
  <div class="quotes-container">
    <div class="circle left-circle"></div>
    <div class="circle right-circle"></div>
    <h1 class="title">Quote Book</h1>
    <input type="text" v-model="searchQuery" placeholder="Search quotes..." class="my-search"/>
    <div v-for="quote in filteredQuotes" :key="quote.id" class="quote">
      <p class="quote-text">"{{ quote.text }}"</p>
      <small class="quote-author">- {{ quote.author || 'Unknown Author' }}</small>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      quotes: []
    };
  },
  computed: {
    filteredQuotes() {
      return this.quotes.filter(quote => 
        quote.text.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  async created() {
    try {
      const response = await fetch('http://localhost:8000/v1/quotes/all');
      const quotesData = await response.json();

      this.quotes = quotesData.map(quote => ({
        ...quote,
        author: quote.author || 'Unknown Author'
      }));
    } catch (error) {
      console.error('Error fetching quotes:', error);
    }
  }
};
</script>

<style scoped>
.quotes-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  border-radius: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}

.circle {
  position: absolute;
  width: 300px; /* Увеличенная ширина круга */
  height: 300px; /* Увеличенная высота круга */
  border-radius: 50%;
  background-color: black;
  opacity: 0.5; /* Полупрозрачность */
  animation: roll-in 1s ease forwards; /* Анимация появления */
}

.left-circle {
  left: -150px; /* Начальная позиция слева */
  top: calc(50% + 30px); /* Немного ниже центра */
  animation-name: roll-in-left; /* Название анимации для левого круга */
}

.right-circle {
  right: -150px; /* Начальная позиция справа */
  top: calc(50% - 70px); /* Немного выше центра */
  animation-name: roll-in-right; /* Название анимации для правого круга */
}

/* Анимация для левого круга */
@keyframes roll-in-left {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

/* Анимация для правого круга */
@keyframes roll-in-right {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}

.title {
  text-align: center;
  font-size: 3rem;
  color: #343a40;
  margin-bottom: 20px;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.my-search {
  padding: 12px 40px;
  margin-bottom: 30px;
  width: 60%;
  max-width: 500px;
  border: none;
  border-radius: 20px;
  font-size: 1rem;
  outline: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.quote {
  width: 60%;
  max-width: 600px;
  border-radius: 10px;
  padding: 20px;
  margin: 15px 0;
  background-color: #ffffff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s, background-color 0.3s, box-shadow 0.3s;
  opacity: 0;
  animation: appear 0.5s forwards;
}

.quote:hover {
  background-color: #ffecb3;
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

@keyframes appear {
  to {
    opacity: 1;
  }
}

.quote-text {
  font-style: italic;
  font-size: 1.5rem;
  color: #343a40;
}

.quote-author {
  text-align: right;
  font-size: 1.2rem;
  color: #666;
  font-weight: bold;
  margin-top: 10px;
}
</style>
