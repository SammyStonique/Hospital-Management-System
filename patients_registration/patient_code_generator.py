from django.http import HttpResponse
import uuid
from .models import Patient

#Function to generate patient_code
def patient_code_gen(hospital_id):
        hospital_uuid = uuid.UUID(hospital_id)
        last_code = Patient.objects.filter(hospital=hospital_uuid).order_by('patient_code').last()
        if not last_code:
            return "PAT0001"
        patient_code = last_code.patient_code
        patient_code_int = int(patient_code.split('PAT')[-1])
        new_patient_code_int = patient_code_int + 1
        new_patient_code = 'PAT'+ str(new_patient_code_int).zfill(4)
        
        return new_patient_code

class PatientCodeGenerator:
        def __init__(self, patient_code):
                self.patient_code = patient_code

def patient_code_generator(request, hospital_id):
        patient_code = patient_code_gen(hospital_id)
        p1 = PatientCodeGenerator(patient_code)
        return HttpResponse(p1.patient_code)
