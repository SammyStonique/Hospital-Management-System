from django.db import models
import uuid
from company.models import Company
from patients_registration.models import  Patient
from users.models import User
from xtra.models import Department

# Create your models here.

class Room(models.Model):
    room_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    staff = models.CharField(max_length=250, blank=True, null=True)
    room_code = models.CharField(max_length=100,unique=True)
    room_name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, related_name="department_room", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="company_room", on_delete=models.CASCADE)

    class Meta:
        ordering = [('room_name')]

    def __str__(self):
        return f'{self.room_name} Room'
    
class Ward(models.Model):
    CATEGORIES = (('','Select Category'),('Children','Children'),('Women','Women'),('Men','Men'))

    ward_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category = models.CharField(max_length=250, choices=CATEGORIES, default='')
    wing = models.CharField(max_length=250, null=True, blank=True)
    ward_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.ward_name}'