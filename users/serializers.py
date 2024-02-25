from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    user_department = serializers.ReadOnlyField(source='user_department.name')
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','identification_no','birth_date','gender','phone_number','profile','image','is_staff','is_active','user_department']


class ManagerSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    class Meta:
        model = Manager
        fields = ['id','user','start_date','phone_number','department','end_date','status']

    def create(self, validated_data):
        manager = Manager.objects.create(**validated_data)
            
        return manager
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance