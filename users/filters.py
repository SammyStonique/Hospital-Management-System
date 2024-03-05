import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from datetime import datetime

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
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_users = User.objects.filter(allowed_company=company_uuid)

    users = company_users.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)) & Q(user_department__name__icontains=user_department)
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        users = users.filter(is_active = status)

    if profile:
        users = users.filter(profile = profile)
    

    for staff in users:
        if (staff.profile != "Super Admin") and (staff.profile != "Patient"):
            obj = {
                "user_id": staff.user_id,
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

@api_view(['POST'])
@csrf_exempt
def managersSearch(request):
    managerList = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    department = data['department']
    manager_name = data['manager_name']
    start_date = data['start_date']
    start_date_from = data['start_date_from']
    start_date_to = data['start_date_to']
    end_date = data['end_date']
    status = data['status']
    phone_number = data['phone_number']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_managers = Manager.objects.filter(company=company_uuid)

    managers = company_managers.filter(Q(manager_name__icontains=manager_name) & Q(department__name__icontains=department)
                                 & Q(phone_number__icontains=phone_number))
    
    if status:
        if status == "True":
            managers = managers.filter(status = "Active")
        else:
            managers = managers.filter(status = "Inactive")
 

    if start_date_from:
        new_start_date_from = datetime.strptime(start_date_from, "%b %d %Y")
        final_start_date_from = new_start_date_from.strftime("%Y-%m-%d")
        managers = managers.filter(start_date__gte=final_start_date_from) 
    
    if start_date_to:
        new_start_date_to = datetime.strptime(start_date_to, "%b %d %Y")
        final_start_date_to = new_start_date_to.strftime("%Y-%m-%d")
        managers = managers.filter(start_date__lte=final_start_date_to) 

    for manager in managers:
            if manager.end_date:
                obj = {
                    "manager_id": manager.manager_id,
                    "manager_name": manager.manager_name,
                    "status": manager.status,
                    "start_date": manager.start_date.strftime("%d %b, %Y"),
                    "end_date": manager.end_date.strftime("%d %b, %Y"),
                    "phone_number": manager.phone_number,
                    "department": manager.department.name,
                }
                managerList.append(obj)
            else:
                obj = {
                    "manager_id": manager.manager_id,
                    "manager_name": manager.manager_name,
                    "status": manager.status,
                    "start_date": manager.start_date.strftime("%d %b, %Y"),
                    "phone_number": manager.phone_number,
                    "department": manager.department.name,
                }
                managerList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(managerList, request)

    return  paginator.get_paginated_response(page)



