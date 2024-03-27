from django.db import models
import uuid
from company.models import Company

# Create your models here.

class ClientCategory(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company, related_name="company_client_category", on_delete=models.CASCADE)

    class Meta:
        ordering= [('name')]

    def __str__(self):
        return f'{self.name} Category'

class Ledger(models.Model):

    STATUS = (('','Select Status'),('Active','Active'),('Inactive','Inactive'))
    FINANCIAL_STATEMENT = (('','Select Financial Statement'),('Balance Sheet','Balance Sheet'),('Income Statement','Income Statement'))
    LEDGER_TYPE = (('','Select Ledger Type'),('Cashbook','Cashbook'),('Current Asset','Current Asset'),('Fixed Asset','Fixed Asset'),('Current Liability','Current Liability')
                   ,('Longterm Liability','Longterm Liability'),('Owner Equity','Owner Equity'),('Income','Income'),('Expenses','Expenses'))

    ledger_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ledger_code = models.CharField(max_length=250, unique=True)
    ledger_name = models.CharField(max_length=250)
    ledger_type = models.CharField(max_length=250, choices=LEDGER_TYPE, default='')
    overdue_bills = models.IntegerField(default=0,blank=True, null=True)
    pending_bills = models.IntegerField(default=0,blank=True, null=True)
    cleared_bills = models.IntegerField(default=0,blank=True, null=True)
    all_bills = models.IntegerField(default=0,blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    client_type = models.ForeignKey(ClientCategory, related_name="client_type_ledger", on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.CharField(max_length=250,blank=True, null=True)
    pin_no = models.CharField(max_length=250,blank=True, null=True)
    amt_overdue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.CharField(max_length=250,blank=True, null=True)
    status = models.CharField(max_length=250, choices=STATUS, default='Active')
    financial_statement = models.CharField(max_length=250, choices=FINANCIAL_STATEMENT, default='')
    contact_person = models.CharField(max_length=250,blank=True, null=True)
    inv_address = models.CharField(max_length=250,blank=True, null=True)
    ship_address = models.CharField(max_length=250,blank=True, null=True)
    company = models.ForeignKey(Company, related_name="company_ledger", on_delete=models.CASCADE)

    class Meta:
        ordering = ['ledger_type','ledger_code']

    def __str__(self):
        return f'{self.ledger_code} - {self.ledger_name} Ledger'

class Journal(models.Model):

    STATUS = (('','Select Status'),('Open','Open'),('Closed','Closed'))
    TRANSACTION_TYPE = (('','Select Txn Type'),('BAL','BAL'),('JNL','JNL'),('INV','INV'),('RCPT','RCPT'),('PMT','PMT'))

    journal_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    journal_no = models.CharField(max_length=250,blank=True, null=True)
    txn_type = models.CharField(max_length=250, choices=TRANSACTION_TYPE, default='JNL')
    client = models.CharField(max_length=250,blank=True, null=True)
    client_id = models.CharField(max_length=250,blank=True, null=True)
    issue_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=250, choices=STATUS, default='Open')
    description = models.TextField()
    reference_no = models.CharField(max_length=250,blank=True, null=True)
    done_by = models.CharField(max_length=250,blank=True, null=True)
    company = models.ForeignKey(Company, related_name="company_journal", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-journal_no']

    def __str__(self):
        return f'{self.journal_no} Journal'
    

class JournalEntry(models.Model):

    TRANSACTION_TYPE = (('','Select Txn Type'),('BAL','BAL'),('JNL','JNL'),('INV','INV'),('RCPT','RCPT'),('PMT','PMT'))

    journal_entry_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    journal = models.ForeignKey(Journal, related_name="journal_entryy", on_delete=models.CASCADE)
    date = models.DateField()
    banking_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    txn_type = models.CharField(max_length=250, choices=TRANSACTION_TYPE, default='JNL')
    posting_account = models.ForeignKey(Ledger, related_name="journal_entry_posting_account", on_delete=models.CASCADE)
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    company = models.ForeignKey(Company, related_name="company_journal_entry", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date','journal']

    def __str__(self):
        return f'{self.journal.journal_no} Journal Entry'