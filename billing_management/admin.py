from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PatientBill)
admin.site.register(PatientBillPaymentHistory)
admin.site.register(MedicalFee)
