from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    hospital = serializers.ReadOnlyField(source='hospital.name')
    class Meta:
        model = Doctor
        fields = ['doctor_id','first_name','last_name','email','phone_number','specialization','department','payroll_number','user','hospital']

    def create(self, validated_data):
        doctor = Doctor.objects.create(**validated_data)
            
        return doctor

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.payroll_number = validated_data.get('payroll_number', instance.payroll_number)
        instance.department = validated_data.get('department', instance.department)

        instance.save()
        return instance
    