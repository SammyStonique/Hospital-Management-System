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
    ward_code = models.CharField(max_length=100,unique=True)
    category = models.CharField(max_length=250, choices=CATEGORIES, default='')
    wing = models.CharField(max_length=250, null=True, blank=True)
    ward_name = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="hospital_ward", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ward_code}-{self.ward_name}'
    
class Bed(models.Model):
    STATUS = (('','Select Status'),('Available','Available'),('Occupied','Occupied'),('Reserved','Reserved'))

    bed_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    bed_number = models.CharField(max_length=100)
    status = models.CharField(max_length=250, choices=STATUS, default='')
    ward = models.ForeignKey(Ward, related_name="ward_beds", on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    patient = models.ForeignKey(Patient, related_name="patient_bed", on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey(Company, related_name="hospital_bed", on_delete=models.CASCADE)

    def __str__(self):
        return f'Bed {self.bed_number}-{self.ward.ward_name}'