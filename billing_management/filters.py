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
def medicalFeesSearch(request):
    feesList = []
    data = json.loads(request.body)
    fees_name = data['fees_name']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    medical_fees = MedicalFee.objects.filter(company=hospital_uuid)

    fees = medical_fees.filter(Q(fee_name__icontains=fees_name) )

    for fee in fees:
        obj = {
            "fees_id": fee.fees_id,
            "fees_name": fee.fee_name,
            "posting_account_id": fee.posting_account.ledger_id,
            "posting_account_code": fee.posting_account.ledger_code,
            "posting_account_name": fee.posting_account.ledger_name,
            "fees_amount": fee.default_amount,

        }
        feesList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(feesList, request)

    return  paginator.get_paginated_response(page)