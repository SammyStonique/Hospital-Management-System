import json
from django.db.models import Q
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
def roomSearch(request):
    roomsList = []
    data = json.loads(request.body)
    room_code = data['room_code']
    room_name = data['room_name']
    department = data['department']
    company_id = data['company']

    company_uuid = uuid.UUID(company_id)
    department_rooms = Room.objects.filter(company=company_uuid)

    rooms = department_rooms.filter(Q(room_code__icontains=room_code) & Q(room_name__icontains=room_name) & Q(department__name__icontains=department) )

    for rom in rooms:
        obj = {
            "room_id": rom.room_id,
            "room_code": rom.room_code,
            "room_name": rom.room_name,
            "department_id": rom.department.department_id,
            "department_name": rom.department.name,
            "staff": rom.staff
        }
        roomsList.append(obj)
            


    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(roomsList, request)

    return  paginator.get_paginated_response(page)


@api_view(['POST'])
@csrf_exempt
def wardSearch(request):
    wardsList = []
    data = json.loads(request.body)
    ward_code = data['ward_code']
    ward_name = data['ward_name']
    wing = data['wing']
    category = data['category']
    hospital_id = data['hospital']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_wards = Ward.objects.filter(hospital=hospital_uuid)

    wards = hospital_wards.filter(Q(ward_code__icontains=ward_code) & Q(ward_name__icontains=ward_name) & Q(wing__icontains=wing))

    if category:
        wards = wards.filter(category = category)
    
    for wrd in wards:
        obj = {
            "ward_id": wrd.ward_id,
            "ward_code": wrd.ward_code,
            "ward_name": wrd.ward_name,
            "wing": wrd.wing,
            "category": wrd.category,
        }
        wardsList.append(obj)
            


    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(wardsList, request)

    return  paginator.get_paginated_response(page)


@api_view(['POST'])
@csrf_exempt
def bedSearch(request):
    bedsList = []
    empty = ""
    data = json.loads(request.body)
    bed_number = data['bed_number']
    ward = data['ward']
    status = data['status']
    category = data['category']
    hospital_id = data['hospital']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_beds = Bed.objects.filter(hospital=hospital_uuid)

    beds = hospital_beds.filter(Q(bed_number__icontains=bed_number) & Q(ward__ward_name__icontains=ward) & Q(ward__category__icontains=category))

    if status:
        beds = beds.filter(status = status)

    for bed in beds:
        if(bed.patient is not None):
            obj = {
                "bed_id": bed.bed_id,
                "bed_number": bed.bed_number,
                "status": bed.status,
                "ward_id": bed.ward.ward_id,
                "ward_code": bed.ward.ward_code,
                "ward_name": bed.ward.ward_name,
                "ward_category": bed.ward.category, 
                "price": bed.price,
                "patient_id": bed.patient.patient_id,
                "patient_name": bed.patient.first_name + " "+bed.patient.last_name,
            }
            bedsList.append(obj)
        else:
            obj = {
                "bed_id": bed.bed_id,
                "bed_number": bed.bed_number,
                "status": bed.status,
                "ward_id": bed.ward.ward_id,
                "ward_code": bed.ward.ward_code,
                "ward_name": bed.ward.ward_name,
                "ward_category": bed.ward.category, 
                "price": bed.price,
                "patient_id": empty,
                "patient_name": empty,
            }
            bedsList.append(obj)
            


    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(bedsList, request)

    return  paginator.get_paginated_response(page)