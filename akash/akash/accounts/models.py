from django.db import models

# Create your models here.
class AccountsUser(models.Model):
    password =models.CharField(max_length=128)
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.CharField(max_length=254)
    mobile_number=models.CharField(max_length=20,blank=True,null=True)


    class Meta:
        managed=False
        db_table='accounts_user'
