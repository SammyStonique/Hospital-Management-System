import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from .models import *
from company.models import Company

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['POST'])
@csrf_exempt
def patientsSearch(request):
    patientList = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    id_number = data['id_number']
    city = data['city']
    birth_date = data['birth_date']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_patients = Patient.objects.filter(hospital=hospital_uuid)

    patients = hospital_patients.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(birth_date__icontains=birth_date)
                                        & Q(phone_number__icontains=phone_number) & Q(id_number__icontains=id_number) & Q(city__icontains=city))

    for pat in patients:
        if(pat.emergency_contact_person):
            obj = {
                "patient_id": pat.patient_id,
                "first_name": pat.first_name,
                "last_name": pat.last_name,
                "email": pat.email,
                "id_number": pat.id_number,
                "phone_number": pat.phone_number,
                "city": pat.city,
                "address": pat.address,
                "country": pat.country,
                "birth_date": pat.birth_date.strftime("%d %b, %Y"),
                "emergency_contact_person_id": pat.emergency_contact_person.contact_person_id,
                "emergency_contact_person_name": pat.emergency_contact_person.first_name + " "+pat.emergency_contact_person.last_name,
                "emergency_contact_person_email": pat.emergency_contact_person.email,
                "emergency_contact_person_phone_number": pat.emergency_contact_person.phone_number,
            }
            patientList.append(obj)
        else:
            obj = {
                "patient_id": pat.patient_id,
                "first_name": pat.first_name,
                "last_name": pat.last_name,
                "email": pat.email,
                "id_number": pat.id_number,
                "phone_number": pat.phone_number,
                "city": pat.city,
                "address": pat.address,
                "country": pat.country,
                "birth_date": pat.birth_date.strftime("%d %b, %Y"),
            }
            patientList.append(obj)

        

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(patientList, request)

    return  paginator.get_paginated_response(page)


@api_view(['POST'])
@csrf_exempt
def contactPersonSearch(request):
    contactPersonList = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone_number = data['phone_number']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    patients_contact_persons = EmergencyContactPerson.objects.filter(hospital=hospital_uuid)

    contact_persons = patients_contact_persons.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) 
                                                       & Q(email__icontains=email) & Q(phone_number__icontains=phone_number))
                                        

    for cont in contact_persons:
        obj = {
            "contact_person_id": cont.contact_person_id,
            "first_name": cont.first_name,
            "last_name": cont.last_name,
            "email": cont.email,
            "phone_number": cont.phone_number,
            "patient": cont.patient
        }
        contactPersonList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(contactPersonList, request)

    return  paginator.get_paginated_response(page)