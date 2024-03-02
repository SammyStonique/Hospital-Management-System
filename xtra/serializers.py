from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    class Meta:
        model = Department
        fields = ['department_id','code','name','company']

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
            
        return department
    
    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance
    