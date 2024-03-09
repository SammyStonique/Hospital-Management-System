from django.db import models
import uuid
from patients_registration.models import PatientHistory, HealthInsurance


# Create your models here.

class PatientBill(models.Model):
    patient_bill_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient_history = models.ForeignKey(PatientHistory, related_name="patient_bill_history", on_delete=models.CASCADE)
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