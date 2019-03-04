#!/usr/bin/env python

import pika


def callback(ch, method, properties, body):
    print(body.decode())


conn_params = pika.ConnectionParameters(host='rabbit', port=5672)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.queue_declare(queue='rabbit-queue')
channel.basic_consume(callback, queue='rabbit-queue', no_ack=True)

print("Waiting for messages. To exit press CTRL+C")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()