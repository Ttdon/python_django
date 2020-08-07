
from rest_framework.serializers import *
from ..models import RegisterUser
from rest_framework.exceptions import APIException


class APIException400(APIException):
    status_code = 400


class UserCreateSerializer(ModelSerializer):
    first_name = CharField(required=True, error_messages={'required':'first name key is required', 'blank':'first name value is required'})
    last_name = CharField(required=True, allow_blank=False)
    email = EmailField(required=True, allow_blank=False)
    phone = CharField(required=True, allow_blank=False)
    address = CharField(required=True, allow_blank=False)
    password = CharField(required=True, allow_blank=False)

    def validate(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        password = data['password']

        if not first_name:
            raise APIException400({
                'message':'first name is required'
            })
        if not last_name:
            raise APIException400({
                'message':'last name is required'
            })
        if not email:
            raise APIException400({
                'message':'email is required'
            })
        if not phone:
            raise APIException400({
                'message':'phone is required'
            })
        if not address:
            raise APIException400({
                'message':'address is required'
            })
        if not password:
            raise APIException400({
                'message':'password is required'
            })
        if len(password) < 8:
            raise APIException400({
                'message':'password must be atleast 8 characters'
            })

        return data

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        phone = validated_data['phone']
        address = validated_data['address']
        password = validated_data['password']

        user_obj = RegisterUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data

    class Meta:
        model = RegisterUser
        fields = '__all__'
