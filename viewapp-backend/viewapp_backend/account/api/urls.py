from django.urls import path
from .view import *


urlpatterns = [

    # path('login', login, name="login"),
    path('getuser', GetUserAPIView.as_view(), name="get user"),
]