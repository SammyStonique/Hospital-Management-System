import os
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from company.models import Company
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.response import Response
from datetime import datetime
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

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DefaultPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000


        #PATIENT VIEWS

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = BasePagination

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = DefaultPagination

class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@csrf_exempt
@api_view(['POST'])
def createPatient(request):
    hospital_id = request.data.get("hospital")
    emergency_contact_id = request.data.get("emergency_contact_person")
    hospital_uuid = uuid.UUID(hospital_id)
    emergency_contact_uuid = uuid.UUID(emergency_contact_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    emergency_contact = EmergencyContactPerson.objects.get(contact_person_id=emergency_contact_uuid)
    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(hospital=hospital,emergency_contact_person=emergency_contact)

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def getPatients(request):
    hospital_id = request.data.get("hospital")
    patient_id = request.data.get("patient")

    if patient_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        patient_uuid = uuid.UUID(patient_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        patient = Patient.objects.get(hospital=hospital, patient_id=patient_uuid)

        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    else:
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        patients = Patient.objects.filter(hospital=hospital)

        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
def updatePatient(request):
    patient_id = request.data.get("patient")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    patient_uuid = uuid.UUID(patient_id)
    patient = Patient.objects.get(hospital=hospital_id,patient_id=patient_uuid)
    
    serializer = PatientSerializer(patient, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def deletePatient(request):
    patient_id = request.data.get("patient")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    patient_uuid = uuid.UUID(patient_id)
    patient = Patient.objects.get(hospital=hospital_id,patient_id=patient_uuid)

    patient.delete() 
    message = {'msg':"The patient has been succesfully deleted"} 
    return Response(message)


@csrf_exempt   
@api_view(['POST'])
def generate_patients_pdf(request):
    patients = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    id_number = data['id_number']
    city = data['city']
    birth_date = data['birth_date']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_patients = Patient.objects.filter(hospital=hospital_uuid)

    patientList = hospital_patients.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(birth_date__icontains=birth_date)
                                        & Q(phone_number__icontains=phone_number) & Q(id_number__icontains=id_number) & Q(city__icontains=city))

    for pat in patientList:
        obj = {
            "patient_id": pat.patient_id,
            "first_name": pat.first_name,
            "last_name": pat.last_name,
            "email": pat.email,
            "id_number": pat.id_number,
            "phone_number": pat.phone_number,
            "city": pat.city,
            "address": pat.address,
            "country": pat.country,
            "birth_date": pat.birth_date.strftime("%d %b, %Y")
        }
        patients.append(obj)

    context = {"patients":patients}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/patients_registration/templates/patients_registration')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('patientsPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Patients.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/patients_registration/static/patients_registration/patientsPDF.css")

    path = 'Patients.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Patients.pdf'
    pdf.close()
    os.remove("Patients.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
@api_view(['POST'])
def generate_patients_excel(request):
    patients = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    first_name = data['first_name']
    last_name = data['last_name']
    birth_date = data['birth_date']
    phone_number = data['phone_number']
    id_number = data['id_number']
    city = data['city']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_patients = Patient.objects.filter(hospital=hospital_uuid)

    patientList = hospital_patients.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(birth_date__icontains=birth_date)
                                        & Q(phone_number__icontains=phone_number) & Q(id_number__icontains=id_number) & Q(city__icontains=city))

    for pat in patientList:
        obj = {
            "patient_id": pat.patient_id,
            "first_name": pat.first_name,
            "last_name": pat.last_name,
            "email": pat.email,
            "id_number": pat.id_number,
            "phone_number": pat.phone_number,
            "city": pat.city,
            "address": pat.address,
            "country": pat.country,
            "birth_date": pat.birth_date.strftime("%d %b, %Y")
        }
        patients.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Patients.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Patients")

    row_num = 0
    columns = ['First Name','Last Name','Email','ID Number','Phone Number','Address','Birth Date','City','Country']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for pat in patients:
        row_num += 1
        row = [pat['first_name'],pat['last_name'],pat['email'],pat['id_number'],pat['phone_number'],pat['address'],pat['birth_date'],pat['city'],pat['country']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
@api_view(['POST'])
def generate_patients_csv(request):
    patients = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    first_name = data['first_name']
    last_name = data['last_name']
    birth_date = data['birth_date']
    phone_number = data['phone_number']
    id_number = data['id_number']
    city = data['city']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    hospital_patients = Patient.objects.filter(hospital=hospital_uuid)

    patientList = hospital_patients.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name) & Q(birth_date__icontains=birth_date)
                                        & Q(phone_number__icontains=phone_number) & Q(id_number__icontains=id_number) & Q(city__icontains=city))

    for pat in patientList:
        obj = {
            "patient_id": pat.patient_id,
            "first_name": pat.first_name,
            "last_name": pat.last_name,
            "email": pat.email,
            "id_number": pat.id_number,
            "phone_number": pat.phone_number,
            "city": pat.city,
            "address": pat.address,
            "country": pat.country,
            "birth_date": pat.birth_date.strftime("%d %b, %Y")
        }
        patients.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Patients.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email','ID Number','Phone Number','Address','Birth Date','City','Country'])

    for pat in patients:
        writer.writerow([pat['first_name'],pat['last_name'],pat['email'],pat['id_number'],pat['phone_number'],pat['address'],pat['birth_date'],pat['city'],pat['country']])
    return response

@csrf_exempt
@api_view(['POST'])
def display_patients_import_excel(request):
    patientList = []
    excel_file = request.FILES['patients_excel']
    wb = load_workbook(excel_file)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, values_only=True):
        first_name,last_name,email,id_number,phone_number,address,birth_date,city,country = row
        obj = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "id_number": id_number,
            "phone_number": phone_number,
            "address": address,
            "birth_date": datetime.strptime(str(birth_date), "%Y-%m-%d %H:%M:%S").strftime("%d %b, %Y"),
            "city": city,
            "country": country,
        }
        patientList.append(obj)

    return JsonResponse({"patients": patientList})


