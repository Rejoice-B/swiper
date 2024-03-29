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
from social import api as social_api
from vip import api as vip_api
urlpatterns = [
    path('api/user/vcode/', user_api.get_verify_code),
    path('api/user/login/', user_api.login),
    path('api/user/logint/', user_api.loginText),
    path('api/user/del/', user_api.delectUser),
    path('api/user/profile/show/', user_api.show_profile),
    path('api/user/profile/modify/', user_api.modify_profile),
    path('api/user/avatar/upload/', user_api.upload_avatar),

    path('api/social/get_rcmd_users/', social_api.get_rcmd_users),
    path('api/social/like/', social_api.like),
    path('api/social/superlike/', social_api.superlike),
    path('api/social/dislike/', social_api.dislike),
    path('api/social/rewind/', social_api.rewind),
    path('api/social/show_liked_me/', social_api.show_liked_me),
    path('api/social/friends/', social_api.get_friends),

    path('api/vip/permissions/', vip_api.show_vip_permissions),

]