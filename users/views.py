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
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
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

# Create your views here.

        #PAGINATION

class BasePagination(PageNumberPagination):
    page_size = 10
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

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def send_user_credentials(request, user_id): 
    data = json.loads(request.body)
    temporary_password = data['temporary_password']
    created_user = get_object_or_404(User, id=user_id)
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

def get_user_image(request, user_id):
    selected_user = get_object_or_404(User, id=user_id)
    user_image = selected_user.image
    return HttpResponse(str(user_image))

def generate_staff_pdf(request):
    users = User.objects.all()
    staff = []

    for stf in users:
        if(stf.profile != "Super Admin" and stf.profile != "Patient"):
            staff.append(stf)

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

def generate_staff_excel(request):
    users = User.objects.all()
    staff = []

    for stf in users:
        if(stf.profile != "Super Admin" and stf.profile != "Patient"):
            staff.append(stf)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Staff.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Staff")

    row_num = 0
    columns = ['First Name','Last Name', 'Email', 'Phone Number', 'ID Number', 'Profile']
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num])

    for stf in staff:
        row_num += 1
        row = [stf.first_name,stf.last_name, stf.email, stf.phone_number, stf.identification_no,stf.profile]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

def generate_staff_csv(request):
    users = User.objects.all()
    staff = []

    for stf in users:
        if(stf.profile != "Super Admin" and stf.profile != "Patient"):
            staff.append(stf)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Staff.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name', 'Email', 'Phone Number', 'ID Number', 'Profile'])

    for stf in staff:
        writer.writerow([stf.first_name,stf.last_name, stf.email, stf.phone_number, stf.identification_no,stf.profile])
    return response
