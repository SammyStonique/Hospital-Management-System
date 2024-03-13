from django.db import models
from django.contrib.auth import get_user_model
from xtra.models import Department
from company.models import Company
import uuid

UserModel = get_user_model()


class Doctor(models.Model):
    doctor_id =models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,null=True,blank=True)
    payroll_number = models.CharField(max_length=250, blank=True)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    email = models.EmailField()
    department = models.ForeignKey(Department, related_name='departments', on_delete=models.DO_NOTHING, blank=True)
    specialization = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="doctor_hospital", on_delete=models.CASCADE)


    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'
    
    class Meta:
        ordering = [('first_name')]
