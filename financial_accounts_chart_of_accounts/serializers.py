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
    

class JournalSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    journal_ledger = LedgerSerializer(many=True, read_only=True)
    class Meta:
        model = Journal
        fields = '__all__'

    def create(self, validated_data):
        journal = Journal.objects.create(**validated_data)
            
        return journal
    
    def update(self, instance, validated_data):
        instance.journal_no = validated_data.get('journal_no', instance.journal_no)
        instance.client = validated_data.get('client', instance.client)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.sub_total = validated_data.get('sub_total', instance.sub_total)
        instance.tax = validated_data.get('tax', instance.tax)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.total_paid = validated_data.get('total_paid', instance.total_paid)
        instance.due_amount = validated_data.get('due_amount', instance.due_amount)
        instance.status = validated_data.get('status', instance.status)
        instance.journal_ledger = validated_data.get('journal_ledger', instance.journal_ledger)
        instance.description = validated_data.get('description', instance.description)
        instance.reference_no = validated_data.get('reference_no', instance.reference_no)
        instance.done_by = validated_data.get('done_by', instance.done_by)

        instance.save()
        return instance
    
class JournalEntrySerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    journal = serializers.ReadOnlyField(source='journal.journal_id')
    posting_account = serializers.PrimaryKeyRelatedField(queryset=Ledger.objects.all(), many=False)
    class Meta:
        model = JournalEntry
        fields = '__all__'

    def create(self, validated_data):
        journal_entry = JournalEntry.objects.create(**validated_data)
            
        return journal_entry
    
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.posting_account = validated_data.get('posting_account', instance.posting_account)
        instance.debit_amount = validated_data.get('debit_amount', instance.debit_amount)
        instance.credit_amount = validated_data.get('credit_amount', instance.credit_amount)
        instance.description = validated_data.get('description', instance.description)
        instance.banking_date = validated_data.get('banking_date', instance.banking_date)
        instance.txn_type = validated_data.get('txn_type', instance.txn_type)

        instance.save()
        return instance