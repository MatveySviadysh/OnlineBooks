<template>
  <div class="home">
    <splash-screen v-if="isSplashVisible" />
    <HederHome />
    <BookTicker />
    <BooksList />
    <BlockComments />
    <AuthorsBlock />
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
        <!-- Добавление кнопок управления -->
        <div class="map-controls">
          <button @click="zoomIn" class="zoom-btn">+</button>
          <button @click="zoomOut" class="zoom-btn">-</button>
          <button @click="resetMap" class="reset-btn">Reset</button>
        </div>
      </l-map>
    </div>
    <CookieConsent />
    <RecomendBooks v-if="isAuthenticated" />
    <MobileApp />
    <InfoService />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import axios from "axios";
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
import "leaflet/dist/leaflet.css";
import "@/styles/components/common/HomePage.scss";
import BookTicker from "../help/BookTicker.vue";
import CookieConsent from "../help/CookieConsent.vue";
import BooksList from "../help/BooksList.vue";
import SplashScreen from "@/components/help/SplashScreen.vue";
import BlockComments from "../help/BlockComments.vue";
import MobileApp from "../help/MobileApp.vue";
import InfoService from "../help/InfoService.vue";
import HederHome from "../help/HederHome.vue";
import RecomendBooks from "../help/RecomendBooks.vue";
import AuthorsBlock from "../help/AuthorsBlock.vue";

export default defineComponent({
  name: "HomePage",
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
    InfoService,
    HederHome,
    RecomendBooks,
    AuthorsBlock,
  },
  setup() {
    const center = ref<[number, number]>([51.505, -0.09]);
    const zoom = ref(13);
    const marker = ref<[number, number]>([51.505, -0.09]);
    const isSplashVisible = ref(true);
    const isAuthenticated = ref(false);

    // Проверка аутентификации пользователя
    const checkAuth = async () => {
      try {
        const response = await axios.get('http://localhost:8001/api/users/me', {
          withCredentials: true
        })
        if (response.data.email) {
          isAuthenticated.value = true;
        }
      } catch (error) {
        isAuthenticated.value = false;
      }
    };

    onMounted(() => {
      checkAuth(); // Вызываем проверку аутентификации при загрузке компонента

      const isSplashAlreadyShown = sessionStorage.getItem("splashShown");
      if (isSplashAlreadyShown) {
        isSplashVisible.value = false;
      } else {
        sessionStorage.setItem("splashShown", "true");
      }
    });

    // Функции управления картой
    const zoomIn = () => {
      zoom.value = zoom.value < 18 ? zoom.value + 1 : 18;
    };
    const zoomOut = () => {
      zoom.value = zoom.value > 1 ? zoom.value - 1 : 1;
    };
    const resetMap = () => {
      center.value = [51.505, -0.09]; // Устанавливаем начальные координаты
      zoom.value = 13; // Сброс масштаба
    };

    return {
      center,
      zoom,
      marker,
      isSplashVisible,
      isAuthenticated,
      zoomIn,
      zoomOut,
      resetMap
    };
  },
});
</script>

<style scoped>
.map-container {
  margin-top: 50px;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2rem auto;
  height: 600px;
  width: 100%;
  max-width: 1400px; /* Ограничение ширины контейнера */
  background-color: #f0f0f0; /* Легкий фон для контекста */
  border-radius: 15px; /* Скругление углов */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Тень для глубины */
  overflow: hidden; /* Скрытие элементов, выходящих за пределы */
}

.map-controls {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 10;
}

.zoom-btn, .reset-btn {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 20px;
  transition: background-color 0.3s;
}

.zoom-btn:hover, .reset-btn:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
</style>
