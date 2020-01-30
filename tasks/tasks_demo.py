# -*- coding: utf-8 -*-

from celery import Celery
from celery.schedules import crontab

app = Celery('demo')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(10.0, test_celery.s('hello'), name='add every 10')    #每10秒　　test_celery为下面定义的函数，‘hello’为传入的参数

    sender.add_periodic_task(30.0, test_celery.s('world'), expires=10)               #每30秒发送一次

    sender.add_periodic_task(

        crontab(hour=13, minute=50, day_of_week=3),      #每周一7点半

        test_celery.s('Happy Mondays!'),
    )

# 创建任务函数
@app.task
def my_task():
    print("######### hello world #########")
    return 'hello world'


# 创建任务函数
@app.task
def test_celery(arg):
    print("######### {} #########".format(arg))
    return 'hello world'



###############################

"""
celery -A tasks worker --loglevel=info

from tasks import my_task
my_task.delay()
"""


"""
celery -A tasks worker --loglevel=info

from tasks import my_task_add
ret = my_task_add.delay(3,4)
ret.failed()
ret.result
"""

"""
celery -B -A tasks worker --loglevel=info

"""




