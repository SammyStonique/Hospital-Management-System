from rest_framework import serializers
from .models import *

class ClientCategorySerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    class Meta:
        model = ClientCategory
        fields = ['category_id','name','company']

    def create(self, validated_data):
        category = ClientCategory.objects.create(**validated_data)
            
        return category
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance
    
class LedgerSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    client_type = serializers.ReadOnlyField(source='client_type.name')
    class Meta:
        model = Ledger
        fields = '__all__'

    def create(self, validated_data):
        ledger = Ledger.objects.create(**validated_data)
            
        return ledger
    
    def update(self, instance, validated_data):
        instance.ledger_code = validated_data.get('ledger_code', instance.ledger_code)
        instance.ledger_name = validated_data.get('ledger_name', instance.ledger_name)
        instance.ledger_type = validated_data.get('ledger_type', instance.ledger_type)
        instance.overdue_bills = validated_data.get('overdue_bills', instance.overdue_bills)
        instance.pending_bills = validated_data.get('pending_bills', instance.pending_bills)
        instance.cleared_bills = validated_data.get('cleared_bills', instance.cleared_bills)
        instance.all_bills = validated_data.get('all_bills', instance.all_bills)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.client_type = validated_data.get('client_type', instance.client_type)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.pin_no = validated_data.get('pin_no', instance.pin_no)
        instance.amt_overdue = validated_data.get('amt_overdue', instance.amt_overdue)
        instance.email = validated_data.get('email', instance.email)
        instance.status = validated_data.get('status', instance.status)
        instance.financial_statement = validated_data.get('financial_statement', instance.financial_statement)
        instance.contact_person = validated_data.get('contact_person', instance.contact_person)
        instance.inv_address = validated_data.get('inv_address', instance.inv_address)
        instance.ship_address = validated_data.get('ship_address', instance.ship_address)


        instance.save()
        return instance