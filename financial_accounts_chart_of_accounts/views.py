import os
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from users.models import Manager
from company.models import Company
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.response import Response
#Pagination
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
#Pdf 
import jinja2
import pdfkit
#Excel
import xlwt
#CSV
import csv

import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

import uuid

#Data Import
from openpyxl import load_workbook

# Create your views here.

        #PAGINATION

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DefaultPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000

            #CLIENT CATEGORIES VIEWS
    
class ClientCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
    pagination_class = BasePagination

class ClientCategoryList(generics.ListCreateAPIView):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
    pagination_class = DefaultPagination

class ClientCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
        

@csrf_exempt
@api_view(['POST'])
def createClientCategory(request):
    company_id = request.data.get("company")
    company_uuid = uuid.UUID(company_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    serializer = ClientCategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(company=company)

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def getClientCategories(request):
    category_id = request.data.get("category")
    company_id = request.data.get("company")

    if category_id is not None:
        company_uuid = uuid.UUID(company_id)
        category_uuid = uuid.UUID(category_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        category = ClientCategory.objects.get(company=company, category_id=category_uuid)

        serializer = ClientCategorySerializer(category)
        return Response(serializer.data)

    else:
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        categories = ClientCategory.objects.filter(company=company)

        serializer = ClientCategorySerializer(categories, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
def updateClientCategory(request):
    category_id = request.data.get("category")
    company = request.data.get("company")
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    category_uuid = uuid.UUID(category_id)
    category = ClientCategory.objects.get(company=company_id,category_id=category_uuid)
    
    serializer = ClientCategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def deleteClientCategory(request):
    category_id = request.data.get("category")
    company = request.data.get("company")
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    category_uuid = uuid.UUID(category_id)
    category = ClientCategory.objects.get(company=company_id,category_id=category_uuid)

    category.delete() 
    message = {'msg':"The category has been succesfully deleted"} 
    return Response(message)


@csrf_exempt   
def generate_client_categories_pdf(request):
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

    context = {"categories":categoryList}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/financial_accounts_chart_of_accounts/templates/financial_accounts_chart_of_accounts')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('clientCategoryPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Client Category.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/financial_accounts_chart_of_accounts/static/financial_accounts_chart_of_accounts/clientCategoryPDF.css")

    path = 'Client Category.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Client Category.pdf'
    pdf.close()
    os.remove("Client Category.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
def generate_client_categories_excel(request):
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


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Client Categories.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Client Categories")

    row_num = 0
    columns = ['Client Category Name']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for cat in categoryList:
        row_num += 1
        row = [cat['category_name']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
def generate_client_categories_csv(request):
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

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Client Category.csv'

    writer = csv.writer(response)
    writer.writerow([ 'Client Category Name'])

    for cat in categoryList:
        writer.writerow([cat['category_name']])
    return response


            #LEDGERS VIEWS
    
class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    pagination_class = BasePagination

class LedgerList(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    pagination_class = DefaultPagination

class LedgerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
        

@csrf_exempt
@api_view(['POST'])
def createLedger(request):
    company_id = request.data.get("company")
    company_uuid = uuid.UUID(company_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    serializer = LedgerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(company=company)

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def getLedgers(request):
    ledger_id = request.data.get("ledger")
    company_id = request.data.get("company")
    ledger_type = request.data.get("ledger_type")

    if ledger_id is not None:
        company_uuid = uuid.UUID(company_id)
        ledger_uuid = uuid.UUID(ledger_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        ledger = Ledger.objects.get(company=company, ledger_id=ledger_uuid)

        serializer = LedgerSerializer(ledger)
        return Response(serializer.data)
    
    elif ledger_type is not None:
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        ledgers = Ledger.objects.filter(company=company, ledger_type=ledger_type)

        serializer = LedgerSerializer(ledgers, many=True)
        return Response(serializer.data)

    else:
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        ledgers = Ledger.objects.filter(company=company)

        serializer = LedgerSerializer(ledgers, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
def updateLedger(request):
    ledger_id = request.data.get("ledger")
    company = request.data.get("company")
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    ledger_uuid = uuid.UUID(ledger_id)
    ledger = Ledger.objects.get(company=company_id,ledger_id=ledger_uuid)
    
    serializer = LedgerSerializer(ledger, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def deleteLedger(request):
    ledger_id = request.data.get("ledger")
    company = request.data.get("company")
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    ledger_uuid = uuid.UUID(ledger_id)
    ledger = Ledger.objects.get(company=company_id,ledger_id=ledger_uuid)

    ledger.delete() 
    message = {'msg':"The ledger has been succesfully deleted"} 
    return Response(message)


@csrf_exempt   
def generate_ledgers_pdf(request):
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

        }
        chartOfAccountsList.append(obj)

    context = {"ledgerd":chartOfAccountsList}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/financial_accounts_chart_of_accounts/templates/financial_accounts_chart_of_accounts')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('ledgerPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Chart Of Accounts.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/financial_accounts_chart_of_accounts/static/financial_accounts_chart_of_accounts/clientCategoryPDF.css")

    path = 'Chart Of Accounts.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Chart Of Accounts.pdf'
    pdf.close()
    os.remove("Chart Of Accounts.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
def generate_ledgers_excel(request):
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

        }
        chartOfAccountsList.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Chart Of Accounts.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Chart Of Accounts")

    row_num = 0
    columns = ['Client Category Name']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for led in chartOfAccountsList:
        row_num += 1
        row = [led['category_name']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
def generate_ledgers_csv(request):
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

        }
        chartOfAccountsList.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Chart Of Accounts.csv'

    writer = csv.writer(response)
    writer.writerow([ 'Client Category Name'])

    for led in chartOfAccountsList:
        writer.writerow([led['category_name']])
    return response
