<template>
    <div class="info-header">
        <div class="info-item">
            <i class="fas fa-book"></i>
            <p>{{ bookCount }} books</p>
        </div>
        <div class="info-item">
            <i class="fas fa-headphones"></i>
            <p>{{ audiobookCount }} audiobooks</p>
        </div>
        <div class="info-item">
            <i class="fas fa-star"></i>
            <p>{{ newBooksLastMonth }} new items this month</p>
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
    audiobookCount: number;
    newBooksLastMonth: number;
}

export default defineComponent({
    name: 'AppInfo',
    data(): AppInfoData {
        return {
            bookCount: 0,
            audiobookCount: 0,
            newBooksLastMonth: 0, // Add this new property
        };
    },
    async created() {
        try {
            // Fetch the total number of books
            const bookResponse = await axios.get('http://127.0.0.1:8001/api/books/books/count');
            this.bookCount = bookResponse.data;

            // Fetch the number of audiobooks
            const audiobookResponse = await axios.get('http://127.0.0.1:8001/api/book/book/count-with-audio');
            this.audiobookCount = audiobookResponse.data;

            // Fetch the number of books added in the last month
            const lastMonthBooksResponse = await axios.get('http://127.0.0.1:8001/api/book/book/count-last-month');
            this.newBooksLastMonth = lastMonthBooksResponse.data;
        } catch (error) {
            console.error('Error fetching counts:', error);
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
