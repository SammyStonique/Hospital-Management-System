import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import *
from users.models import *

@csrf_exempt
def departmentSearch(request):
    departList = []
    empty = ""
    data = json.loads(request.body)
    code = data['code']
    name = data['name']

    departments = Department.objects.filter(Q(code__icontains=code) & Q(name__icontains=name) )

    for dep in departments:
        manager = Manager.objects.filter(department=dep)
        if len(manager):
            obj = {
                "code": dep.code,
                "name": dep.name,
                "manager_first_name": manager[0].user.first_name,
                "manager_last_name": manager[0].user.last_name,
                "start_date": manager[0].start_date.strftime("%d %b, %Y")
            }
            departList.append(obj)
        else:
            obj = {
                "code": dep.code,
                "name": dep.name,
                "manager_first_name": empty,
                "manager_last_name": empty,
                "start_date": empty
            }
            departList.append(obj)

    return JsonResponse({'departments': departList})