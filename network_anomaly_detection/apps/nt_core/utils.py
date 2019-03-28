# _*_ coding: utf-8 _*_
# @time     : 2019/03/26
# @Author   : Amir
# @Site     : 
# @File     : utils.py
# @Software : PyCharm
import time


REGEX_MOBILE = "^1[3456789]\d{9}$"

def get_current_timestamp():
    """
    获取当前时间戳
    :return:
    """
    return int(time.time()) * 1000