from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email,phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,phone_number, password, **other_fields)
    
    def create_user(self, email,phone_number,password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other')) 

    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=250,blank=True)
    last_name = models.CharField(max_length=250,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=250,choices=GENDER,default='',blank=True)
    phone_number = models.CharField(max_length=250)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= False)
    start_date = models.DateTimeField(auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name','age','gender']

    def __str__(self):
        return f'{self.email}'
