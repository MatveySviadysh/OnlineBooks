<template>
    <div class="info-header">
        <div class="info-item">
            <i class="fas fa-book"></i>
            <p>{{ bookCount }} books</p>
        </div>
        <div class="info-item">
            <i class="fas fa-headphones"></i>
            <p>2000+ audiobooks</p>
        </div>
        <div class="info-item">
            <i class="fas fa-star"></i>
            <p>200+ new items every month</p>
        </div>
        <div class="info-item">
            <i class="fas fa-wifi"></i>
            <p>Online access</p>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

interface AppInfoData {
    bookCount: number;
}

export default defineComponent({
    name: 'AppInfo',
    data(): AppInfoData {
        return {
            bookCount: 0
        };
    },
    async created() {
        try {
            const response = await axios.get('http://localhost:8001/api/books/books/count');
            this.bookCount = response.data;
        } catch (error) {
            console.error('Error fetching book count:', error);
        }
    }
});
</script>

<style scoped>
.info-header {
    width: 1050px;
    height: 150px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px auto;
    padding: 0 20px;
}

.info-item {
    text-align: center;
}

.info-item i {
    font-size: 24px;
    color: #000000;
    margin-bottom: 10px;
}

.info-item p {
    font-size: 16px;
    margin: 0;
    color: #333;
}
</style>