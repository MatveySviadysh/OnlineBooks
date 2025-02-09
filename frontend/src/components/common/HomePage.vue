<template>
  <div class="home">
    <splash-screen v-if="isSplashVisible" />
    <HederHome />
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
    <RecomendBooks />
    <MobileApp />
    <AuthorsBlock />
    <InfoService />
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
import InfoService from '../help/InfoService.vue';
import HederHome from '../help/HederHome.vue';
import RecomendBooks from '../help/RecomendBooks.vue';
import AuthorsBlock from '../help/AuthorsBlock.vue';

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

    onMounted(() => {
      const isSplashAlreadyShown = sessionStorage.getItem('splashShown');

      if (isSplashAlreadyShown) {
        isSplashVisible.value = false;
      } else {
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
  height: 600px;
}

.l-map {
  height: 100%;
  width: 100%;
}
</style>
