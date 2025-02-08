<template>
    <div class="a-row">
        <a class="btn">Books</a>
        <a class="btn">Audiobooks</a>
        <a class="btn" href="https://t.me/Obook2007_bot?start=some_parameter">Our Bot</a>
        <a class="btn">Authors</a>
        <a class="btn">Quotes</a>
        <a class="btn">Top Books</a>
        <a class="btn">New Books</a>
    </div>
</template>

<script lang="ts">
export default {
    name: 'AnimatedButtons',
};
</script>

<style scoped>
.a-row {
    width: 1150px;
    height: 50px;
    margin-top: 100px;
    display: flex;
    gap: 40px;
    margin-left: 23%;
}

.btn {
    text-align: center;
    padding: 8px 16px;
    border-radius: 15px;
    border: 1px solid #909090;
    cursor: pointer;
    width: 90px;
    color: black;
    background-color: white;
    position: relative;
    overflow: hidden;
    transition: all 0.5s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    background: radial-gradient(circle, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.5));
    transform: translate(-50%, -50%) scale(0);
    transition: transform 0.5s ease, opacity 0.5s ease;
    border-radius: 50%;
    z-index: 0;
    opacity: 0;
}

.btn:hover::before {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
}

.btn:hover {
    color: white;
    background-color: black;
    border-color: black;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    transform: scale(1.1);
}

.btn:active {
    transform: scale(0.9);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.btn span {
    position: relative;
    z-index: 1;
}

/* Добавляем градиентный фон при наведении */
.btn:hover {
    background: linear-gradient(45deg, #000000, #333333);
}

/* Добавляем анимацию текста при наведении */
.btn:hover span {
    animation: textGlow 1s ease-in-out infinite alternate;
}

@keyframes textGlow {
    from {
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.7), 0 0 10px rgba(255, 255, 255, 0.7);
    }
    to {
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.9), 0 0 20px rgba(255, 255, 255, 0.9);
    }
}
</style>