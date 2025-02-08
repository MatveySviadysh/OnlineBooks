<template>
    <HomeHeaderButtons />
    <div class="header-home">
      <div class="header-content">
        <div class="header-home-text">
          Online Book — read and listen with one subscription
        </div>
        <div class="button-container">
          <a href="/book/read">Read</a>
        </div>
      </div>
      <div class="header-image">
        <img class="header-photo" src="@/assets/home_header.jpg" alt="Main Image">
      </div>
    </div>
    <InformationHeader />
  </template>
  
  <script lang="ts">
  import InformationHeader from './InformationHeader.vue';
  import HomeHeaderButtons from './HomeHeaderButtons.vue';
  
  export default {
    name: 'AppInfo',
    components: {
      InformationHeader,
      HomeHeaderButtons,
    },
  };
  </script>
  
  <style scoped>
  .header-home {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 1200px;
    height: 466px;
    margin: 7% auto 0;
    margin-top: 30px;
  }
  
  .header-content {
    display: flex;
    flex-direction: column;
    text-align: left;
    flex: 1;
    padding-right: 20px;
    height: 337px;
  }
  
  .header-home-text {
    font-weight: 600;
    font-size: 34px;
    width: 400px;
    margin: 0 auto 20px;
  }
  
  .header-image {
    flex: 1;
    display: flex;
    justify-content: flex-end;
  }
  
  .header-photo {
    width: 600px;
    height: 337px;
    object-fit: cover;
    border-radius: 10px;
    margin-left: 20px;
  }
  
  .button-container {
    position: relative;
    width: 190px;
    height: 50px;
    text-align: center;
    margin-top: 30px;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    border-radius: 4rem;
    background: black; /* Черный фон */
    border: 1px solid white; /* Тонкая белая рамка */
  }
  
  .button-container:hover {
    transform: rotate(-4deg) scale(1.1);
    box-shadow: 0 8px 16px rgba(255, 255, 255, 0.2); /* Белая тень */
  }
  
  .button-container::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: white; /* Белый фон при наведении */
    border-radius: 4rem;
    z-index: -1;
    opacity: 0;
    transition: opacity 0.4s ease, transform 0.4s ease;
    transform: scale(0.9);
  }
  
  .button-container:hover::before {
    opacity: 1;
    transform: scale(1);
  }
  
  .button-container::after {
    content: '';
    width: 8px;
    height: 120px;
    background: linear-gradient(
      to right,
      rgba(255, 255, 255, 0) 0%,
      rgba(255, 255, 255, 0.8) 50%,
      rgba(255, 255, 255, 0) 100%
    ); /* Градиентная световая полоса */
    rotate: 30deg;
    position: absolute;
    inset: 0;
    top: 0;
    left: -180%;
    margin: auto;
    transition: left 0.6s cubic-bezier(0.2, 0.5, 0.2, 1.2);
  }
  
  .button-container:hover::after {
    left: 120%;
  }
  
  a {
    color: white; /* Белый текст */
    text-decoration: none;
    font-size: 18px;
    cursor: pointer;
    z-index: 1;
    transition: color 0.4s ease;
  }
  
  .button-container:hover a {
    color: black; /* Черный текст при наведении */
  }
  </style>