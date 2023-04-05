"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from user import api as user_api

urlpatterns = [
    path('api/user/vcode/', user_api.get_verify_code),
    path('api/user/login/', user_api.login),
    path('api/user/logint/', user_api.loginText),
    path('api/user/del/', user_api.delectUser),
    path('api/user/profile/show/', user_api.show_profile),
    path('api/user/profile/modify/', user_api.modify_profile),
    # url(r'^api/uer/avatar/upload', user_api.upload_avatar),
]