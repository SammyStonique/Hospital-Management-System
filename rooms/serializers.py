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
    
class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = ['ward_id','ward_code','ward_name','wing','category','hospital']

    def create(self, validated_data):
        ward = Ward.objects.create(**validated_data)
            
        return ward
    
    def update(self, instance, validated_data):
        instance.ward_code = validated_data.get('ward_code', instance.ward_code)
        instance.ward_name = validated_data.get('ward_name', instance.ward_name)
        instance.wing = validated_data.get('wing', instance.wing)
        instance.category = validated_data.get('category', instance.category)

        instance.save()
        return instance
    
class BedSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(),many=False)
    ward = serializers.PrimaryKeyRelatedField(queryset=Ward.objects.all(),many=False)
    class Meta:
        model = Room
        fields = ['bed_id','bed_number','status','ward','price','patient','hospital']

    def create(self, validated_data):
        bed = Bed.objects.create(**validated_data)
            
        return bed
    
    def update(self, instance, validated_data):
        instance.bed_number = validated_data.get('bed_number', instance.bed_number)
        instance.status = validated_data.get('status', instance.status)
        instance.ward = validated_data.get('ward', instance.ward)
        instance.price = validated_data.get('price', instance.price)
        instance.patient = validated_data.get('patient', instance.patient)

        instance.save()
        return instance