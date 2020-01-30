
# -*- coding: utf-8 -*-



from __future__ import absolute_import
from celery.schedules import crontab
from datetime import timedelta

# 使用redis存储任务队列
broker_url = 'redis://192.168.1.103:6379/10'
# 使用redis存储结果
result_backend = 'redis://192.168.1.103:6379/13'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
# 时区设置
timezone = 'Asia/Shanghai'
# celery默认开启自己的日志
# False表示不关闭
worker_hijack_root_logger = False
# 存储结果过期时间，过期后自动删除
# 单位为秒
result_expires = 60 * 60 * 24

# 导入任务所在文件
imports = [
    # 'celery_task.app_scripts.test1',
    # 'celery_task.app_scripts.test2',
    'celery_task.app_scripts.task_requests',
]

# 需要执行任务的配置
beat_schedule = {
    # 'test1': {
    #     # 具体需要执行的函数
    #     # 该函数必须要使用@app.task装饰
    #     'task': 'celery_task.app_scripts.test1.test1_run',
    #     # 定时时间
    #     # 每分钟执行一次，不能为小数
    #     'schedule': crontab(minute='*/1'),
    #     # 或者这么写，每小时执行一次
    #     # "schedule": crontab(minute=0, hour="*/1")
    #     # 执行的函数需要的参数
    #     'args': ()
    # },
    # 'test2': {
    #     'task': 'celery_task.app_scripts.test2.test2_run',
    #     # 设置定时的时间，10秒一次
    #     'schedule': timedelta(seconds=1),
    #     'args': ()
    # },

    'task_requests': {
        'task': 'celery_task.app_scripts.task_requests.test_get_request_2019_nCoV',
        # 设置定时的时间，10秒一次
        'schedule': timedelta(seconds=5),
        'args': ()
    }
    # },
    # 'task_requests_1': {
    #     'task': 'celery_task.app_scripts.task_requests.test_get_request_1',
    #     # 设置定时的时间，10秒一次
    #     'schedule': timedelta(seconds=1),
    #     'args': ()
    # }
}

# CELERYBEAT_SCHEDULE = {
#     'celery_app.task.task1': {
#         'task': 'celery_app.task.task1',
#         'schedule': timedelta(seconds=20),
#         'args': (1, 10)
#     },
#     'celery_app.task.task2': {
#         'task': 'celery_app.task.task2',
#         'schedule': crontab(minute='*/2'),
#         'args': ()
#     }
# }