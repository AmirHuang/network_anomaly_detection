# _*_ coding: utf-8 _*_
# @time     : 2019/03/26
# @Author   : Amir
# @Site     : 
# @File     : permissions.py
# @Software : PyCharm

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
