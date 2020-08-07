from django.contrib import admin
from django.urls import path,include

from accounts.api.views import UserCreateAPIView

urlpatterns = [

     path('create',UserCreateAPIView.as_view()),
]
