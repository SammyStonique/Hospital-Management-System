from django.db import models
import uuid
from doctor_profile.models import Doctor
from company.models import Company
from patients_registration.models import Patient

# Create your models here.


class Appointment(models.Model):
    appointment_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, related_name="patient_appointment", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor_appointment", on_delete=models.SET_NULL,blank=True, null=True)
    patient_name = models.CharField(max_length=250, null=True, blank=True)
    doctor_name = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    hospital = models.ForeignKey(Company, related_name="appointment_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient.first_name + " " + self.patient.last_name+ " -#"+self.patient.id_number} Appointment'
    
    class Meta:
        ordering=[('-date')]