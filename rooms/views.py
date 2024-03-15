import environ,os
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

import re
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from .models import *
from company.models import Company
from xtra.models import Department
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime,timedelta
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


           #ROOMS VIEWS
    
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


@csrf_exempt
@api_view(['POST'])
def createRoom(request):
    company_id = request.data.get("company")
    department_id = request.data.get("department")
    company_uuid = uuid.UUID(company_id)
    department_uuid = uuid.UUID(department_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    department = Department.objects.get(department_id=department_uuid)
    serializer = RoomSerializer(data=request.data)


    if serializer.is_valid():
        serializer.save(department=department,company=company)

    else:
        print(serializer.errors) 
    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def getDepartmentRooms(request):
    room_id = request.data.get("room")
    company_id = request.data.get("company")
    department_id = request.data.get("department")

    if room_id is not None and department_id is not None:
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company_id)
        room_uuid = uuid.UUID(room_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        room = Room.objects.get(company=company, department=department_uuid, room_id=room_uuid)

        serializer = RoomSerializer(room)
        return Response(serializer.data)

    elif department_id is not None:
        department_uuid = uuid.UUID(department_id)
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        room = Room.objects.filter(company=company, department=department_uuid)

        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    else:
        company_uuid = uuid.UUID(company_id)
        company = get_object_or_404(Company, company_id=company_uuid)
        rooms = Room.objects.filter(company=company)

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

csrf_exempt
@api_view(['PUT'])
def updateDepartmentRoom(request):
    room_id = request.data.get("room")
    department_id = request.data.get("department")
    company = request.data.get("company")
    room_uuid = uuid.UUID(room_id)
    department_uuid = uuid.UUID(department_id)
    company_uuid = uuid.UUID(company)
    company_id = get_object_or_404(Company, company_id=company_uuid)
    room = Room.objects.get(company=company_id,room_id=room_uuid)
    
    serializer = RoomSerializer(room, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors)

    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def deleteRoom(request):
    room_id = request.data.get("room")
    department_id = request.data.get("department")
    company = request.data.get("company")
    company_uuid = uuid.UUID(company)
    department_uuid = uuid.UUID(department_id)
    room_uuid = uuid.UUID(room_id)
    department = get_object_or_404(Department, company=company_uuid, department_id=department_uuid)
    room = Room.objects.get(company=company_uuid,department=department, room_id=room_uuid)

    room.delete() 
    message = {'msg':"The room has been succesfully deleted"} 
    return Response(message)

        #ROOM REPORTS

@csrf_exempt 
@api_view(['POST'])
def generate_rooms_pdf(request):
    roomsList = []
    data = json.loads(request.body)
    room_code = data['room_code']
    room_name = data['room_name']
    department = data['department']
    company_id = data['company']

    company_uuid = uuid.UUID(company_id)
    department_rooms = Room.objects.filter(company=company_uuid)

    rooms = department_rooms.filter(Q(room_code__icontains=room_code) & Q(room_name__icontains=room_name) & Q(department__name__icontains=department) )

    for rom in rooms:
        obj = {
            "room_id": rom.room_id,
            "room_code": rom.room_code,
            "room_name": rom.room_name,
            "department_id": rom.department.department_id,
            "department_name": rom.department.name,
            "staff": rom.staff
        }
        roomsList.append(obj)

    context = {"rooms":roomsList}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/rooms/templates/rooms')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('roomsPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Rooms.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/rooms/static/rooms/roomsPDF.css")

    path = 'Rooms.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Rooms.pdf'
    pdf.close()
    os.remove("Rooms.pdf")  # remove the locally created pdf file.
    return response

@api_view(['POST'])
@csrf_exempt
def generate_rooms_excel(request):
    roomsList = []
    data = json.loads(request.body)
    room_code = data['room_code']
    room_name = data['room_name']
    department = data['department']
    company_id = data['company']

    company_uuid = uuid.UUID(company_id)
    department_rooms = Room.objects.filter(company=company_uuid)

    rooms = department_rooms.filter(Q(room_code__icontains=room_code) & Q(room_name__icontains=room_name) & Q(department__name__icontains=department) )

    for rom in rooms:
        obj = {
            "room_id": rom.room_id,
            "room_code": rom.room_code,
            "room_name": rom.room_name,
            "department_id": rom.department.department_id,
            "department_name": rom.department.name,
            "staff": rom.staff
        }
        roomsList.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Rooms.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Rooms")

    row_num = 0
    columns = ['Code','Name','Department','Staff']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style = style1)

    for rom in roomsList:
        row_num += 1
        row = [rom['room_code'],rom['room_name'], rom['department_name'], rom['staff']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@api_view(['POST'])
@csrf_exempt
def generate_rooms_csv(request):
    roomsList = []
    data = json.loads(request.body)
    room_code = data['room_code']
    room_name = data['room_name']
    department = data['department']
    company_id = data['company']

    company_uuid = uuid.UUID(company_id)
    department_rooms = Room.objects.filter(company=company_uuid)

    rooms = department_rooms.filter(Q(room_code__icontains=room_code) & Q(room_name__icontains=room_name) & Q(department__name__icontains=department) )

    for rom in rooms:
        obj = {
            "room_id": rom.room_id,
            "room_code": rom.room_code,
            "room_name": rom.room_name,
            "department_id": rom.department.department_id,
            "department_name": rom.department.name,
            "staff": rom.staff
        }
        roomsList.append(obj)


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Rooms.csv'

    writer = csv.writer(response)
    writer.writerow(['Code','Name','Department','Staff'])

    for rom in roomsList:
        writer.writerow([rom['room_code'],rom['room_name'], rom['department_name'], rom['staff']])
    return response

@csrf_exempt
@api_view(['POST'])
def display_rooms_import_excel(request):
    roomsList = []
    excel_file = request.FILES['rooms_excel']
    wb = load_workbook(excel_file)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, values_only=True):
        code,name, department,staff = row
        obj = {
            "room_code": code,
            "room_name": name,
            "department": department,
            "staff": staff
        }
        roomsList.append(obj)

    return JsonResponse({"rooms": roomsList})


@csrf_exempt
@api_view(['POST'])
def import_rooms_excel(request):

    excel_file = request.FILES['rooms_excel']
    company_id = request.data.get('company')
    company_uuid = uuid.UUID(company_id)
    company = get_object_or_404(Company, company_id=company_uuid)
    rooms = Room.objects.filter(company=company)
    wb = load_workbook(excel_file)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, values_only=True):
        code,name, department,staff = row
        department_id = Department.objects.get(name=department,company=company)
        Room.objects.create(room_code=code, room_name=name, department=department_id, company=company, staff=staff) 
        

    return HttpResponse("Excel Import Succesful")