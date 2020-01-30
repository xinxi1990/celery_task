# -*- coding: utf-8 -*-

#!/usr/bin/env python

import Queue
import threading

message = Queue.Queue(10)


def producer(i):
    while True:
        message.put(i)


def consumer(i):
    while True:
        msg = message.get()
        print("############# {} #############".format(msg))


for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()

print("#############")