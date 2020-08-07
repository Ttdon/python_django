from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class RegisterUser(AbstractUser):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)

def __str__(self):
    return self.first_name