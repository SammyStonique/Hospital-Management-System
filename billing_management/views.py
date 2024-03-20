import environ,os
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

import re
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from company.models import Company
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#Pagination
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
from hms.utils import insert_commas

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


           #MedicalFeeS VIEWS
    
class MedicalFeeList(generics.ListCreateAPIView):
    queryset = MedicalFee.objects.all()
    serializer_class = MedicalFeeSerializer

class MedicalFeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalFee.objects.all()
    serializer_class = MedicalFeeSerializer


@csrf_exempt
@api_view(['POST'])
def createMedicalFee(request):
    hospital_id = request.data.get("hospital")
    ledger_id = request.data.get("posting_account")
    hospital_uuid = uuid.UUID(hospital_id)
    ledger_uuid = uuid.UUID(ledger_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    posting_account = Ledger.objects.get(company=hospital, ledger_id=ledger_uuid)
    serializer = MedicalFeeSerializer(data=request.data)


    if serializer.is_valid():
        serializer.save(company=hospital, posting_account=posting_account)

    else:
        print(serializer.errors) 
    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def getMedicalFees(request):
    fees_id = request.data.get("fees")
    hospital_id = request.data.get("hospital")

    if fees_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        fees_uuid = uuid.UUID(fees_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        fee = MedicalFee.objects.get(company=hospital, fees_id=fees_uuid)

        serializer = MedicalFeeSerializer(fee)
        return Response(serializer.data)

    else:
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        fees = MedicalFee.objects.filter(company=hospital)

        serializer = MedicalFeeSerializer(fees, many=True)
        return Response(serializer.data)

csrf_exempt
@api_view(['PUT'])
def updateMedicalFee(request):
    fees_id = request.data.get("fees")
    hospital_id = request.data.get("hospital")
    fees_uuid = uuid.UUID(fees_id)
    hospital_uuid = uuid.UUID(hospital_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    fee = MedicalFee.objects.get(company=hospital,fees_id=fees_uuid)
    
    serializer = MedicalFeeSerializer(fee, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors)

    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def deleteMedicalFee(request):
    fees_id = request.data.get("fees")
    hospital_id = request.data.get("hospital")
    fees_uuid = uuid.UUID(fees_id)
    hospital_uuid = uuid.UUID(hospital_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    fee = MedicalFee.objects.get(company=hospital,fees_id=fees_uuid)

    fee.delete() 
    message = {'msg':"The medical fee has been succesfully deleted"} 
    return Response(message)

        #ROOM REPORTS

@csrf_exempt 
@api_view(['POST'])
def generate_medical_fees_pdf(request):
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
            "posting_account_name": fee.posting_account.ledger_code+' - '+fee.posting_account.ledger_name,
            "fees_amount": round(fee.default_amount),

        }
        feesList.append(obj)

    context = {"fees":feesList}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/billing_management/templates/billing_management')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('medicalFeesPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Medical Fees.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/billing_management/static/billing_management/medicalFeesPDF.css")

    path = 'Medical Fees.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Medical Fees.pdf'
    pdf.close()
    os.remove("Medical Fees.pdf")  # remove the locally created pdf file.
    return response

@api_view(['POST'])
@csrf_exempt
def generate_medical_fees_excel(request):
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
            "posting_account_name": fee.posting_account.ledger_code+' - '+fee.posting_account.ledger_name,
            "fees_amount": fee.default_amount,

        }
        feesList.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Medical Fees.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Medical Fees")

    row_num = 0
    columns = ['Name', 'Posting Account','Default Amount']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style = style1)

    for fee in feesList:
        row_num += 1
        row = [fee['fees_name'],fee['posting_account_name'], fee['fees_amount']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@api_view(['POST'])
@csrf_exempt
def generate_medical_fees_csv(request):
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
            "posting_account_name": fee.posting_account.ledger_code+' - '+fee.posting_account.ledger_name,
            "fees_amount": fee.default_amount,

        }
        feesList.append(obj)


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Medical Fees.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Posting Account','Default Amount'])

    for fee in feesList:
        writer.writerow([fee['fees_name'],fee['posting_account_name'], fee['fees_amount']])
    return response

