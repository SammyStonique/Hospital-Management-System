from django.db.models.signals import post_delete
from .models import Patient, EmergencyContactPerson
from django.dispatch import receiver




@receiver(post_delete, sender = Patient)
def delete_contact_person(sender, instance, **kwargs):
        if instance.emergency_contact_person:
            contact_person = EmergencyContactPerson.objects.get(contact_person_id=instance.emergency_contact_person.contact_person_id, hospital=instance.hospital)
            contact_person.delete()
            print("CONTACT PERSON DELETED SUCCESSFULLY")