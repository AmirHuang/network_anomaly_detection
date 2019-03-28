# _*_ coding: utf-8 _*_
# @time     : 2019/03/26
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.urls import path, include, re_path
from nt_user.views import (
    UserViewset, FeedbackMessageViewset, ReturnUrlView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewset, base_name='users')
router.register(r'messages', FeedbackMessageViewset, base_name='messages')

urlpatterns = [
    path(r'index/', ReturnUrlView.as_view())
]
urlpatterns += router.urls