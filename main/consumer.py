import pika

params = pika.URLParameters('amqps://kkiyfxsg:kN3C7NYlYQzUbtNCAbdgU23M1vQLHyHP@armadillo.rmq.cloudamqp.com/kkiyfxsg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Receive in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()