<template>
  <div class="comment-form">
    <h2>Add Comment</h2>
    <form @submit.prevent="submitComment">
        <textarea v-model="text" placeholder="Enter comment" required></textarea>
        <button type="submit">Submit</button>
    </form>
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
      text: '',
      successMessage: ''
    };
  },
  methods: {
    async submitComment() {
      const currentDateTime = new Date().toISOString();
      const commentData = {
        text: this.text,
        created_at: currentDateTime
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
          this.successMessage = 'Comment sent successfully!';
          this.text = '';
          setTimeout(() => {
            this.successMessage = '';
            this.$router.push('/');
          }, 3000);
        } else {
          console.error('Ошибка при создании комментария');
        }
      } catch (error) {
        console.error('Ошибка сети:', error);
      }
    }
  }
}
</script>

<style scoped>

textarea{
  max-width: 577px;
}
.comment-form {
  margin-top: 14%; /* Увеличено для смещения вниз */
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 10px;
  max-width: 600px;
  width: 100%; /* Позволяет адаптироваться к меньшим экранам */
  margin-left: 35%;
  margin-bottom: 9%;

}

h2 {
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

textarea {
  width: 100%;
  height: 100px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  font-size: 14px;
  resize: none;
}

textarea:focus {
  border-color: #007BFF;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

button {
  background-color: black;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  width: 100%;
}

button:hover {
  background-color: #333;
}

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
