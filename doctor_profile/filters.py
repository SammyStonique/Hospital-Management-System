import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from .models import *

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['POST'])
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
    hospital_id = data['hospital']

    doctors = Doctor.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(department__name__icontains=department)
                                & Q(specialization__icontains=specialization) & Q(phone_number__icontains=phone_number) & Q(payroll_number__icontains=payroll_number) )

    

    for doct in doctors:
        if (str(doct.hospital.company_id) == hospital_id):
            obj = {
                "doctor_id": doct.doctor_id,
                "email": doct.email,
                "first_name": doct.first_name,
                "last_name": doct.last_name,
                "specialization": doct.specialization,
                "payroll_number": doct.payroll_number,
                "phone_number": doct.phone_number,
                "department": doct.department.name,
                "department_id": doct.department.department_id
            }
            doctorsList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(doctorsList, request)

    return  paginator.get_paginated_response(page)