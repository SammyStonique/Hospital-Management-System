from django.db import models
import uuid
from doctor_profile.models import Doctor
from company.models import Company


# Create your models here.

class EmergencyContactPerson(models.Model):
    contact_person_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="emmergency_contact_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name + " " +self.last_name+ " Contact Person"}'

class Patient(models.Model):
    patient_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    hospital = models.ForeignKey(Company, related_name="patient_hospital", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    id_number = models.CharField(max_length=250)
    birth_date = models.DateField()
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    emergency_contact_person = models.ForeignKey(EmergencyContactPerson, related_name="patient_contact_person", on_delete=models.DO_NOTHING,blank=True, null=True)

    def __str__(self):
        return f'{self.first_name + " " + self.last_name + " Patient"}'

class PatientHistory(models.Model):
    patient_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, related_name="patient_history", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor_history", on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    hospital = models.ForeignKey(Company, related_name="patient_history_hospital", on_delete=models.CASCADE)


class PatientFollowupHistory(models.Model):
    patient_followup_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient_history = models.ForeignKey(PatientHistory, related_name="patient_history", on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    hospital = models.ForeignKey(Company, related_name="patient_follow_up_hospital", on_delete=models.CASCADE)

class PatientAdmissionHistory(models.Model):
    patient_admission_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient_history = models.ForeignKey(PatientHistory, related_name="patient_admission_history", on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ward_no = models.CharField(max_length=250)
    bed_no = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="patient_admission_hospital", on_delete=models.CASCADE)


class PatientDiagnosisHistory(models.Model):
    patient_diagnosis_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, related_name="patient_diagnosis_history", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor_diagnosis_history", on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    hospital = models.ForeignKey(Company, related_name="patient_diagnosis_hospital", on_delete=models.CASCADE)


class HealthInsurance(models.Model):
    health_insurance_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="health_insurance_hospital", on_delete=models.CASCADE)