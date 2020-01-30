# 背景
celery



# celery命令

``` bash
发布任务
celery -A celery_task beat
执行任务
celery -A celery_task worker -l info -P eventlet
将以上两条合并
celery -B -A celery_task worker
后台启动celery worker进程
celery multi start work_1 -A appcelery
停止worker进程，如果无法停止，加上-A
celery multi stop WORKNAME
重启worker进程
celery multi restart WORKNAME
查看进程数
celery status -A celery_task

celery -B -A celery_task worker --loglevel=info
```