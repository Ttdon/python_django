
from rest_framework.generics import *
from rest_framework.views import APIView

from .serializer import UserCreateSerializer
from ..models import RegisterUser

from rest_framework.response import Response
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    def post(selfself, request, *args, **kwargs):
     data = request.data
     serializer = UserCreateSerializer(data=data)
     if serializer.is_valid():
         serializer.save()
         return Response({
             'message': 'user created'
         },status=200)


     return Response(serializer.errors, status=400)