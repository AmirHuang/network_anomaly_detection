# _*_ coding: utf-8 _*_
# @time     : 2019/03/28
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.urls import path
from nt_resource.views import (
    CatNormalResourceView,
    CatNormalResourceListView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cat_normal_list', CatNormalResourceListView, base_name='cat_normal_list')

urlpatterns = [
    path(r'cat_normal_resource/', CatNormalResourceView.as_view()),
    # url(r'^cat_normal_list$', cat_list),
]

urlpatterns += router.urls