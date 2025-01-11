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
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue'
  import '@/styles/components/common/ContactUs.scss'

  export default defineComponent({
    name: 'EmailForm',
    setup() {
      const userEmail = ref('')
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
        isSuccess
      }
    }
  })
  </script>
  
  <style scoped>
  .email-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  h2 {
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  .success-message {
    color: green;
    text-align: center;
  }
  
  .error-message {
    color: red;
    text-align: center;
  }
  </style>
  