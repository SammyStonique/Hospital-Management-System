from django.urls import path,include

from . import views

urlpatterns = [
    path("doctor-list/", views.DoctorList.as_view()),
    path("doctor-details/<int:pk>", views.DoctorDetails.as_view()),
]