<template>
  <div class="home">
    <splash-screen v-if="isSplashVisible" />
    <img src="@/assets/main.jpg" alt="Main Image">
    <BookTicker />
    <BooksList />
    <BlockComments />
    <div class="map-container">
      <l-map
        style="height: 600px; width: 100%;"
        :zoom="zoom"  
        :center="center"
      >
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <l-marker :lat-lng="marker"></l-marker>
      </l-map>
    </div>
    <CookieConsent />
    <MobileApp />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
import "leaflet/dist/leaflet.css";
import '@/styles/components/common/HomePage.scss'
import BookTicker from '../help/BookTicker.vue'
import CookieConsent from '../help/CookieConsent.vue'
import BooksList from '../help/BooksList.vue'
import SplashScreen from '@/components/help/SplashScreen.vue'
import BlockComments from '../help/BlockComments.vue';
import MobileApp from '../help/MobileApp.vue';


export default defineComponent({
  name: 'HomePage',
  components: {
    BlockComments,
    SplashScreen,
    BookTicker,
    CookieConsent,
    BooksList,
    LMap,
    LTileLayer,
    LMarker,
    MobileApp,
  },
  setup() {
    const center = ref<[number, number]>([51.505, -0.09]); // Координаты центра карты
    const zoom = ref(13); // Зум карты
    const marker = ref<[number, number]>([51.505, -0.09]); // Координаты маркера
    const isSplashVisible = ref(true); // Флаг для отображения SplashScreen

    onMounted(() => {
      // Проверка на наличие записи в sessionStorage
      const isSplashAlreadyShown = sessionStorage.getItem('splashShown');

      if (isSplashAlreadyShown) {
        isSplashVisible.value = false; // Если уже показывали, скрываем SplashScreen
      } else {
        // Если это первый заход на вкладке, сохраняем в sessionStorage
        sessionStorage.setItem('splashShown', 'true');
      }
    });

    return {
      center,
      zoom,
      marker,
      isSplashVisible
    };
  }
});
</script>

<style scoped>
.map-container {
  margin: 2rem 0;
  text-align: center;
  height: 600px; /* Пример фиксированной высоты для контейнера */
}

l-map {
  height: 100%; /* Карта займет всю высоту контейнера */
  width: 100%;
}
</style>
