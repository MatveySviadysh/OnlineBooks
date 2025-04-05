FROM node:16-alpine

# Устанавливаем необходимые пакеты и создаем пользователя
RUN apk add --no-cache --virtual .gyp python3 make g++ && \
    adduser -D appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

WORKDIR /app
USER appuser

# Копируем и устанавливаем зависимости
COPY --chown=appuser:appuser package*.json ./
RUN npm config set cache /tmp/.npm-cache && \
    mkdir -p /tmp/.npm-cache && \
    chmod -R 777 /tmp/.npm-cache && \
    npm ci --no-cache

# Копируем исходный код
COPY --chown=appuser:appuser . .

# Настройки окружения
ENV HOST=0.0.0.0
ENV NODE_ENV=development
ENV CHOKIDAR_USEPOLLING=true

# Явно задаем права для кеша Babel
RUN mkdir -p /tmp/.cache/babel-loader && \
    chmod -R 777 /tmp/.cache

EXPOSE 8080

CMD ["npm", "run", "serve"]