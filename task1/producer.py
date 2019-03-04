#!/usr/bin/env python

import pika
import time
import random


conn_params = pika.ConnectionParameters(host='rabbit', port=5672)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.queue_declare(queue='rabbit-queue')

try:
    while True:
        num = random.random()
        channel.basic_publish(exchange='', routing_key='rabbit-queue', body=str(num))
        print("Sent number: ", str(num))
        time.sleep(random.randint(1, 3))

except KeyboardInterrupt:
    # channel.queue_delete(queue='rabbit-queue')
    connection.close()



