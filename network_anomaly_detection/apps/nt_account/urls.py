# _*_ coding: utf-8 _*_
# @time     : 2019/03/27
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.urls import path

from nt_account.views import GenerateTokenView


urlpatterns = [
    path('generate_token/', GenerateTokenView.as_view())
]
