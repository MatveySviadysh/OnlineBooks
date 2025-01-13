<template>
  <div>
    
    <div class="comments-grid">
      <div
        v-for="(column, colIndex) in columns"
        :key="colIndex"
        class="comments-column"
        :class="[getColumnClass(colIndex), { 'rotate-reverse': isColumnWide(colIndex) }]"
        ref="column-${colIndex}"
      >
        <div v-for="(comment) in column" :key="comment.user_id" class="comment-card">
          <p>{{ comment.text }}</p>
          <p class="comment-date">{{ formatDate(comment.created_at) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      comments: [],
      columns: [[], [], [], [], []], // Array to represent 5 columns
    };
  },
  mounted() {
    this.fetchComments();
    this.addInfiniteComments();
  },
  methods: {
    async fetchComments() {
      try {
        const response = await fetch('http://127.0.0.1:8001/api/comments/comments/?skip=0&limit=100', {
          method: 'GET',
          headers: {
            'accept': 'application/json',
          },
        });
        const data = await response.json();
        this.comments = data;
        this.distributeCommentsIntoColumns();
      } catch (error) {
        console.error('Ошибка при получении комментариев:', error);
      }
    },
    addInfiniteComments() {
      setInterval(() => {
        const newComment = {
          user_id: Date.now(),
          text: 'Новый комментарий для бесконечной анимации.',
          created_at: new Date().toISOString(),
        };
        this.comments.push(newComment);
        this.distributeCommentsIntoColumns();
      }, 10000); // Add new comment every 10 seconds
    },
    distributeCommentsIntoColumns() {
      this.columns = [[], [], [], [], []]; // Reset columns
      this.comments.forEach((comment, index) => {
        const columnIndex = index % 5; // Distribute comments into 5 columns
        this.columns[columnIndex].push(comment);
      });
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      const day = String(date.getDate()).padStart(2, '0');
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const year = date.getFullYear();
      return `${day}.${month}.${year}`;
    },
    getColumnClass(index) {
      // Apply different animations for each column
      return `rotate-${index + 1}`;
    },
    isColumnWide(index) {
      const column = this.$refs[`column-${index}`];
      return column && column.clientHeight > 400; // Check if the column exceeds 400px height
    }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

h2 {
  text-align: center;
  color: #333;
}

.comments-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 5 columns */
  gap: 30px; /* Increased gap between columns */
  margin-top: 20px;
  position: relative;
  max-height: 90vh; /* Use dynamic height based on viewport */
  max-width: 100%; /* Limit grid width to 500px */
  overflow: hidden; /* Remove scrollbar */
  z-index: 1; /* Ensure the grid stays behind the comment columns */
  margin-left: auto;
  margin-right: auto; /* Center the grid horizontally */
}

.comments-column {
  display: flex;
  flex-direction: column;
  height: auto; /* Allow column height to adjust with content */
  overflow: hidden;
  position: relative;
  z-index: 2; /* Ensure comment columns are on top of the grid */
  animation: infinite-scroll 20s linear infinite;
}

.comment-card {
  border: 1px solid #000000;
  padding: 15px;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  background-color: #f8f4ef;
  z-index: 3;
  margin-bottom: 20px;
  height: 130px;
  position: relative; /* Для внутренних анимаций */
  overflow: hidden; /* Чтобы элементы не выходили за пределы */
  transition: box-shadow 0.3s ease; /* Плавный переход тени */
}

.comment-card:hover {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); /* Более глубокая тень */
  animation: flashColor 1s ease-in-out infinite; /* Анимация вспышки */
}

@keyframes flashColor {
  0% {
    background-color: #f8f4ef; /* Исходный цвет */
  }
  50% {
    background-color: #f3ece3; /* Яркий цвет (вспышка) */
  }
  100% {
    background-color: #f8f4ef; /* Возвращаемся к исходному цвету */
  }
}

.comment-card:hover .card-content {
  animation: pulseText 1.5s ease-in-out infinite; /* Анимация пульсации текста */
}

.card-content {
  transition: transform 0.3s ease-in-out;
}

@keyframes pulseText {
  0% {
    transform: scale(1); /* Исходное состояние */
    color: #6b4f3e; /* Исходный цвет текста */
  }
  50% {
    transform: scale(1.05); /* Легкое увеличение текста */
    color: #ff8a00; /* Цвет текста становится более теплым */
  }
  100% {
    transform: scale(1); /* Возврат к исходному состоянию */
    color: #6b4f3e; /* Возврат к исходному цвету текста */
  }
}

.comment-date{
  text-align: right;
  margin-top: 90px;
}
@keyframes infinite-scroll {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20%); /* Уменьшено до 50% от высоты колонки */
  }
  100% {
    transform: translateY(0);
  }
}

.rotate-1 {
  animation: infinite-scroll 25s linear infinite; /* Different speeds for variety */
}

.rotate-2 {
  animation: infinite-scroll 40s linear infinite;
}

.rotate-3 {
  animation: infinite-scroll 28s linear infinite;
}

.rotate-4 {
  animation: infinite-scroll 40s linear infinite;
}

.rotate-5 {
  animation: infinite-scroll 35s linear infinite;
}

p {
  font-size: 14px;
  margin: 5px 0;
  font-family: 'Playfair Display', serif; /* Font styling */
}
</style>
