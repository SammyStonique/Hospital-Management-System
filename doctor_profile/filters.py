import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

@csrf_exempt
def department_code_search(request):
    departList = []
    data = json.loads(request.body)
    code = data['code']
    name = data['name']

    departments = Department.objects.filter(Q(code__icontains=code) & Q(name__icontains=name) )

    for dep in departments:
        obj = {
            "id": dep.id,
            "code": dep.code,
            "name": dep.name,
            # "url": "departments/%s" % dep.id
        }
        departList.append(obj)

    return JsonResponse({'departments': departList})