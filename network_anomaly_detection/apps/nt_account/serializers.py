# _*_ coding: utf-8 _*_
# @time     : 2019/03/27
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from nt_account.models import UserApiRecordHistory


class UserApiRecordHistorySer(serializers.ModelSerializer):
    class Meta:
        model = UserApiRecordHistory
        fields = '__all__'
