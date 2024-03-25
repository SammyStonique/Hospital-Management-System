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
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 100000

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


@api_view(['POST'])
@csrf_exempt
def journalSearch(request):
    journalList = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    journal_no = data['journal_no']
    description = data['description']
    client = data['client']
    date_from = data['date_from']
    date_to = data['date_to']
    min_amount = data['min_amount']
    max_amount = data['max_amount']
    txn_type = data['txn_type']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_journals = Journal.objects.filter(company=company_uuid)

    journals = company_journals.filter(Q(journal_no__icontains=journal_no) & Q(description__icontains=description) & Q(txn_type__icontains=txn_type))

    if date_from:
        journals = journals.filter(issue_date__gte=date_from)

    if date_to:
        journals = journals.filter(issue_date__lte=date_to)

    if min_amount:
        journals = journals.filter(total_amount__gte=min_amount)

    if max_amount:
        journals = journals.filter(total_amount__lte=max_amount)

    if client:
        journals = journals.filter(Q(client__icontains=client))

    for jnl in journals:
        obj = {
            "journal_id": jnl.journal_id,
            "journal_no": jnl.journal_no,
            "client": jnl.client,
            "issue_date": jnl.issue_date.strftime("%d %b, %Y"),
            "due_date": jnl.due_date,
            "sub_total": jnl.sub_total,
            "tax": jnl.tax,
            "total_amount": jnl.total_amount,
            "total_paid": jnl.total_paid,
            "due_amount": jnl.due_amount,
            "status": jnl.status,
            "description": jnl.description,
            "done_by": jnl.done_by,

        }
        journalList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(journalList, request)

    return  paginator.get_paginated_response(page)


@api_view(['POST'])
@csrf_exempt
def journalEntrySearch(request):
    journalEntryList = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    banking_date_from = data['banking_date_from']
    banking_date_to = data['banking_date_to']
    description = data['description']
    reference_no = data['reference_no']
    date_from = data['date_from']
    date_to = data['date_to']
    debit_amount = data['debit_amount']
    credit_amount = data['credit_amount']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_journal_entries = JournalEntry.objects.filter(company=company_uuid)

    journal_entries = company_journal_entries.filter(Q(description__icontains=description) & Q(debit_amount__eq=debit_amount) & Q(credit_amount__eq=credit_amount))

    if date_from:
        journal_entries = journal_entries.filter(date__gte=date_from)

    if date_to:
        journal_entries = journal_entries.filter(date__lte=date_to)

    if banking_date_from:
        journal_entries = journal_entries.filter(banking_date__gte=banking_date_from)

    if banking_date_to:
        journal_entries = journal_entries.filter(banking_date__lte=banking_date_to)

    if reference_no:
        journal_entries = journal_entries.filter(journal__reference_no__icontains=reference_no)

    for jnle in journal_entries:
        obj = {
            "journal_entry_id": jnle.journal_entry_id,
            "journal_no": jnle.journal.journal_no,
            "date": jnle.date,
            "banking_date": jnle.banking_date,
            "description": jnle.description,
            "txn_type": jnle.txn_type,
            "posting_account_id": jnle.posting_account.ledger_id,
            "posting_account_name": jnle.posting_account.ledger_name,
            "posting_account_code": jnle.posting_account.ledger_code,
            "debit_amount": jnle.debit_amount,
            "credit_amount": jnle.credit_amount,
            "reference_no": jnle.journal.reference_no,
            "done_by": jnle.journal.done_by,

        }
        journalEntryList.append(obj)

    pagination_class = BasePagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(journalEntryList, request)

    return  paginator.get_paginated_response(page)


@api_view(['POST'])
@csrf_exempt
def jnlSearch(request):
    journalList = []
    data = json.loads(request.body)
    patient_id = data['patient']
    company_id = data['company']
    contra = 0

    company_uuid = uuid.UUID(company_id)
    journals = Journal.objects.filter(company=company_uuid, client_id=patient_id)

    for jnl in journals:
        if jnl.txn_type == "INV":
            obj = {
                "journal_id": jnl.journal_id,
                "journal_no": jnl.journal_no,
                "date": jnl.issue_date.strftime("%d %b, %Y"),
                "description": jnl.description,
                "txn_type": jnl.txn_type,
                "debit_amount": jnl.total_amount,
                "credit_amount": contra,
                "reference_no": jnl.reference_no,
                "total_amount": jnl.total_amount,
                "done_by": jnl.done_by,

            }
            journalList.append(obj)
        elif jnl.txn_type == "RCPT":
            obj = {
                "journal_id": jnl.journal_id,
                "journal_no": jnl.journal_no,
                "date": jnl.issue_date.strftime("%d %b, %Y"),
                "description": jnl.description,
                "txn_type": jnl.txn_type,
                "debit_amount": contra,
                "credit_amount": jnl.total_amount,
                "reference_no": jnl.reference_no,
                "total_amount": jnl.total_amount,
                "done_by": jnl.done_by,

            }
            journalList.append(obj)

    pagination_class = DefaultPagination
    paginator = pagination_class()

    page = paginator.paginate_queryset(journalList, request)

    return  paginator.get_paginated_response(page)