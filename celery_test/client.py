# -*- coding: utf-8 -*-
import time
from celery_app import task1
from celery_app import task2


task1.add.apply_async(args=[2, 8])  # 也可用 task1.add.delay(2, 8)
task2.multiply.apply_async(args=[3, 7])  # 也可用 task2.multiply.delay(3, 7)
print '计算任务已经派发，5秒后将进行下一次任务派发'
time.sleep(5)


