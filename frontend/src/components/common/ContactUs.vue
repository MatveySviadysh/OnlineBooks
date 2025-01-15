<template>
  <div class="email-form">
    <h2>Напишите нам</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="message_body">Сообщение</label>
        <textarea 
          v-model="messageBody" 
          id="message_body" 
          placeholder="Введите ваше сообщение" 
          required
        ></textarea>
      </div>
      <button type="submit">Отправить</button>
    </form>

    <p v-if="message" :class="{'success-message': isSuccess, 'error-message': !isSuccess}">
      {{ message }}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import '@/styles/components/common/ContactUs.scss'

export default defineComponent({
  name: 'EmailForm',
  setup() {
    const messageBody = ref('')
    const message = ref('')
    const isSuccess = ref(true)

    const handleSubmit = async () => {
      try {
        const response = await fetch('http://localhost:8888/send_user_email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message_body: messageBody.value,
          }),
        });

        const result = await response.json();

        if (result.success) {
          message.value = 'Сообщение успешно отправлено!';
          isSuccess.value = true;
          messageBody.value = ''; // Очистка поля сообщения только при успехе
        } else {
          message.value = result.message || 'Что-то пошло не так. Попробуйте еще раз.';
          isSuccess.value = false;
        }
      } catch (error) {
        message.value = 'Ошибка при отправке сообщения. Пожалуйста, попробуйте позже.';
        isSuccess.value = false;
      }
    };

    return {
      messageBody,
      handleSubmit,
      message,
      isSuccess
    }
  }
})
</script>

<style scoped>
.success-message {
  color: green;
  margin-top: 10px;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.email-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
