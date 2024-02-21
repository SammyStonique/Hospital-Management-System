from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','identification_no','birth_date','gender','phone_number','profile','image','is_staff','is_active']