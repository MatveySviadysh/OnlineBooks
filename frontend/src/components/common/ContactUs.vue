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
          <img src="@/assets/contact_us.png" alt="">
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

<style scoped>.contact-us-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f8f4ef, #eae0d5);
  padding: 20px;
  flex-direction: column;
}

.back-button-container {
  width: 100%;
  max-width: 850px;
  text-align: left;
  margin-bottom: 10px;
}

.back-button {
  cursor: pointer;
  font-size: 16px;
  color: #333;
  transition: color 0.3s ease;
}

.back-button:hover {
  color: #555;
}

.contact-us-form {
  width: 100%;
  max-width: 850px;
  background: #f8f5f0;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 24px;
  color: #333;
  text-transform: uppercase;
  margin-bottom: 15px;
  text-align: center;
}

.form-group {
  text-align: left;
  margin-bottom: 15px;
}

.form-group img {
  display: block;
  max-width: 700px;
  margin: 0 auto 15px;
}

.form-group textarea {
  width: 96.5%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  resize: vertical;
  transition: border-color 0.3s ease;
}

.form-group textarea:focus {
  border-color: #555;
  outline: none;
}

.contact-us-button {
  width: 100%;
  background: linear-gradient(90deg, #333, #555);
  color: #fff;
  border: none;
  padding: 12px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.contact-us-button:hover {
  background: linear-gradient(90deg, #555, #777);
}

.contact-us-button:disabled {
  background: #999;
  cursor: not-allowed;
}

.alert.error {
  background-color: #fee;
  color: #e63946;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 0.9rem;
  text-align: center;
  box-shadow: 0px 2px 5px rgba(255, 0, 0, 0.1);
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
  background: #fffdf8;
  color: #333;
  padding: 20px;
  border-radius: 12px;
  position: fixed;
  top: 70px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: 320px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeIn 1s forwards, fadeOut 1s 2.5s forwards;
  text-align: center;
  font-size: 16px;
}

/* Анимации */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(20px);
  }
}

</style>
