from rest_framework.serializers import ModelSerializer
from ..models import RegisterUser


class RegisterUserDetailsSerilaizer(ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'