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
def staffSearch(request):
    staffList = []
    data = json.loads(request.body)
    user_department = data['user_department']
    name = data['name']
    status = data['is_active']
    identification_no = data['identification_no']
    profile = data['profile']
    phone_number = data['phone_number']
    hospital_id = data['hospital_id']

    users = User.objects.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)) & Q(user_department__name__icontains=user_department)
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        users = users.filter(is_active = status)

    if profile:
        users = users.filter(profile = profile)
    

    for staff in users:
        if (staff.profile != "Super Admin") and (staff.profile != "Patient") and (str(staff.allowed_company.company_id) == hospital_id):
            obj = {
                "id": staff.id,
                "email": staff.email,
                "first_name": staff.first_name,
                "last_name": staff.last_name,
                "is_active": staff.is_active,
                "identification_no": staff.identification_no,
                "profile": staff.profile,
                "phone_number": staff.phone_number,
                "user_department": staff.user_department.name,
            }
            staffList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(staffList, request)

    return  paginator.get_paginated_response(page)