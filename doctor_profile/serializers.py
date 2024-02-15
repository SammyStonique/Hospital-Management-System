from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','code','name']

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
            
        return department
    
    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance
    
class ManagerSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Manager
        fields = ['id','name','start_date','phone_number','department','end_date','status']

    def create(self, validated_data):
        manager = Manager.objects.create(**validated_data)
            
        return manager

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    # department = serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Doctor
        # fields = ['first_name','last_name','email','phone_number','specialization','department','payroll_number','user']
        fields = ['id','first_name','last_name','email','phone_number','specialization','payroll_number','user']

    def create(self, validated_data):
        doctor = Doctor.objects.create(**validated_data)
            
        return doctor