@csrf_exempt
@api_view(['POST'])
def import_patients_excel(request):

    excel_file = request.FILES['patients_excel']
    hospital_id = request.data.get('hospital_id')
    hospital_uuid = uuid.UUID(hospital_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    patients = Patient.objects.filter(hospital=hospital)
    wb = load_workbook(excel_file)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, values_only=True):
        first_name,last_name,email,id_number,phone_number,address,birth_date,city,country = row
        Patient.objects.create(first_name=first_name, last_name=last_name, email=email, id_number=id_number, birth_date=birth_date,
                               phone_number=phone_number,city=city,address=address, country=country, hospital=hospital) 
        

    return HttpResponse("Excel Import Succesful")


        #EMERGENCY CONTACT PERSON VIEWS

class EmergencyContactPersonViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContactPerson.objects.all()
    serializer_class = EmergencyContactPersonSerializer
    pagination_class = BasePagination

class EmergencyContactPersonList(generics.ListCreateAPIView):
    queryset = EmergencyContactPerson.objects.all()
    serializer_class = EmergencyContactPersonSerializer
    pagination_class = DefaultPagination

class EmergencyContactPersonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmergencyContactPerson.objects.all()
    serializer_class = EmergencyContactPersonSerializer


@csrf_exempt
@api_view(['POST'])
def createEmergencyContactPerson(request):
    hospital_id = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital_id)
    hospital = get_object_or_404(Company, company_id=hospital_uuid)
    serializer = EmergencyContactPersonSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(hospital=hospital)

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def getEmergencyContactPersons(request):
    hospital_id = request.data.get("hospital")
    contact_person_id = request.data.get("contact_person")

    if contact_person_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        contact_person_uuid = uuid.UUID(contact_person_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        contact_person = EmergencyContactPerson.objects.get(hospital=hospital, contact_person_id=contact_person_uuid)

        serializer = EmergencyContactPersonSerializer(contact_person)
        return Response(serializer.data)

    else:
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        contact_persons = EmergencyContactPerson.objects.filter(hospital=hospital)

        serializer = EmergencyContactPersonSerializer(contact_persons, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
def updateEmergencyContactPerson(request):
    contact_person_id = request.data.get("contact_person")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    contact_person_uuid = uuid.UUID(contact_person_id)
    contact_person = EmergencyContactPerson.objects.get(hospital=hospital_id,contact_person_id=contact_person_uuid)
    
    serializer = EmergencyContactPersonSerializer(contact_person, data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        print(serializer.errors) 

    
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def deleteEmergencyContactPerson(request):
    contact_person_id = request.data.get("contact_person")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    contact_person_uuid = uuid.UUID(contact_person_id)
    contact_person = EmergencyContactPerson.objects.get(hospital=hospital_id,contact_person_id=contact_person_uuid)

    contact_person.delete() 
    message = {'msg':"The emergency contact person has been succesfully deleted"} 
    return Response(message)


@csrf_exempt   
def generate_contact_persons_pdf(request):
    contact_persons = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone_number = data['phone_number']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    patients_contact_persons = EmergencyContactPerson.objects.filter(hospital=hospital_uuid)

    contactPersonList = patients_contact_persons.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name)
                                                       & Q(email__icontains=email) & Q(phone_number__icontains=phone_number))
                                        

    for cont in contactPersonList:
        obj = {
            "contact_person_id": cont.contact_person_id,
            "first_name": cont.first_name,
            "last_name": cont.last_name,
            "email": cont.email,
            "phone_number": cont.phone_number,
        }
        contact_persons.append(obj)

    context = {"contact_persons":contact_persons}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/patients_registration/templates/patients_registration')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('contactPersonsPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Contact People.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/patients_registration/static/patients_registration/patientsPDF.css")

    path = 'Contact People.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Contact People.pdf'
    pdf.close()
    os.remove("Contact People.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
def generate_contact_persons_excel(request):
    contact_persons = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone_number = data['phone_number']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    patients_contact_persons = EmergencyContactPerson.objects.filter(hospital=hospital_uuid)

    contactPersonList = patients_contact_persons.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name)
                                                       & Q(email__icontains=email) & Q(phone_number__icontains=phone_number))
                                        

    for cont in contactPersonList:
        obj = {
            "contact_person_id": cont.contact_person_id,
            "first_name": cont.first_name,
            "last_name": cont.last_name,
            "email": cont.email,
            "phone_number": cont.phone_number,
        }
        contact_persons.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Contact People.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Contact People")

    row_num = 0
    columns = ['First Name','Last Name','Email','Phone Number']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for cont in contact_persons:
        row_num += 1
        row = [cont['first_name'],cont['last_name'],cont['email'],cont['phone_number']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
def generate_contact_persons_csv(request):
    contact_persons = []
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone_number = data['phone_number']
    hospital_id = data['hospital_id']

    hospital_uuid = uuid.UUID(hospital_id)
    patients_contact_persons = EmergencyContactPerson.objects.filter(hospital=hospital_uuid)

    contactPersonList = patients_contact_persons.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name)
                                                       & Q(email__icontains=email) & Q(phone_number__icontains=phone_number))
                                        

    for cont in contactPersonList:
        obj = {
            "contact_person_id": cont.contact_person_id,
            "first_name": cont.first_name,
            "last_name": cont.last_name,
            "email": cont.email,
            "phone_number": cont.phone_number,
        }
        contact_persons.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Conatact People.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email','Phone Number'])

    for cont in contact_persons:
        writer.writerow([cont['first_name'],cont['last_name'],cont['email'],cont['phone_number']])
    return response

