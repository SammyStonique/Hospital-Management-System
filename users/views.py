import environ,os
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

import re
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import *
from company.models import Company
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime,timedelta
#Pagination
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
#SMS Config
import africastalking
username = env('AFRICASTALKING_USERNAME')
api_key = env('AFRICASTALKING_API_KEY')
africastalking.initialize(username, api_key)  
sms = africastalking.SMS
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

from django.contrib.auth import get_user_model
UserModel = get_user_model()

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = BasePagination
    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
@api_view(['POST'])
def getDepartmentStaff(request):
    department_id = request.data.get("department")
    company = request.data.get("company")
    staff_id = request.data.get("staff")

    if staff_id is not None:
        staff_uuid = uuid.UUID(staff_id)
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company)
        allowed_company = get_object_or_404(Company, company_id=company_uuid)
        staff = User.objects.get(allowed_company=allowed_company, user_department=department_uuid,user_id=staff_uuid)

        serializer = UserSerializer(staff)

        return Response(serializer.data)
    else:
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company)
        allowed_company = get_object_or_404(Company, company_id=company_uuid)
        staff = User.objects.filter(allowed_company=allowed_company, user_department=department_uuid)

        serializer = UserSerializer(staff, many=True)

        return Response(serializer.data)


@csrf_exempt
def send_user_credentials(request, user_id): 
    data = json.loads(request.body)
    temporary_password = data['temporary_password']
    created_user = get_object_or_404(User, user_id=user_id)
    phone_number = created_user.phone_number
    first_name = created_user.first_name
    email = created_user.email

    if(phone_number.startswith("+254")):
        pn = phone_number
    elif(phone_number.startswith('0')):
        pn = re.sub("0","+254",phone_number,1)
    elif (phone_number.startswith('7') or phone_number.startswith('1')):
        pn = "+254"+phone_number
    elif(phone_number.startswith('254')):
        pn = "+"+phone_number

    sms.send(f'Dear {first_name}, Your KHS Username: {email}, Temporary Password: {temporary_password}',[f'{pn}'],callback=send_user_credentials)

    return HttpResponse("Credentials successfully sent")

api_view(['POST'])
@csrf_exempt
def reset_password(request,user_id):
    data = json.loads(request.body)
    new_password = data['new_password']
    user = UserModel.objects.get(user_id=user_id)
    user.set_password(new_password)
    user.save()

    return HttpResponse("Password Changed Succesfully")

