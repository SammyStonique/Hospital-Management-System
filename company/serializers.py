from .models import *
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id','name','town','logo','email','phone_number','kra_pin','registration_number','country']