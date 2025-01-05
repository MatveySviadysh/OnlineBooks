<template>
  <footer class="main-footer">
    <div class="footer-content">
      <!-- Навигация -->
      <div class="footer-section">
        <h3>Навигация</h3>
        <nav>
          <ul>
            <li><router-link to="/services">Услуги</router-link></li>
            <li><router-link to="/offers">Предложения</router-link></li>
            <li><router-link to="/artists">Художники</router-link></li>
            <li><router-link to="/list">Каталог</router-link></li>
          </ul>
        </nav>
      </div>

      <!-- Служба поддержки -->
      <div class="footer-section customer-service">
        <h3>Служба поддержки</h3>
        <div class="working-hours">
          <p>Пн-Пт: 9:00 - 17:00</p>
          <p>Сб: 10:00 - 16:00</p>
          <p>24 декабря: 10:00 - 14:00</p>
        </div>
        <div class="contact-info">
          <a href="tel:+74004414546" class="phone">+7 (400) 441-45-46</a>
          <a href="mailto:support@example.com" class="email">
            <i class="far fa-envelope"></i> Написать нам
          </a>
        </div>
      </div>

      <!-- Рассылка -->
      <div class="footer-section newsletter">
        <h3>Новости и акции</h3>
        <p>Подпишитесь на нашу рассылку, чтобы быть в курсе новых коллекций и специальных предложений</p>
        <form @submit.prevent="handleSubscribe" class="subscribe-form">
          <input 
            v-model="email" 
            type="email" 
            placeholder="Ваш email" 
            required
          />
          <button type="submit">Подписаться</button>
        </form>
      </div>

      <!-- Социальные сети -->
      <div class="footer-section social-media">
        <h3>Мы в соцсетях</h3>
        <div class="social-links">
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Pinterest">
            <i class="fab fa-pinterest"></i>
          </a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <a href="#" class="location-link">
        <i class="fas fa-map-marker-alt"></i> Россия
      </a>
      <p class="copyright">&copy; {{ currentYear }} Art Gallery. Все права защищены.</p>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'AppFooter',
  setup() {
    const email = ref('')

    const handleSubscribe = () => {
      console.log('Подписка на email:', email.value)
      email.value = ''
    }

    return {
      email,
      handleSubscribe,
      currentYear: new Date().getFullYear()
    }
  }
})
</script>

<style lang="scss" scoped>
.main-footer {
  background-color: #1a1a1a;
  color: #ffffff;
  padding: 60px 20px 30px;
  margin-top: auto;

  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
  }

  .footer-section {
    padding: 0 15px;

    h3 {
      font-size: 18px;
      margin-bottom: 20px;
      color: #ffffff;
      font-weight: 600;
    }

    ul {
      list-style: none;
      padding: 0;
      
      li {
        margin-bottom: 12px;
        
        a {
          color: #cccccc;
          text-decoration: none;
          transition: color 0.3s ease;
          
          &:hover {
            color: #ffffff;
          }
        }
      }
    }
  }

  .customer-service {
    .working-hours {
      margin-bottom: 20px;
      
      p {
        color: #cccccc;
        margin: 8px 0;
      }
    }

    .contact-info {
      display: flex;
      flex-direction: column;
      gap: 10px;

      .phone, .email {
        color: #ffffff;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: color 0.3s ease;

        &:hover {
          color: #cccccc;
        }

        i {
          font-size: 16px;
        }
      }
    }
  }

  .newsletter {
    .subscribe-form {
      display: flex;
      gap: 10px;
      margin-top: 20px;

      input {
        flex: 1;
        padding: 12px;
        border: 1px solid #333;
        border-radius: 4px;
        background-color: #333;
        color: #ffffff;
        
        &::placeholder {
          color: #999;
        }

        &:focus {
          outline: none;
          border-color: #ffffff;
        }
      }

      button {
        background-color: #ffffff;
        color: #1a1a1a;
        border: none;
        padding: 12px 24px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;

        &:hover {
          background-color: #cccccc;
        }
      }
    }
  }

  .social-media {
    .social-links {
      display: flex;
      gap: 20px;
      justify-content: flex-start;

      a {
        color: #ffffff;
        font-size: 22px;
        transition: transform 0.3s ease;

        &:hover {
          transform: translateY(-3px);
        }
      }
    }
  }

  .footer-bottom {
    text-align: center;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #333;

    .location-link {
      color: #cccccc;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
      transition: color 0.3s ease;

      &:hover {
        color: #ffffff;
      }
    }

    .copyright {
      color: #999;
      font-size: 14px;
    }
  }
}

@media (max-width: 768px) {
  .main-footer {
    padding: 40px 15px 20px;

    .footer-content {
      grid-template-columns: 1fr;
      gap: 30px;
    }

    .footer-section {
      text-align: center;

      .social-links {
        justify-content: center;
      }
    }

    .newsletter .subscribe-form {
      flex-direction: column;
    }
  }
}
</style> 