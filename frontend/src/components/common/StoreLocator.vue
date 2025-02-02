<template>
    <div class="store-locator-container">
      <!-- Back Button with Text -->
      
  
      <SplashScreen v-if="isSplashVisible" />
      <div v-else class="map-wrapper">
        <div class="store-description">
            <div class="back-button-container">
        <button @click="goBack" class="back-button">
          <span class="back-text">Назад</span>
        </button>
      </div>
          <h1>Наши магазины</h1>
          <p>Найдите ближайший к вам магазин на карте.</p>
          <div class="store-details">
            <div class="column">
              <h3>Информация о магазине</h3>
              <p>Описание и адрес магазина</p>
            </div>
            <div class="column">
              <h3>Часы работы</h3>
              <p>Понед. - Пятн. 9:00 - 18:00</p>
              <p>Суб. - Вск. Выходной</p>
            </div>
          </div>
        </div>
  
        <div class="map-container">
          <LMap :center="center" :zoom="zoom" style="height: 100%; width: 100%;">
            <LTileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              :attribution="'&copy; <a href=\'https://www.openstreetmap.org/copyright\'>OpenStreetMap</a> contributors'"
            />
            <LMarker :lat-lng="marker" />
          </LMap>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';
  import SplashScreen from '@/components/help/SplashScreen.vue';
  import { LMap, LTileLayer, LMarker } from 'vue3-leaflet';
  import 'leaflet/dist/leaflet.css';
  
  export default defineComponent({
    name: 'StoreLocator',
    components: {
      SplashScreen,
      LMap,
      LTileLayer,
      LMarker
    },
    setup() {
      const center = ref<[number, number]>([51.505, -0.09]);
      const zoom = ref(13);
      const marker = ref<[number, number]>([51.505, -0.09]);
      const isSplashVisible = ref(true);
  
      onMounted(() => {
        const isSplashAlreadyShown = sessionStorage.getItem('splashShown');
        if (isSplashAlreadyShown) {
          isSplashVisible.value = false;
        } else {
          setTimeout(() => {
            isSplashVisible.value = false;
            sessionStorage.setItem('splashShown', 'true');
          }, 3000);
        }
      });
  
      const goBack = () => {
        window.history.back(); // This will navigate to the previous page in the browser's history.
      };
  
      return {
        center,
        zoom,
        marker,
        isSplashVisible,
        goBack
      };
    }
  });
  </script>
  
  <style scoped>
  .store-locator-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    background-color: #f8f4ef;
    min-height: 100vh;
  }
  
  .map-wrapper {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1500px;
    margin-top: 20px;
  }
  
  .store-description {
    flex: 1;
    padding-right: 20px;
    max-width: 500px;
  }
  
  .store-details {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  .column {
    flex: 1;
    margin-right: 20px;
  }
  
  .map-container {
    flex: 2;
    height: 500px;
    width: 100%;
  }
  
  h1, h3 {
    font-size: 24px;
    font-weight: bold;
  }
  
  p {
    font-size: 16px;
  }
  
  /* Back Button Styling */
  .back-button-container {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    padding: 10px 0;
  }
  
  .back-button {
    background: none;
    border: 1px solid #007bff;
    border-radius: 5px;
    color: #007bff;
    font-size: 16px;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .back-button:hover {
    background-color: #007bff;
    color: white;
  }
  
  .back-text {
    margin-left: 8px;
  }
  </style>
  