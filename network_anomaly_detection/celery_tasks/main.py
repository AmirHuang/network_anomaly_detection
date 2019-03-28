# _*_ coding: utf-8 _*_
# @time     : 2019/03/27
# @Author   : Amir
# @Site     : 
# @File     : main.py
# @Software : PyCharm

from celery import Celery
# 为celery使用django配置文件进行设置
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'network_anomaly_detection.settings'
# 创建celery应用
app = Celery('celery_tasks')
# 导入celery配置
app.config_from_object('celery_tasks.config')
# 自动注册celery任务
app.autodiscover_tasks(['celery_tasks.nt_account', 'celery_tasks.nt_resource'])


@app.task(bind=True)
def debug_task(self):
    print('------task-----')
    print('Request: {0!r}'.format(self.request))

# 启动ｃｅｌｅｒｙ应用
#  celery -A celery_tasks.main worker -l info
