<template>
    <div>
      <h2>Прослушивание книги: {{ book.title || 'Название отсутствует' }}</h2>
  
      <p v-if="book.audio_file_path">
        <strong>Аудиофайл:</strong> {{ book.audio_file_path }}
      </p>
  
      <audio ref="audio" controls v-if="book.audio_file_path" :src="book.audio_file_path" @error="handleAudioError"></audio>
      <p v-else>Аудиофайл не доступен.</p>
  
      <div class="controls">
        <button @click="playAudio">Играть</button>
        <button @click="pauseAudio">Пауза</button>
        <button @click="stopAudio">Стоп</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      id: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        book: {}, // Данные о книге
      };
    },
    async created() {
      try {
        await this.fetchBook();
      } catch (error) {
        console.error("Ошибка при загрузке книги:", error);
      }
    },
    methods: {
      async fetchBook() {
        try {
          const response = await fetch(`http://127.0.0.1:8001/api/books/books/${this.id}`);
          if (!response.ok) {
            throw new Error(`HTTP статус: ${response.status}`);
          }
  
          const data = await response.json();
  
          // Проверяем и преобразуем путь аудиофайла
          if (data.audio_file_path) {
            if (data.audio_file_path.includes("drive.google.com")) {
              const fileId = this.extractFileId(data.audio_file_path);
              if (fileId) {
                data.audio_file_path = `https://drive.google.com/uc?export=download&id=${fileId}`;
              } else {
                console.error("Невозможно извлечь ID файла из ссылки Google Drive.");
              }
            }
          } else {
            console.warn("Путь к аудиофайлу отсутствует в данных книги.");
          }
  
          this.book = data;
          console.log("Данные книги:", this.book); // Для проверки
        } catch (error) {
          console.error("Ошибка при загрузке данных книги:", error);
        }
      },
      extractFileId(url) {
        const match = url.match(/(?:id=|\/d\/)([a-zA-Z0-9_-]+)/);
        return match ? match[1] : null;
      },
      playAudio() {
        const audio = this.$refs.audio;
        if (audio) {
          audio.play();
        } else {
          console.error("Аудиоплеер не найден.");
        }
      },
      pauseAudio() {
        const audio = this.$refs.audio;
        if (audio) {
          audio.pause();
        }
      },
      stopAudio() {
        const audio = this.$refs.audio;
        if (audio) {
          audio.pause();
          audio.currentTime = 0;
        }
      },
      handleAudioError() {
        console.error("Ошибка загрузки аудиофайла. Проверьте доступность файла или его ссылку.");
        alert("Ошибка загрузки аудиофайла. Проверьте доступность файла или его ссылку.");
      },
    },
  };
  </script>
  
  <style scoped>
  .controls {
    margin-top: 10px;
  }
  
  button {
    margin-right: 5px;
  }
  
  .audio-player {
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 5px;
    background-color: #f9f9f9;
    margin-top: 20px;
  }
  </style>
  