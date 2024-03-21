from django.db import models
import uuid
# from patients_registration.models import PatientHistory, HealthInsurance
from patients_registration.models import HealthInsurance
from financial_accounts_chart_of_accounts.models import Ledger
from company.models import  Company


# Create your models here.

class PatientBill(models.Model):
    patient_bill_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    # patient_history = models.ForeignKey(PatientHistory, related_name="patient_bill_history", on_delete=models.CASCADE)
    health_insurance = models.ForeignKey(HealthInsurance, related_name="patient_health_insurance", on_delete=models.DO_NOTHING)
    patient_payable = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_payable = models.DecimalField(max_digits=10, decimal_places=2)


class PatientBillPaymentHistory(models.Model):
    patient_bill_payment_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient_bill = models.ForeignKey(PatientBill, related_name="patient_bills", on_delete=models.DO_NOTHING)
    patient_paid = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class MedicalFee(models.Model):
    fees_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    fee_name = models.CharField(max_length=250)
    posting_account = models.ForeignKey(Ledger, related_name="fees_posting_account", on_delete=models.CASCADE)
    default_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    company = models.ForeignKey(Company, related_name="company_medical_fees", on_delete=models.CASCADE)


    class Meta:
        ordering = ['fee_name']

    def __str__(self):
        return f'{self.fee_name} - Medical Fees'