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
