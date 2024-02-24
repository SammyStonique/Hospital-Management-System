import os
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
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

            #DOCTORS VIEWS

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = BasePagination
    
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DefaultPagination

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

def generate_doctors_pdf(request):
    doctors = Doctor.objects.all()

    context = {"doctors":doctors}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/doctor_profile/templates/doctor_profile')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('doctorPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Doctors.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/doctor_profile/static/doctor_profile/departmentPDF.css")

    path = 'Doctors.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Doctors.pdf'
    pdf.close()
    os.remove("Doctors.pdf")  # remove the locally created pdf file.
    return response

def generate_doctors_excel(request):
    doctors = Doctor.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Doctors.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Doctors")

    row_num = 0
    columns = ['First Name', 'Last Name', 'Email', 'Payroll Number','Phone Number','Department','Specialization']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for doct in doctors:
        row_num += 1
        row = [doct.first_name,doct.last_name,doct.email,doct.payroll_number,doct.phone_number,doct.department.name,doct.specialization]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

def generate_doctors_csv(request):
    doctors = Doctor.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Doctors.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Payroll Number','Phone Number','Department','Specialization'])

    for doct in doctors:
        writer.writerow([doct.first_name,doct.last_name,doct.email,doct.payroll_number,doct.phone_number,doct.department.name,doct.specialization])
    return response
