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

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = BasePagination

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = DefaultPagination

class AppointmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@csrf_exempt
@api_view(['POST'])
def createAppointment(request):
    hospital_id = request.data.get("hospital")
    patient_id = request.data.get("patient")
    doctor_id = request.data.get("doctor")
    print("The doctor is of the type ",type(doctor_id))

    if doctor_id is not None: 
        print("Buda I'm the one")
        hospital_uuid = uuid.UUID(hospital_id)
        doctor_uuid = uuid.UUID(doctor_id)
        patient_uuid = uuid.UUID(patient_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        patient = Patient.objects.get(patient_id=patient_uuid)
        doctor = Doctor.objects.get(doctor_id=doctor_uuid)
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(hospital=hospital,patient=patient, doctor=doctor)

        else:
            print(serializer.errors) 

        return Response(serializer.data)
    
    else:
        print("I am running the show")
        hospital_uuid = uuid.UUID(hospital_id)
        patient_uuid = uuid.UUID(patient_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        patient = Patient.objects.get(patient_id=patient_uuid)
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(hospital=hospital,patient=patient)

        else:
            print(serializer.errors) 

        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def getAppointments(request):
    appointment_id = request.data.get("appointment")
    hospital_id = request.data.get("hospital")
    patient_id = request.data.get("patient")
    doctor_id = request.data.get("doctor")

    if appointment_id is not None:
        appointment_uuid = uuid.UUID(appointment_id)
        hospital_uuid = uuid.UUID(hospital_id)
        patient_uuid = uuid.UUID(patient_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        patient = Patient.objects.get(patient_id=patient_uuid, hospital=hospital)
        appointment = Appointment.objects.get(hospital=hospital, patient=patient, appointment_id=appointment_uuid)

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    elif patient_id is not None and doctor_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        patient_uuid = uuid.UUID(patient_id)
        doctor_uuid = uuid.UUID(doctor_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        appointments = Appointment.objects.filter(hospital=hospital, patient=patient_uuid, doctor=doctor_uuid)

        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)

    elif patient_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        patient_uuid = uuid.UUID(patient_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        appointments = Appointment.objects.filter(hospital=hospital, patient=patient_uuid)

        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)

    elif doctor_id is not None:
        hospital_uuid = uuid.UUID(hospital_id)
        doctor_uuid = uuid.UUID(doctor_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        appointments = Appointment.objects.filter(hospital=hospital, doctor=doctor_uuid)

        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)
    
    else:
        hospital_uuid = uuid.UUID(hospital_id)
        hospital = get_object_or_404(Company, company_id=hospital_uuid)
        appointments = Appointment.objects.filter(hospital=hospital)

        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
def updateAppointment(request):
    appointment_id = request.data.get("appointment")
    hospital = request.data.get("hospital")
    patient_id = request.data.get("patient")
    doctor_id = request.data.get("doctor")

    if doctor_id is not None:
        hospital_uuid = uuid.UUID(hospital)
        doctor_uuid = uuid.UUID(doctor_id)
        patient_uuid = uuid.UUID(patient_id)
        appointment_uuid = uuid.UUID(appointment_id)
        hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
        patient = Patient.objects.get(hospital=hospital_id,patient_id=patient_uuid)
        doctor = Doctor.objects.get(hospital=hospital_id, doctor_id=doctor_uuid)
        appointment = Appointment.objects.get(appointment_id=appointment_uuid)
        serializer = AppointmentSerializer(appointment, data=request.data)

        if serializer.is_valid():
            serializer.save(doctor=doctor, patient=patient)

        else:
            print(serializer.errors) 

        return Response(serializer.data)
    else:
        hospital_uuid = uuid.UUID(hospital)
        appointment_uuid = uuid.UUID(appointment_id)
        hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
        patient_uuid = uuid.UUID(patient_id)
        patient = Patient.objects.get(hospital=hospital_id,patient_id=patient_uuid)
        appointment = Appointment.objects.get(appointment_id=appointment_uuid)
        serializer = AppointmentSerializer(appointment, data=request.data)

        if serializer.is_valid():
            serializer.save(patient=patient)

        else:
            print(serializer.errors) 

        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def deleteAppointment(request):
    appointment_id = request.data.get("appointment")
    hospital = request.data.get("hospital")
    hospital_uuid = uuid.UUID(hospital)
    hospital_id = get_object_or_404(Company, company_id=hospital_uuid)
    appointment_uuid = uuid.UUID(appointment_id)
    appointment = Appointment.objects.get(hospital=hospital_id,appointment_id=appointment_uuid)

    appointment.delete() 
    message = {'msg':"The appointment has been succesfully deleted"} 
    return Response(message)


@csrf_exempt   
@api_view(['POST'])
def generate_appointments_pdf(request):
    appointments = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    empty = ""
    patient = data['patient_name']
    doctor = data['doctor_name']
    from_date = data['from_date']
    to_date = data['to_date']
    hospital_id = data['hospital']

    appointmentsList = Appointment.objects.filter((Q(patient__first_name__icontains=patient)|Q(patient__last_name__icontains=patient)) 
                                & (Q(doctor__first_name__icontains=doctor)|Q(doctor__last_name__icontains=doctor)) )

    if from_date:
        appointmentsList = appointmentsList.filter(date__gte=from_date) 
    
    if to_date:
        appointmentsList = appointmentsList.filter(date__lte=to_date) 

    for apt in appointmentsList:
        if (str(apt.hospital.company_id) == hospital_id and apt.time):
            obj = {
                "appointment_id": apt.appointment_id,
                "patient_id": apt.patient.patient_id,
                "patient_name": apt.patient.first_name + " "+ apt.patient.last_name,
                "patient_id_number": apt.patient.id_number,
                "doctor_id": apt.doctor.doctor_id,
                "doctor_name": apt.doctor.first_name + " "+ apt.doctor.last_name,
                "date": apt.date.strftime("%d %b, %Y"),
                "time": apt.time,
                "notes": apt.notes,
            }
            appointments.append(obj)
        else:
            obj = {
                "appointment_id": apt.appointment_id,
                "patient_id": apt.patient.patient_id,
                "patient_name": apt.patient.first_name + " "+ apt.patient.last_name,
                "patient_id_number": apt.patient.id_number,
                "doctor_id": apt.doctor.doctor_id,
                "doctor_name": apt.doctor.first_name + " "+ apt.doctor.last_name,
                "date": apt.date.strftime("%d %b, %Y"),
                "time": empty,
                "notes": apt.notes,
            }
            appointments.append(obj)

    context = {"appointments":appointments}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/Hospital Management System/hms/bookings/templates/bookings')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('appointmentsPDF.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Appointments.pdf', configuration=config, options=options, css="/home/sammyb/Hospital Management System/hms/bookings/static/bookings/appointmentsPDF.css")

    path = 'Appointments.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Appointments.pdf'
    pdf.close()
    os.remove("Appointments.pdf")  # remove the locally created pdf file.
    return response

@csrf_exempt
@api_view(['POST'])
def generate_appointments_excel(request):
    appointments = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    empty = ""
    patient = data['patient_name']
    doctor = data['doctor_name']
    from_date = data['from_date']
    to_date = data['to_date']
    hospital_id = data['hospital']

    appointmentsList = Appointment.objects.filter((Q(patient__first_name__icontains=patient)|Q(patient__last_name__icontains=patient)) 
                                & (Q(doctor__first_name__icontains=doctor)|Q(doctor__last_name__icontains=doctor)) )

    if from_date:
        appointmentsList = appointmentsList.filter(date__gte=from_date) 
    
    if to_date:
        appointmentsList = appointmentsList.filter(date__lte=to_date) 

    for apt in appointmentsList:
        if (str(apt.hospital.company_id) == hospital_id):
            obj = {
                "appointment_id": apt.appointment_id,
                "patient_id": apt.patient.patient_id,
                "patient_name": apt.patient.first_name + " "+ apt.patient.last_name,
                "patient_id_number": apt.patient.id_number,
                "doctor_id": apt.doctor.doctor_id,
                "doctor_name": apt.doctor.first_name + " "+ apt.doctor.last_name,
                "date": apt.date.strftime("%d %b, %Y"),
                "time": apt.time,
                "notes": apt.notes,
            }
            appointments.append(obj)


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Appointments.xls'

    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet("Appointments")

    row_num = 0
    columns = ['Patient Name','Patient ID No','Doctor Name','Date','Time','Notes']
    style1 = xlwt.easyxf('font:bold 1')
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num],style=style1)

    for apt in appointments:
        row_num += 1
        row = [apt['patient_name'],apt['patient_id_number'],apt['doctor_name'],apt['date'],apt['time'],apt['notes']]
        for col_num in range(len(row)):
            worksheet.write(row_num, col_num, row[col_num])
       
    workbook.save(response)
    return response

@csrf_exempt
@api_view(['POST'])
def generate_appointments_csv(request):
    appointments = []
    new_data = json.dumps(request.data)
    data = json.loads(new_data)
    patient = data['patient_name']
    doctor = data['doctor_name']
    from_date = data['from_date']
    to_date = data['to_date']
    hospital_id = data['hospital']

    appointmentsList = Appointment.objects.filter((Q(patient__first_name__icontains=patient)|Q(patient__last_name__icontains=patient)) 
                                & (Q(doctor__first_name__icontains=doctor)|Q(doctor__last_name__icontains=doctor)) )

    if from_date:
        appointmentsList = appointmentsList.filter(date__gte=from_date) 
    
    if to_date:
        appointmentsList = appointmentsList.filter(date__lte=to_date) 

    for apt in appointmentsList:
        if (str(apt.hospital.company_id) == hospital_id):
            obj = {
                "appointment_id": apt.appointment_id,
                "patient_id": apt.patient.patient_id,
                "patient_name": apt.patient.first_name + " "+ apt.patient.last_name,
                "patient_id_number": apt.patient.id_number,
                "doctor_id": apt.doctor.doctor_id,
                "doctor_name": apt.doctor.first_name + " "+ apt.doctor.last_name,
                "date": apt.date.strftime("%d %b, %Y"),
                "time": apt.time,
                "notes": apt.notes,
            }
            appointments.append(obj)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Appointments.csv'

    writer = csv.writer(response)
    writer.writerow(['Patient Name','Patient ID No','Doctor Name','Date','Time','Notes'])

    for apt in appointments:
        writer.writerow([apt['patient_name'],apt['patient_id_number'],apt['doctor_name'],apt['date'],apt['time'],apt['notes']])
    return response
