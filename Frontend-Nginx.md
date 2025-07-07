# Frontend & Nginx Documentation

## Описание

Этот проект содержит фронтенд-приложение и конфигурацию Nginx для его сервировки.  
Фронтенд построен на [укажи, например React/Vue/Angular] и собирается в статические файлы, которые Nginx раздает пользователям.

---

## Структура проекта

frontend/ # Исходники фронтенда
├── public/
├── src/
├── package.json
└── ... # Другие файлы фронтенда

nginx/
├── default.conf # Конфигурация Nginx для фронтенда
Dockerfile # (если есть) образ для фронтенда + nginx


---

## Установка и запуск фронтенда локально

1. Перейдите в папку фронтенда:

```bash
cd frontend

    Установите зависимости:

npm install

    Запустите локальный дев-сервер:

npm start

    Фронтенд будет доступен по адресу http://localhost:3000 (по умолчанию)

Сборка фронтенда

Для сборки статических файлов используйте:

npm run build

После успешной сборки статические файлы появятся в папке frontend/build (или dist, в зависимости от настройки).
Настройка и запуск Nginx
Конфигурация

Пример базовой конфигурации Nginx (nginx/default.conf):

server {
    listen 80;
    server_name your_domain_or_ip;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Можно добавить конфигурации для API проксирования, кэширования и т.д.
}

Запуск через Docker

Если есть Dockerfile для фронтенда и Nginx, соберите образ и запустите контейнер:

docker build -t frontend-nginx .
docker run -p 80:80 frontend-nginx

Запуск Nginx без Docker (на сервере)

    Скопируйте статические файлы из frontend/build в папку, которая указана в конфигурации Nginx, например /usr/share/nginx/html

    Поместите файл конфигурации в /etc/nginx/sites-available/default (или в соответствующую директорию)

    Перезапустите Nginx:

sudo systemctl restart nginx

Полезные команды

    Запуск сборки фронтенда: npm run build

    Запуск локального сервера фронтенда: npm start

    Перезапуск Nginx: sudo systemctl restart nginx

    Проверка статуса Nginx: sudo systemctl status nginx

Советы

    В try_files указано fallback на index.html для поддержки SPA маршрутизации.

    Не забудьте настроить DNS или hosts файл для вашего домена, если используете его вместо IP.

    При необходимости можно настроить HTTPS с помощью сертификатов (например, Let's Encrypt).

Часто задаваемые вопросы (FAQ)

Q: Что делать, если после сборки фронтенда Nginx выдает 404?
A: Проверьте, что статические файлы действительно лежат в папке, указанной в root конфигурации Nginx, и что try_files настроен правильно.

Q: Как проксировать API-запросы через Nginx?
A: Добавьте в конфигурацию Nginx секцию location /api/ { proxy_pass http://backend_address; }