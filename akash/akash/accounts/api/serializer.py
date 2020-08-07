from django.contrib.auth.models import User
from django.forms import CharField, EmailField
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.exceptions import APIException

# class APIException400(APIException):
# 	 status_code =  400
#
#
# class UserCreateSerializer(Serializer):
# 	first_name = CharField(error_messages={'required': 'first name token key required'})
# 	last_name = CharField(error_messages={'required': 'last name key required'})
# 	email = EmailField( error_messages={'required': 'email key required'})
# 	mobile_number = CharField( error_messages={'required': 'mobile number key required'})
# 	password = CharField( error_messages={'required': 'password key required'})
#
# 	def validate(self, data):
# 		mobile_number = data['mobile_number']
# 		password = data['password']
# 		email = data['email']
# 		first_name = data['first_name']
# 		last_name = data['last_name']
#
#
# 		# device type validation
#
#
# 		if first_name == '':
# 			raise APIException400({
# 					'message': 'First name is required',
# 				})
#
# 		if last_name == '':
# 				raise APIException400({
# 					'message': 'Last name is required',
# 				})
# 		if mobile_number.isdigit():
# 			user_qs = User.objects.filter(mobile_number__iexact=mobile_number, 										  account_type='1').exclude(mobile_number__isnull=True).exclude(
# 				mobile_number__iexact='').distinct()
# 			if user_qs.exists():
# 				raise APIException400({
# 					'message': 'User with this mobile number is already exists',
# 				})
# 			else:
# 				raise APIException400({
# 					'message': 'Please correct your mobile number',
# 				})
# 			user_qs = User.objects.filter(email__iexact=email)
# 			if user_qs.exists():
# 				raise APIException400({
# 					'message': 'User with this Email already exists',
# 				})
# 			if len(password) < 8:
# 				raise APIException400({
# 					'message': 'Password must be at least 8 characters',
# 				})
#
#
from accounts.models import AccountsUser


class UserCreateSerializer(serializers.ModelSerializer):
	#password2 = serializers.CharField(style={'input type':'password'},write_only=True)

	class Meta:
		model = AccountsUser
		fields = ['first_name','last_name','mobile_number','password']
		extra_kwargs = {
 'password':{'write_only':True}
		}

class APIException400(APIException):
	status_code = 400

	def save(self):
		account = AccountsUser(
						email=self.validated_data['email'],
						first_name=self.validated_data['first_name'],
						last_name=self.validated_data['last_name'],
						mobile_number=self.validated_data['mobile_number'],
						password=self.validated_data['password']
				)


	def validate(self, data):
		mobile_number = data['mobile_number']
		password = data['password']
		email = data['email']
		first_name = data['first_name']
		last_name = data['last_name']

		if first_name == '':
			raise APIException400({
				'message': 'First name is required',
			})

		if last_name == '':
			raise APIException400({
				'message': 'Last name is required',
			})

		# pass validation
		if len(password) < 8:
			raise APIException400({
				'message': 'Password must be at least 8 characters',
			})




