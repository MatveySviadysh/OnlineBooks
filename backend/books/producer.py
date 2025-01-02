import pika
import json

# Параметры подключения к RabbitMQ
params = pika.URLParameters(
    'amqps://kbbyzakw:nAG9OKoU1ofXTP5cajel-izZcI8VpmLY@armadillo.rmq.cloudamqp.com/kbbyzakw'
)

# Устанавливаем соединение и создаем канал
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Функция для публикации сообщений
def publish(method, body):
    channel.basic_publish(
        exchange='', 
        routing_key='admin',  # Указываем ту же очередь, что и у consumer
        body=json.dumps(body),
        properties= pika.BasicProperties(method)     # Конвертируем сообщение в JSON-строку
    )
