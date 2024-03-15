from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    class Meta:
        model = Room
        fields = ['room_id','room_code','room_name','staff','department','company']

    def create(self, validated_data):
        room = Room.objects.create(**validated_data)
            
        return room
    
    def update(self, instance, validated_data):
        instance.room_code = validated_data.get('room_code', instance.room_code)
        instance.room_name = validated_data.get('room_name', instance.room_name)
        instance.staff = validated_data.get('staff', instance.staff)
        instance.department = validated_data.get('department', instance.department)

        instance.save()
        return instance