from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("first_name","Riex Super Admin")
        extra_fields.setdefault("user_role",1)
        return self.create_user(email=email,password=password,**extra_fields)


class User(AbstractUser):
    email=models.EmailField(max_length=254,unique=True)
    first_name=models.CharField(max_length=254,default=False)
    username=models.CharField(max_length=25,unique=True)
    user_role=models.IntegerField(null=False,max_length=1,default=False)
    img=models.TextField(null=True)
    permissions=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=CustomUserManager()

    def __str__(self):
        return self.username

 


class Institution(models.Model):
    authId=models.IntegerField(null=True)
    insGUID=models.TextField(null=True)
    insName=models.TextField(null=True)
    insId=models.CharField(max_length=200,null=True)
    addr1=models.TextField(null=True)
    addr2=models.TextField(null=True)
    city=models.TextField(null=True)
    state=models.TextField(null=True)
    pinCode=models.TextField(null=True)
    country=models.TextField(null=True)
    phone=models.TextField(null=True)
    contactPerson=models.TextField(null=True)
    insLogo=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)



    
    