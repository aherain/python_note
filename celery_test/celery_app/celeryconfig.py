BROKER_URL = 'redis://127.0.0.1:6379'               #Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  #Backend

CELERY_TIMEZONE='Asia/Beijing'                     #UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (                                  #hhh
    'celery_app.task1',
    'celery_app.task2'
)