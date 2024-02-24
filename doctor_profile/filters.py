import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

@csrf_exempt
def doctorSearch(request):
    doctorsList = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    specialization = data['specialization']
    department = data['department']
    payroll_number = data['payroll_number']
    phone_number = data['phone_number']

    doctors = Doctor.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(department__name__icontains=department)
                                & Q(specialization__icontains=specialization) & Q(phone_number__icontains=phone_number) & Q(payroll_number__icontains=payroll_number) )

    

    for doct in doctors:
        obj = {
            "id": doct.id,
            "email": doct.email,
            "first_name": doct.first_name,
            "last_name": doct.last_name,
            "specialization": doct.specialization,
            "payroll_number": doct.payroll_number,
            "phone_number": doct.phone_number,
            "department": doct.department.name,
        }
        doctorsList.append(obj)

    return JsonResponse({'doctors': doctorsList})