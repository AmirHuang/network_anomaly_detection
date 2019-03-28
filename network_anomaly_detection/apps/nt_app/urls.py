# _*_ coding: utf-8 _*_
# @time     : 2019/03/27
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm


from django.urls import path
from nt_app.views import (
    CatResourceView,
    CatResourceListView
)

urlpatterns = [
    path(r'cat_resource/', CatResourceView.as_view()),
    path(r'cat_list/', CatResourceListView.as_view()),
]
