<template>
  <div class="contact-us-container">
    <!-- Back button -->
    <div class="back-button-container">
      <p class="back-button" @click="goBack">
        ← Назад
      </p>
    </div>

    <div class="contact-us-form">
      <div class="alert error" v-if="error">
        {{ error }}
      </div>

      <h2>Contact Us</h2>

      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <textarea 
            v-model="messageBody" 
            id="message_body" 
            placeholder="Enter your message" 
            required
          ></textarea>
        </div>

        <button class="contact-us-button" type="submit" :disabled="loading">
          {{ loading ? 'Sending...' : 'Send' }}
        </button>
      </form>

      <div v-if="message" :class="{'success-message': isSuccess, 'error-message': !isSuccess}">
        {{ message }}
      </div>
    </div>

    <!-- Success message after sending -->
    <div v-if="successMessage" class="success-popup">
      <p>{{ successMessage }}</p>
    </div>
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
    const loading = ref(false)
    const error = ref('')
    const successMessage = ref('')

    const handleSubmit = async () => {
      loading.value = true
      error.value = ''
      successMessage.value = ''

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
          successMessage.value = 'Message successfully sent!'
          isSuccess.value = true
          messageBody.value = '' // Clear message field only on success
        } else {
          error.value = result.message || 'Something went wrong. Please try again.'
          isSuccess.value = false
        }
      } catch (err) {
        error.value = 'Error sending message. Please try again later.'
        isSuccess.value = false
      } finally {
        loading.value = false
      }
    };

    const goBack = () => {
      window.history.back();  // This will take the user to the previous page
    };

    return {
      messageBody,
      handleSubmit,
      message,
      isSuccess,
      loading,
      error,
      successMessage,
      goBack
    }
  }
})
</script>

<style scoped>
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

.contact-us-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f4ef;
  padding: 20px;
  flex-direction: column;
}

.back-button-container {
  align-items: left;
  text-align: left;
}





.contact-us-form {
  position: relative;
  width: 835px;
  height: auto;
  background-color: #fff;
  padding: 30px;
  border-radius: 0;
  box-shadow: none;
}

h2 {
  font-size: 1.5rem;
  color: #333;
  text-transform: uppercase;
  margin-bottom: 10px;
  text-align: center;
}

.form-group {
  text-align: left;
  margin-bottom: 15px;
}

.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 0px;
  font-size: 0.9rem;
  resize: vertical;
}

.contact-us-button {
  width: 100%;
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.contact-us-button:hover {
  background-color: #555;
}

.contact-us-button:disabled {
  background-color: #999;
  cursor: not-allowed;
}

.alert.error {
  background-color: #fee;
  color: #e63946;
  border-radius: 4px;
  margin-bottom: 20px;
  font-size: 0.8rem;
  text-align: center;
}

.success-message {
  color: green;
  text-align: center;
  margin-top: 10px;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.success-popup {
  background-color: #fffdf8;
  color: #333;
  padding: 20px;
  border-radius: 8px;
  position: fixed;
  top: 70px;
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
</style>
