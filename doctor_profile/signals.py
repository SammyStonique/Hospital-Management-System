from django.db.models.signals import post_save
from users.models import User
from django.dispatch import receiver
from .models import Doctor

@receiver(post_save, sender = User, dispatch_uid="user_creation")
def create_doctor(sender, instance, created, **kwargs):
    if User.profile == "Doctor" and created:
        Doctor.objects.create(user=instance)

# @receiver(post_save, sender = User, dispatch_uid="user_updation")
# def save_doctor(sender, instance,**kwargs):
#     instance.doctor.save()