import pika

params = pika.URLParameters('amqps://kkiyfxsg:kN3C7NYlYQzUbtNCAbdgU23M1vQLHyHP@armadillo.rmq.cloudamqp.com/kkiyfxsg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')