<template>
  <div class="home">
    <img src="@/assets/main.jpg" alt="">
    <BookTicker />
    <BooksList />
    <div class="map-container">
      <h2>Локация</h2>
      <l-map
        style="height: 400px; width: 100%;"
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
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
import "leaflet/dist/leaflet.css";
import '@/styles/components/common/HomePage.scss'
import BookTicker from '../help/BookTicker.vue'
import CookieConsent from '../help/CookieConsent.vue'
import BooksList from '../help/BooksList.vue'

export default defineComponent({
  name: 'HomePage',
  components: {
    BookTicker,
    CookieConsent,
    BooksList,
    LMap,
    LTileLayer,
    LMarker,
  },
  setup() {
    const center = ref<[number, number]>([51.505, -0.09]); // Координаты центра карты
    const zoom = ref(13); // Зум карты
    const marker = ref<[number, number]>([51.505, -0.09]); // Координаты маркера

    return {
      center,
      zoom,
      marker
    };
  }
});
</script>

<style scoped>
.map-container {
  margin: 2rem 0;
  text-align: center;
}
</style>

