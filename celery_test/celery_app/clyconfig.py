from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

CELERY_TIMEZONE='Asia/Shang'

CELERY_IMPORTS = ('celery_app.task1',
                  'celery_app.task2')

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),
        'args': (5, 8)
    },

    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=9, minute=50),
        'args': (3, 7)
    }
}

#启动 Celery Beat 进程，定时将任务发送到 Broker，在项目根目录下执行下面命令
# celery beat -A celery_app

# celery -B -A celery_app worker --loglevel=info


