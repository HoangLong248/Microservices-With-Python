import pika, json

params = pika.URLParameters('amqps://kkiyfxsg:kN3C7NYlYQzUbtNCAbdgU23M1vQLHyHP@armadillo.rmq.cloudamqp.com/kkiyfxsg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)