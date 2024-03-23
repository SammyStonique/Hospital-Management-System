from django.db.models.signals import post_save,post_delete
from patients_registration.models import Patient
from django.dispatch import receiver
from .models import Ledger


status = "Active"
financial_statement = "Balance Sheet"
ledger_type = "Current Asset"


@receiver(post_save, sender = Patient)
def create_ledger(sender, instance, created, **kwargs):
    if created:
        ledger = Ledger.objects.create(ledger_code=instance.patient_code, ledger_type=ledger_type, ledger_name=instance.first_name+" "+instance.last_name, phone_number=instance.phone_number, financial_statement=financial_statement,
                                  inv_address=instance.address, email=instance.email, status=status, company=instance.hospital)
        Patient.objects.filter(patient_code=instance.patient_code).update(ledger_id=ledger)
        ledger.save()

@receiver(post_delete, sender = Patient)
def delete_ledger(sender, instance, **kwargs):
        if instance.ledger_id:
            ledger = Ledger.objects.get(ledger_code=instance.patient_code, company=instance.hospital)
            ledger.delete()
            print("LEDGER DELETED SUCCESSFULLY")

