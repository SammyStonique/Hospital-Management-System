from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    class Meta:
        model = Doctor
        fields = ['id','first_name','last_name','email','phone_number','specialization','department','payroll_number','user']

    def create(self, validated_data):
        doctor = Doctor.objects.create(**validated_data)
            
        return doctor

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('department', instance.department)

        instance.save()
        return instance
    