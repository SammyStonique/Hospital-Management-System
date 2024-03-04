import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from .models import *
from users.models import *

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['POST'])
@csrf_exempt
def departmentSearch(request):
    departList = []
    empty = ""
    data = json.loads(request.body)
    code = data['code']
    name = data['name']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_departments = Department.objects.filter(company=company_uuid)

    departments = company_departments.filter(Q(code__icontains=code) & Q(name__icontains=name) )

    for dep in departments:
        manager = Manager.objects.filter(department=dep)
        if len(manager):
            obj = {
                "department_id": dep.department_id,
                "code": dep.code,
                "name": dep.name,
                "manager_first_name": manager[0].user.first_name,
                "manager_last_name": manager[0].user.last_name,
                "start_date": manager[0].start_date.strftime("%d %b, %Y")
            }
            departList.append(obj)
        else:
            obj = {
                "department_id": dep.department_id,
                "code": dep.code,
                "name": dep.name,
                "manager_first_name": empty,
                "manager_last_name": empty,
                "start_date": empty
            }
            departList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(departList, request)

    return  paginator.get_paginated_response(page)
