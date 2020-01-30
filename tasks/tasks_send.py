# -*- coding: utf-8 -*-


# 调用任务

from tasks import my_task_add
ret = my_task_add.delay(10,50)


print(ret.ready()) # 判断任务是否执行完毕
print(ret.failed()) # 是否失败
print(ret.result) # 结果
print(ret.get(timeout=1))
print(ret.get(propagate=False))
print(ret.ready())
print(ret.traceback)


