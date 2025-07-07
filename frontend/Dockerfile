FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 8081

CMD ["npm", "run", "serve", "--", "--port", "8081", "--host", "0.0.0.0"]
