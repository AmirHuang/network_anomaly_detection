"""network_anomaly_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve
from network_anomaly_detection.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nt_user.urls')),
    path('', include('nt_account.urls')),
    path('', include('nt_app.urls')),
    path(r'nt_resource/', include('nt_resource.urls')),
    path('docs/', include_docs_urls(title='Amir接口文档')),
    # rest_framework自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    # rest_framework自带的登录
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # jwt的认证接口
    path('login/', obtain_jwt_token),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
]
