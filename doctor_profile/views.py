import os
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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

import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


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



@csrf_exempt
@api_view(['POST'])
def createDoctor(request):
    hospital_id = request.data.get("hospital")
    department_id = request.data.get("department")
    hospital_uuid = uuid.UUID(hospital_id)
    department_uuid = uuid.UUID(department_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    department = Department.objects.get(department_id=department_uuid)
    serializer = DoctorSerializer(data=request.data)


    if serializer.is_valid():
        serializer.save(department=department,hospital=hospital)

    else:
        print(serializer.errors) 
    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def getDepartmentDoctors(request):
    doctor_id = request.data.get("doctor")
    hospital_id = request.data.get("hospital")
    department_id = request.data.get("department")

    if doctor_id is not None and department_id is not None:
        department_uuid = uuid.UUID(department_id)
        hospital_uuid = uuid.UUID(hospital_id)
        doctor_uuid = uuid.UUID(doctor_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        doctor = Doctor.objects.get(hospital=hospital, department=department_uuid, doctor_id=doctor_uuid)

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    elif department_id is not None:
        department_uuid = uuid.UUID(department_id)
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        doctor = Doctor.objects.filter(hospital=hospital, department=department_uuid)

        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

    else:
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        doctor = Doctor.objects.filter(hospital=hospital)

        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

csrf_exempt
@api_view(['PUT'])
def updateDepartmentDoctor(request):
    doctor_id = request.data.get("doctor")
    hospital = request.data.get("hospital")
    doctor_uuid = uuid.UUID(doctor_id)
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    doctor = Doctor.objects.get(hospital=hospital_id, doctor_id=doctor_uuid)
    
    serializer = DoctorSerializer(doctor, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors)

    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def deleteDoctor(request):
    doctor_id = request.data.get("doctor")
    department_id = request.data.get("department")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    department_uuid = uuid.UUID(department_id)
    doctor_uuid = uuid.UUID(doctor_id)
    department = get_object_or_404(Department, company=hospital_uuid, department_id=department_uuid)
    doctor = Doctor.objects.get(hospital=hospital_uuid,department=department, doctor_id=doctor_uuid)

    doctor.delete() 
    message = {'msg':"The doctor has been succesfully deleted"} 
    return Response(message)



@csrf_exempt   
def generate_doctors_pdf(request):
    doctors = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    specialization = data['specialization']
    department = data['department']
    payroll_number = data['payroll_number']
    phone_number = data['phone_number']
    hospital_id = data['hospital']

    doctorsList = Doctor.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(department__name__icontains=department)
                                & Q(specialization__icontains=specialization) & Q(phone_number__icontains=phone_number) & Q(payroll_number__icontains=payroll_number) )

    

    for doct in doctorsList:
        if (str(doct.hospital.company_id) == hospital_id):
            obj = {
                "doctor_id": doct.doctor_id,
                "email": doct.email,
                "first_name": doct.first_name,
                "last_name": doct.last_name,
                "specialization": doct.specialization,
                "payroll_number": doct.payroll_number,
                "phone_number": doct.phone_number,
                "department": doct.department,
            }
            doctors.append(obj)

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

@csrf_exempt  
def generate_doctors_excel(request):
    doctors = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    specialization = data['specialization']
    department = data['department']
    payroll_number = data['payroll_number']
    phone_number = data['phone_number']
    hospital_id = data['hospital']

    doctorsList = Doctor.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(department__name__icontains=department)
                                & Q(specialization__icontains=specialization) & Q(phone_number__icontains=phone_number) & Q(payroll_number__icontains=payroll_number) )

    

    for doct in doctorsList:
        if (str(doct.hospital.company_id) == hospital_id):
            obj = {
                "doctor_id": doct.doctor_id,
                "email": doct.email,
                "first_name": doct.first_name,
                "last_name": doct.last_name,
                "specialization": doct.specialization,
                "payroll_number": doct.payroll_number,
                "phone_number": doct.phone_number,
                "department": doct.department.name,
            }
            doctors.append(obj)

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
        row = [doct['first_name'],doct['last_name'],doct['email'],doct['payroll_number'],doct['phone_number'],doct['department'],doct['specialization']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
def generate_doctors_csv(request):
    doctors = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    specialization = data['specialization']
    department = data['department']
    payroll_number = data['payroll_number']
    phone_number = data['phone_number']
    hospital_id = data['hospital']

    doctorsList = Doctor.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(department__name__icontains=department)
                                & Q(specialization__icontains=specialization) & Q(phone_number__icontains=phone_number) & Q(payroll_number__icontains=payroll_number) )

    

    for doct in doctorsList:
        if (str(doct.hospital.company_id) == hospital_id):
            obj = {
                "doctor_id": doct.doctor_id,
                "email": doct.email,
                "first_name": doct.first_name,
                "last_name": doct.last_name,
                "specialization": doct.specialization,
                "payroll_number": doct.payroll_number,
                "phone_number": doct.phone_number,
                "department": doct.department.name,
            }
            doctors.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Doctors.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Payroll Number','Phone Number','Department','Specialization'])

    for doct in doctors:
        writer.writerow([doct['first_name'],doct['last_name'],doct['email'],doct['payroll_number'],doct['phone_number'],doct['department'],doct['specialization']])
    return response
