from django.db.models.signals import post_save,pre_save
from patients_registration.models import Patient
from django.dispatch import receiver
from django.db.models import Q
from .models import Ledger


status = "Active"
financial_statement = "Balance Sheet"


@receiver(post_save, sender = Patient)
def create_patient_ledger(sender, instance, created, **kwargs):
    if created:
        Ledger.objects.create(ledger_name=instance.first_name+" "+instance.last_name, phone_number=instance.phone_number, financial_statement=financial_statement,
                                  inv_address=instance.address, email=instance.email, status=status, company=instance.hospital)
        print("LEDGER CREATED SUCCESSFULLY")
    else:
        print("LEDGER NOT CREATED")

@receiver(post_save, sender = Patient)
def save_patient_ledger(sender, instance,**kwargs):
    instance.ledger.save()

