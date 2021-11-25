from django.contrib import admin
from django.urls import path, include
from .views import LoginApi, UserListApi, UserDetailsApi

app_name = 'api'

urlpatterns = [
    path('v1/login', LoginApi),
    path('v1/user/list', UserListApi),
    path('v1/user/details', UserDetailsApi)
]
