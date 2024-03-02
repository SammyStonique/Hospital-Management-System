from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    user_department = serializers.ReadOnlyField(source='user_department.name')
    allowed_company = serializers.ReadOnlyField(source='allowed_company.company_id')
    class Meta:
        model = User
        fields = ['user_id','email','first_name','last_name','identification_no','birth_date','gender','phone_number','profile','image','is_staff','is_active','user_department','allowed_company']


class ManagerSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    class Meta:
        model = Manager
        fields = ['manager_id','user','start_date','phone_number','department','end_date','status']

    def create(self, validated_data):
        manager = Manager.objects.create(**validated_data)
            
        return manager
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.end_date = validated_data.get('end_date', instance.end_date)

        instance.save()
        return instance