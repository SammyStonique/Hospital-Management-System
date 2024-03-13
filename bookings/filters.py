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
def appointmentsSearch(request):
    appointmentsList = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    patient = data['patient_name']
    doctor = data['doctor_name']
    from_date = data['from_date']
    to_date = data['to_date']
    hospital_id = data['hospital']

    appointments = Appointment.objects.filter((Q(patient__first_name__icontains=patient)|Q(patient__last_name__icontains=patient)) 
                                & (Q(doctor__first_name__icontains=doctor)|Q(doctor__last_name__icontains=doctor)) )

    if from_date:
        appointments = appointments.filter(date__gte=from_date) 
    
    if to_date:
        appointments = appointments.filter(date__lte=to_date) 

    for apt in appointments:
        if (str(apt.hospital.company_id) == hospital_id):
            obj = {
                "appointment_id": apt.appointment_id,
                "patient_id": apt.patient.patient_id,
                "patient_name": apt.patient.first_name + " "+ apt.patient.last_name,
                "patient_id_number": apt.patient.id_number,
                "doctor_id": apt.doctor.doctor_id,
                "doctor_name": apt.doctor.first_name + " "+ apt.doctor.last_name,
                "date": apt.date.strftime("%d %b, %Y"),
                "time": apt.time,
                "notes": apt.notes,
            }
            appointmentsList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(appointmentsList, request)

    return  paginator.get_paginated_response(page)