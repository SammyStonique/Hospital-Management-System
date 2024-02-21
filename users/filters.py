import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

@csrf_exempt
def staffSearch(request):
    staffList = []
    data = json.loads(request.body)
    email = data['email']
    name = data['name']
    status = data['is_active']
    identification_no = data['identification_no']
    profile = data['profile']
    phone_number = data['phone_number']

    users = User.objects.filter(Q(email__icontains=email) & (Q(first_name__icontains=name) | Q(last_name__icontains=name))
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        users = users.filter(is_active = status)

    if profile:
        users = users.filter(profile = profile)

    for staff in users:
        obj = {
            "id": staff.id,
            "email": staff.email,
            "first_name": staff.first_name,
            "last_name": staff.last_name,
            "is_active": staff.is_active,
            "identification_no": staff.identification_no,
            "profile": staff.profile,
            "phone_number": staff.phone_number,
        }
        staffList.append(obj)

    return JsonResponse({'staff': staffList})