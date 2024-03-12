from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    hospital = serializers.ReadOnlyField(source='hospital.company_id')
    emergency_contact_person = serializers.PrimaryKeyRelatedField(queryset=EmergencyContactPerson.objects.all(),many=False)
    class Meta:
        model = Patient
        fields = ['patient_id','first_name','last_name','email','id_number','phone_number','address','birth_date','city','country','hospital','emergency_contact_person']

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
            
        return patient
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.id_number = validated_data.get('id_number', instance.id_number)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.address = validated_data.get('address', instance.address)
        instance.emergency_contact_person = validated_data.get('emergency_contact_person', instance.emergency_contact_person)

        instance.save()
        return instance
    

class EmergencyContactPersonSerializer(serializers.ModelSerializer):
    hospital = serializers.ReadOnlyField(source='hospital.company_id')
    class Meta:
        model = EmergencyContactPerson
        fields = ['contact_person_id','first_name','last_name','email','phone_number','patient','hospital']

    def create(self, validated_data):
        contact_person = EmergencyContactPerson.objects.create(**validated_data)
            
        return contact_person
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.patient = validated_data.get('patient', instance.patient)

        instance.save()
        return instance