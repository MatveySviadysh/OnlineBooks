<template>
    <div class="store-locator-container">
      <SplashScreen v-if="isSplashVisible" />
      <div v-else class="map-wrapper">
        <div class="store-description">
            <div class="back-button-container">
              <button @click="goBack" class="back-button">
                <span class="back-text">Back</span>
              </button>
            </div>
          <h1 class="title">Our Stores</h1>
          <p class="subtitle">Find the nearest store to you on the map.</p>
          <div class="store-details">
            <div class="column">
              <h3>Store Information</h3>
              <p>Store description and address</p>
            </div>
            <div class="column">
              <h3>Working Hours</h3>
              <p>Mon. - Fri. 9:00 - 18:00</p>
              <p>Sat. - Sun. Closed</p>
            </div>
          </div>
        </div>
  
        <div class="map-container">
          <LMap :center="center" :zoom="zoom" style="height: 100%; width: 100%;">
            <LTileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              :attribution="'© <a href=\'https://www.openstreetmap.org/copyright\'>OpenStreetMap</a> contributors'"
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
        window.history.back();
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
    padding: 40px;
    background: linear-gradient(135deg, #f8f4ef 0%, #e8e4df 100%);
    min-height: 100vh;
  }
  
  .map-wrapper {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1500px;
    margin-top: 20px;
    gap: 40px;
  }
  
  .store-description {
    flex: 1;
    padding: 30px;
    max-width: 500px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }
  
  .store-details {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
    gap: 20px;
  }
  
  .column {
    flex: 1;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 15px;
    transition: transform 0.3s ease;
  }
  
  .column:hover {
    transform: translateY(-5px);
  }
  
  .map-container {
    flex: 2;
    height: 600px;
    width: 100%;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }
  
  .title {
    font-size: 36px;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 10px;
    font-family: 'Playfair Display', serif;
  }
  
  .subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
  }
  
  h3 {
    font-size: 24px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 15px;
  }
  
  p {
    font-size: 16px;
    line-height: 1.6;
    color: #666;
  }
  
  .back-button-container {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    padding: 10px 0;
    margin-bottom: 20px;
  }
  
  .back-button {
    background: none;
    border: 2px solid #2c3e50;
    border-radius: 10px;
    color: #2c3e50;
    font-size: 16px;
    font-weight: 600;
    padding: 12px 24px;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .back-button:hover {
    background-color: #2c3e50;
    color: white;
    transform: translateX(-5px);
  }
  
  .back-text {
    margin-left: 8px;
  }

  @media (max-width: 1024px) {
    .map-wrapper {
      flex-direction: column;
    }
    
    .store-description {
      max-width: 100%;
    }
    
    .map-container {
      height: 400px;
    }
  }
  </style>
