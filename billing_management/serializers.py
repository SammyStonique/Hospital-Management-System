from rest_framework import serializers
from .models import *

class MedicalFeeSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    posting_account = serializers.PrimaryKeyRelatedField(queryset=Ledger.objects.all(), many=False)
    class Meta:
        model = MedicalFee
        fields = '__all__'

    def create(self, validated_data):
        medical_fee = MedicalFee.objects.create(**validated_data)
            
        return medical_fee
    
    def update(self, instance, validated_data):
        instance.fee_name = validated_data.get('fee_name', instance.fee_name)
        instance.posting_account = validated_data.get('posting_account', instance.posting_account)
        instance.default_amount = validated_data.get('default_amount', instance.default_amount)

        instance.save()
        return instance