from random import random

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.templatetags.rest_framework import data
from accounts.api.serializer import UserCreateSerializer


# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.data
#
#     # user_obj = User.objects.create(email=data['email'], first_name=data['first_name'], last_name=data['last_name'],
#     #                                mobile_number=data['mobile_number'])
#     user_obj.set_password(data['password'])
#     user_obj.save()
#     message = 'Sign-up successfully. Please verify Your mobile number'
#
#     mobile_number = data.get("mobile_number")
@api_view(['POST'])
def registration_view(request):
    if request.method =='POST':
        serializer =UserCreateSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            Account=serializer.save()
            data['response']='successfully register'
            data['email']=Account.email
            data['first_name']=Account.first_name
            data['last_name']=Account.last_name
        else:
            data=serializer.errors
            return Response(data)
