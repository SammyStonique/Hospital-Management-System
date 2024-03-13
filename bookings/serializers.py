from rest_framework import serializers
from .models import *


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(),many=False)
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(),many=False)
    hospital = serializers.ReadOnlyField(source='hospital.name')
    class Meta:
        model = Appointment
        fields = ['appointment_id','patient','doctor','date','notes','hospital','time','doctor_name','patient_name']

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)
            
        return appointment

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.doctor = validated_data.get('doctor', instance.doctor)
        instance.doctor_name = validated_data.get('doctor_name', instance.doctor_name)
        instance.time = validated_data.get('time', instance.time)

        instance.save()
        return instance