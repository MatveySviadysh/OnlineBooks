import pika
import json

# Параметры подключения к RabbitMQ
params = pika.URLParameters(
    'amqps://kbbyzakw:nAG9OKoU1ofXTP5cajel-izZcI8VpmLY@armadillo.rmq.cloudamqp.com/kbbyzakw'
)

# Устанавливаем соединение и создаем канал
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Указываем, какую очередь слушать
channel.queue_declare(queue='admin')

# Callback для обработки сообщений
def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")  # Выводим полученное сообщение

# Настраиваем consumer
channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("start_consuming")
channel.start_consuming()

# Закрываем канал (будет вызван после завершения работы consumer)
channel.close()
