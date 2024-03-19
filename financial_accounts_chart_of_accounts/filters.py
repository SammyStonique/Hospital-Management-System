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

class DefaultPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['POST'])
@csrf_exempt
def clientCategorySearch(request):
    categoryList = []
    data = json.loads(request.body)
    category_name = data['category_name']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    client_categories = ClientCategory.objects.filter(company=company_uuid)

    categories = client_categories.filter(Q(name__icontains=category_name) )

    for cat in categories:
        obj = {
            "category_id": cat.category_id,
            "category_name": cat.name,

        }
        categoryList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(categoryList, request)

    return  paginator.get_paginated_response(page)

@api_view(['POST'])
@csrf_exempt
def chartOfAccountsSearch(request):
    chartOfAccountsList = []
    data = json.loads(request.body)
    ledger_code = data['ledger_code']
    ledger_name = data['ledger_name']
    financial_statement = data['financial_statement']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_ledgers = Ledger.objects.filter(company=company_uuid)

    ledgers = company_ledgers.filter(Q(ledger_name__icontains=ledger_name) & Q(ledger_code__icontains=ledger_code))

    if financial_statement:
        ledgers = ledgers.filter(financial_statement = financial_statement)

    for led in ledgers:
        obj = {
            "ledger_id": led.ledger_id,
            "ledger_code": led.ledger_code,
            "ledger_name": led.ledger_name,
            "ledger_type": led.ledger_type,
            "financial_statement": led.financial_statement,
            "balance": led.balance,
            "status": led.status,

        }
        chartOfAccountsList.append(obj)

    pagination_class = DefaultPagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(chartOfAccountsList, request)

    return  paginator.get_paginated_response(page)