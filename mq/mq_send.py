# -*- coding: utf-8 -*-

#!/usr/bin/env python
import pika
#
# for i in range(10000):
#
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#
#     channel.queue_declare(queue='hello_{0}'.format(i))
#     print("#############")
#
#     channel.basic_publish(exchange='',
#                           routing_key='hello_{0}'.format(i),
#                           body='Hello World_{0}!'.format(i))
#     print(" [x] Sent 'Hello World!'")



#!/usr/bin/env python

import pika

# ######################### 生产者 #########################


for i in range(100):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()  # 创建通道

    channel.queue_declare(queue='hello')  # 队列名称

    channel.basic_publish(exchange='',
                          routing_key='hello',  # 路由名称
                          body='Hello World!_{0}'.format(i))  # 发送内容
    print(" [x] Sent 'Hello World_{0}!'".format(i))
    connection.close()

