from django.urls import path
from .views import *

urlpatterns = [
     path('usercreate', UserCreateAPIView.as_view(), name="user create"),
]
