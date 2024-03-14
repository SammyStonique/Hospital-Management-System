from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    user_department_name = serializers.ReadOnlyField(source='user_department.name')
    user_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    allowed_company = serializers.ReadOnlyField(source='allowed_company.company_id')
    class Meta:
        model = User
        fields = ['user_id','email','first_name','last_name','identification_no','birth_date','gender','phone_number','profile','image','is_staff','is_active','user_department','user_department_name','allowed_company']


class ManagerSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    company = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Manager
        fields = ['manager_id','user','manager_name','start_date','phone_number','department','end_date','status','company']

    def create(self, validated_data):
        manager = Manager.objects.create(**validated_data)
            
        return manager
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.manager_name = validated_data.get('manager_name', instance.manager_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()
        return instance