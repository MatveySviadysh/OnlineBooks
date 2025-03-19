<template>
    <div class="listening-container">
        <div class="header-info">
            <div>
                <a style="margin-right: 10px; text-decoration: none; color: black;" href="/">Главная</a>
                >
                <font style="margin-left: 10px; color: orange;">Слушать книгу</font>
            </div>
        </div>

        <div class="book-info">
            <h2>Слушать книгу: {{ book.title }}</h2>
            <p><strong>Автор:</strong> {{ book.author }}</p>
            <div class="book-cover" :class="{'no-cover': !book.image}">
                <img v-if="book.image" :src="book.image" alt="Обложка книги" />
                <span v-else>Нет обложки</span>
            </div>

            <div>Аудиофайл: <a :href="book.audio_file_url" target="_blank">{{ book.audio_file_url }}</a></div>
            <audio v-if="book.audio_file_url" :src="book.audio_file_url" controls></audio>

            <button @click="playAudio">Воспроизвести аудиофайл</button>
        </div>

        <div class="navigation-buttons">
            <button @click="goToBookReader">Читать книгу</button>
            <button @click="goToAllBooks">Вернуться к всем книгам</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            book: {
                title: '',
                author: '',
                image: '',
                audio_file_url: '' // Здесь мы инициализируем аудиофайл
            },
            audio: null // Добавляем переменную для хранения аудио объекта
        };
    },
    async created() {
        const bookId = this.$route.params.id; // Получаем ID книги из параметров маршрута
        try {
            const response = await fetch(`http://127.0.0.1:8001/api/books/books/${bookId}`);
            if (!response.ok) {
                throw new Error(`HTTP статус: ${response.status}`);
            }
            this.book = await response.json();

            // Присвоим правильную ссылку на аудиофайл
            if (this.book.audio_file_path) {
                const fileId = this.book.audio_file_path.split('id=')[1]; // Получаем идентификатор из URL
                this.book.audio_file_url = `https://drive.google.com/uc?export=media&id=${fileId}`; // Используем export=media для прямого доступа
            }
        } catch (error) {
            console.error('Ошибка при загрузке книги:', error);
        }
    },
    methods: {
        playAudio() {
    if (this.audio) {
        this.audio.pause(); // Останавливаем, если уже воспроизводится
    }
    this.audio = new Audio(this.book.audio_file_url);

    this.audio.play().catch(error => {
        console.error('Ошибка воспроизведения аудиофайла:', error);
        alert('Не удалось воспроизвести аудиофайл. Проверьте URL или формат файла.'); // Сообщение об ошибке
    });
}
,
        goToBookReader() {
            this.$router.push({ name: 'BookReader', params: { id: this.book._id } });
        },
        goToAllBooks() {
            this.$router.push({ name: 'AllReadBooks' });
        }
    }
};
</script>

  
  
  
  <style scoped>
  .listening-container {
    padding: 20px;
  }
  
  .header-info {
    font-size: 18px;
    margin-bottom: 20px;
  }
  
  .book-info {
    border: 1px solid #e2e2e2;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
  }
  
  .book-cover {
    margin: 10px auto;
    text-align: center;
  }
  
  .navigation-buttons {
    margin-top: 20px;
    display: flex;
    justify-content: space-around;
  }
  </style>
  