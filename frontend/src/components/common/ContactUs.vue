<template>
  <div class="email-form">
    <h2>Напишите нам</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="user_email">Ваш Email</label>
        <input 
          v-model="userEmail" 
          type="email" 
          id="user_email" 
          placeholder="Введите ваш email" 
          required 
        />
      </div>
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

    <!-- Display email if user is authenticated -->
    <p v-if="userEmailFromAPI">
      Авторизованный Email: {{ userEmailFromAPI }}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import '@/styles/components/common/ContactUs.scss'

export default defineComponent({
  name: 'EmailForm',
  setup() {
    const userEmail = ref('')
    const messageBody = ref('')
    const message = ref('')
    const isSuccess = ref(true)
    const userEmailFromAPI = ref('') // Email из API, если пользователь авторизован

    // Функция для получения email авторизованного пользователя
    const fetchUserEmail = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8001/api/users/me', {
          method: 'GET',
        });

        // Проверяем статус ответа и извлекаем данные из ответа
        if (response.status === 200) {
          const result = await response.json(); // Данные из JSON
          if (result.email) {
            userEmail.value = result.email; // Если email есть, сохраняем его
          } else {
            userEmail.value = ''; // Если email нет, оставляем пустым
          }
        } else {
          userEmail.value = ''; // Если статус не 200, оставляем пустым
        }
      } catch (error) {
        console.error('Error fetching user email:', error);
        userEmail.value = ''; // В случае ошибки также очищаем email
      }
    };


    // Выполнение запроса при монтировании компонента
    onMounted(() => {
      fetchUserEmail();
    });

    // Функция для отправки сообщения
    const handleSubmit = async () => {
      try {
        const response = await fetch('http://localhost:8888/send_user_email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_email: userEmail.value,
            message_body: messageBody.value,
          }),
        });

        const result = await response.json();

        if (result.success) {
          message.value = 'Message successfully sent to the service and response sent to user.';
          isSuccess.value = true;
        } else {
          message.value = result.message || 'Something went wrong. Please try again.';
          isSuccess.value = false;
        }
      } catch (error) {
        message.value = 'Error while sending email. Please try again later.';
        isSuccess.value = false;
      }

      userEmail.value = ''; // Clear email field
      messageBody.value = ''; // Clear message field
    };

    return {
      userEmail,
      messageBody,
      handleSubmit,
      message,
      isSuccess,
      userEmailFromAPI
    }
  }
})
</script>

<style scoped>
.success-message {
  color: green;
}

.error-message {
  color: red;
}
</style>
