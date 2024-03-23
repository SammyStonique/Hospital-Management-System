from django.db import models
import uuid
from doctor_profile.models import Doctor
from financial_accounts_chart_of_accounts.models import Ledger
from users.models import User
from company.models import Company


# Create your models here.

class EmergencyContactPerson(models.Model):
    contact_person_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    patient = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="emergency_contact_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name + " " +self.last_name+ " Contact Person"}'

class Patient(models.Model):
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other'))

    patient_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient_code = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="patient_hospital", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=GENDER, default='')
    id_number = models.CharField(max_length=250)
    birth_date = models.DateField()
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    start_date = models.DateTimeField(auto_now_add=True)
    ledger_id = models.OneToOneField(Ledger, on_delete=models.SET_NULL, null=True, blank=True)
    emergency_contact_person = models.ForeignKey(EmergencyContactPerson, related_name="patient_contact_person", on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return f'{self.first_name + " " + self.last_name + " Patient"}'
    
    class Meta:
        ordering = [('-start_date')]

class PatientHistory(models.Model):
    patient_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, related_name="patient_history_patient", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, related_name="patient_history_staff", on_delete=models.SET_NULL, null=True, blank=True)
    is_doctor = models.BooleanField(default=False)
    date = models.DateField()
    notes = models.TextField()
    hospital = models.ForeignKey(Company, related_name="patient_history_hospital", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date','patient']

    def __str__(self):
        return f'{self.patient.patient_code} - {self.patient.first_name} {self.patient.last_name} History'

class PatientFollowupHistory(models.Model):
    patient_followup_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    # patient_history = models.ForeignKey(PatientHistory, related_name="patient_history_followup", on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    hospital = models.ForeignKey(Company, related_name="patient_follow_up_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient_followup_history_id} FollowUp History'

class PatientAdmissionHistory(models.Model):
    patient_admission_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    # patient_history = models.ForeignKey(PatientHistory, related_name="patient_admission_history", on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ward_no = models.CharField(max_length=250)
    bed_no = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="patient_admission_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient_admission_history_id} Admission'


class PatientDiagnosisHistory(models.Model):
    patient_diagnosis_history_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, related_name="patient_diagnosis_history", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor_diagnosis_history", on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    hospital = models.ForeignKey(Company, related_name="patient_diagnosis_hospital", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient.patient_code} - {self.patient.first_name} {self.patient.last_name} Diagnosis History'


class HealthInsurance(models.Model):
    health_insurance_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    hospital = models.ForeignKey(Company, related_name="health_insurance_hospital", on_delete=models.CASCADE)