# -*- coding: utf-8 -*-

#!/usr/bin/env python

import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='jmeterQueue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,         #获取body后执行回调函数
                      queue='jmeterQueue',
                      no_ack=True)                #自动应答开启，会给MQ服务器发送一个ack：‘已经收到了’。


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

