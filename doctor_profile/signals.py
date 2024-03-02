from django.db.models.signals import post_save,pre_save
# from users.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Doctor

UserModel = get_user_model()

@receiver(post_save, sender = UserModel)
def create_doctor(sender, instance, created, **kwargs):
    if created and instance.profile == "Doctor":
        Doctor.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name,
                                  phone_number=instance.phone_number, email=instance.email, department=instance.user_department, hospital=instance.allowed_hospital)
        print("DOCTOR CREATED SUCCESSFULLY")
    else:
        print("MISSION NOT SUCCESFUL")

@receiver(post_save, sender = UserModel)
def save_doctor(sender, instance,**kwargs):
    if instance.profile == "Doctor":
        instance.doctor.save()
    else:
        print("NOT A DOCTOR")

# @receiver(post_save, sender = UserModel)
# def update_doctor(sender, updated, instance, **kwargs):
#     if updated and  instance.profile == "Doctor":
#         Doctor.objects.update(user=instance, first_name=instance.first_name, last_name=instance.last_name,
#                                   phone_number=instance.phone_number, email=instance.email, department=instance.user_department)
#         print("DOCTOR UPDATED SUCCESSFULLY")
#     else:
#         print("UPDATING NOT SUCCESFUL")