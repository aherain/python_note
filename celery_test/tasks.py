# -*- coding:utf-8 -*-

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    time.sleep(5)
    return x+y



#单个测试用例
#启动：
#celery worker -A tasks --loglevel=info


# >>> from tasks import add
# >>> add.delay(2,8)

