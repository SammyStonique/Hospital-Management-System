from django.db.models.signals import post_save
# from users.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Doctor

UserModel = get_user_model()

@receiver(post_save, sender = UserModel)
def create_doctor(sender, instance, created, **kwargs):
    if created and instance.profile == "Doctor":
        Doctor.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name,
                                  phone_number=instance.phone_number, email=instance.email)
        print("DOCTOR CREATED SUCCESSFULLY")
    else:
        print("MISSION NOT SUCCESFUL")

@receiver(post_save, sender = UserModel)
def save_doctor(sender, instance,**kwargs):
    if instance.profile == "Doctor":
        instance.doctor.save()
    else:
        print("NOT A DOCTOR")