# _*_ coding: utf-8 _*_
# @time     : 2019/03/27
# @Author   : Amir
# @Site     : 
# @File     : tasks.py
# @Software : PyCharm

from celery_tasks.main import app
from nt_account.models import UserApiRecordHistory


@app.task
def save_api_record_task(data):
    """
    保存用户使用的接口记录
    :param data:
    :return:
    """
    api_history = UserApiRecordHistory(**data)
    api_history.save()