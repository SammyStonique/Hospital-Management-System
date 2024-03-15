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
