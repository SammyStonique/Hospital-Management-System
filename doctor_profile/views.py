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

            #DOCTORS VIEWS
    
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


            #DEPARTMENTS VIEWS
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = BasePagination

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

def generate_departments_pdf(request):
    departments = Department.objects.all()

    context = {"departments":departments}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/doctor_profile/templates/doctor_profile')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('departmentPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Departments.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/doctor_profile/static/doctor_profile/departmentPDF.css")

    path = 'Departments.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Departments.pdf'
    pdf.close()
    os.remove("Departments.pdf")  # remove the locally created pdf file.
    return response

def generate_departments_excel(request):
    departments = Department.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Departments.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Departments")

    row_num = 0
    columns = ['Code', 'Name', 'Manager', 'Start Date']
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num])

    for dep in departments:
        row_num += 1
        row = [dep.code,dep.name]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

def generate_departments_csv(request):
    departments = Department.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Departments.csv'

    writer = csv.writer(response)
    writer.writerow(['Code', 'Name', 'Manager', 'Start Date'])

    for dep in departments:
        writer.writerow([dep.code, dep.name])
    return response

            #MANAGER VIEWS
    
class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
