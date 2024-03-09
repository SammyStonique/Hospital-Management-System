from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EmergencyContactPerson)
admin.site.register(Patient)
admin.site.register(PatientHistory)
admin.site.register(PatientFollowupHistory)
admin.site.register(PatientAdmissionHistory)
admin.site.register(PatientDiagnosisHistory)
admin.site.register(HealthInsurance)