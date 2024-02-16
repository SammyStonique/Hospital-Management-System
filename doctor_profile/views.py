from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
#Pagination
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

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

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