@csrf_exempt 
def generate_staff_pdf(request):
    staff = []
    data = json.loads(request.body)
    user_department = data['user_department']
    name = data['name']
    status = data['is_active']
    identification_no = data['identification_no']
    profile = data['profile']
    phone_number = data['phone_number']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_users = User.objects.filter(allowed_company=company_uuid)

    staffList = company_users.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)) & Q(user_department__name__icontains=user_department)
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        staffList = staffList.filter(is_active = status)

    if profile:
        staffList = staffList.filter(profile = profile)
    

    for stf in staffList:
        if stf.profile != "Super Admin" and stf.profile != "Patient":
            obj = {
                "user_id": stf.user_id,
                "email": stf.email,
                "first_name": stf.first_name,
                "last_name": stf.last_name,
                "is_active": stf.is_active,
                "identification_no": stf.identification_no,
                "profile": stf.profile,
                "phone_number": stf.phone_number,
                "user_department": stf.user_department.name,
            }
            staff.append(obj)

    context = {"staff":staff}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/users/templates/users')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('staffPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Staff.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/users/static/users/staffPDF.css")

    path = 'Staff.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Staff.pdf'
    pdf.close()
    os.remove("Staff.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
def generate_staff_excel(request):
    staff = []
    data = json.loads(request.body)
    user_department = data['user_department']
    name = data['name']
    status = data['is_active']
    identification_no = data['identification_no']
    profile = data['profile']
    phone_number = data['phone_number']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_users = User.objects.filter(allowed_company=company_uuid)

    staffList = company_users.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)) & Q(user_department__name__icontains=user_department)
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        staffList = staffList.filter(is_active = status)

    if profile:
        staffList = staffList.filter(profile = profile)
    

    for stf in staffList:
        if stf.profile != "Super Admin" and stf.profile != "Patient" and (str(stf.allowed_company.company_id) == company_id):
            obj = {
                "user_id": stf.user_id,
                "email": stf.email,
                "first_name": stf.first_name,
                "last_name": stf.last_name,
                "is_active": stf.is_active,
                "identification_no": stf.identification_no,
                "profile": stf.profile,
                "phone_number": stf.phone_number,
                "user_department": stf.user_department.name,
            }
            staff.append(obj)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Staff.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Staff")

    row_num = 0
    columns = ['First Name','Last Name', 'Email', 'Phone Number', 'ID Number', 'Profile','Department']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style = style1)

    for stf in staff:
        row_num += 1
        row = [stf['first_name'],stf['last_name'], stf['email'], stf['phone_number'], stf['identification_no'],stf['profile'],stf['user_department']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
def generate_staff_csv(request):
    staff = []
    data = json.loads(request.body)
    user_department = data['user_department']
    name = data['name']
    status = data['is_active']
    identification_no = data['identification_no']
    profile = data['profile']
    phone_number = data['phone_number']
    company_id = data['company_id']

    company_uuid = uuid.UUID(company_id)
    company_users = User.objects.filter(allowed_company=company_uuid)

    staffList = company_users.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)) & Q(user_department__name__icontains=user_department)
                                & Q(identification_no__icontains=identification_no) & Q(phone_number__icontains=phone_number) )
    
    if status:
        staffList = staffList.filter(is_active = status)

    if profile:
        staffList = staffList.filter(profile = profile)
    

    for stf in staffList:
        if stf.profile != "Super Admin" and stf.profile != "Patient":
            obj = {
                "user_id": stf.user_id,
                "email": stf.email,
                "first_name": stf.first_name,
                "last_name": stf.last_name,
                "is_active": stf.is_active,
                "identification_no": stf.identification_no,
                "profile": stf.profile,
                "phone_number": stf.phone_number,
                "user_department": stf.user_department.name,
            }
            staff.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Staff.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name', 'Email', 'Phone Number', 'ID Number', 'Profile','Department'])

    for stf in staff:
        writer.writerow([stf['first_name'],stf['last_name'], stf['email'], stf['phone_number'], stf['identification_no'],stf['profile'],stf['user_department']])
    return response

            #MANAGER VIEWS
    
class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


@csrf_exempt
@api_view(['POST'])
def createManager(request):
    company_id = request.data.get("company")
    department_id = request.data.get("department")
    company_uuid = uuid.UUID(company_id)
    department_uuid = uuid.UUID(department_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    department = Department.objects.get(department_id=department_uuid)
    serializer = ManagerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(department=department,company=company)

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def getDepartmentManagers(request):
    manager_id = request.data.get("manager")
    company_id = request.data.get("company")
    department_id = request.data.get("department")

    if manager_id is not None and department_id is not None:
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company_id)
        manager_uuid = uuid.UUID(manager_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        department = Department.objects.filter(company=company_uuid, department_id=department_uuid)
        manager = Manager.objects.get(company=company, department=department, manager_id=manager_uuid)

        serializer = ManagerSerializer(manager)
        return Response(serializer.data)

    elif department_id is not None:
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        manager = Manager.objects.filter(company=company, department=department_uuid)

        serializer = ManagerSerializer(manager, many=True)
        return Response(serializer.data)

    else:
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        manager = Manager.objects.filter(company=company)

        serializer = ManagerSerializer(manager, many=True)
        return Response(serializer.data)

csrf_exempt
@api_view(['PUT'])
def updateDepartmentManager(request):
    manager_id = request.data.get("manager")
    department_id = request.data.get("department")
    company = request.data.get("company")
    manager_uuid = uuid.UUID(manager_id)
    department_uuid = uuid.UUID(department_id)
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    manager = Manager.objects.get(company=company_id,department_id=department_uuid,manager_id=manager_uuid)
    
    serializer = ManagerSerializer(manager, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors)

    return Response(serializer.data)

@api_view(['PUT'])
def replaceManager(request):
    company_id = request.data.get("company")
    manager_id = request.data.get("manager")
    manager_uuid = uuid.UUID(manager_id)
    company_uuid = uuid.UUID(company_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    manager = Manager.objects.get(manager_id=manager_uuid,company=company)
    end_date = request.data.get('end_date')
    serializer = ManagerSerializer(manager, data=request.data, partial=True)
    new_end_date= (datetime.strptime(end_date, "%Y-%m-%d")- timedelta(days=1)).strftime("%Y-%m-%d")

    if serializer.is_valid():
        serializer.save(end_date=new_end_date)

    else:
        print(serializer.errors)    
        
    return Response(serializer.data)




    
