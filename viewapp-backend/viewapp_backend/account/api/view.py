
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.views.generic import ListView
from rest_framework.views import APIView
from ..models import RegisterUser
from rest_framework.response import Response
from .serializer import *
from django.core import serializers
class GetUserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        qs = RegisterUser.objects.all()
        data = RegisterUserDetailsSerilaizer(qs, many=True).data
        print(data)
        return Response({
            'message':'Register user list',
            'data':data
        }, status=HTTP_200_OK)