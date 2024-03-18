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

            #DEPARTMENTS VIEWS
    
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
