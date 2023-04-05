import os
from celery import Celery

#设置环境变量，加载 Django 的 settings
os.environ.setdefault('DIANGO_SETTINGS_MODULE','swiper.settings')

#创建 Celery Application
celery_app = Celery('swiper')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks() # 自动发现通过装饰器定义的所有任务

def call_by_worker(func):
    '''将任务在 Celery 中异步进行'''
    task=celery_app.task(func)
    return task.delay