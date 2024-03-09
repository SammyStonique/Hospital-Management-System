from django.urls import path,include
from . import views

from .filters import doctorSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("doctors",views.DoctorViewSet, basename="doctors")

urlpatterns = [
    path("", include(router.urls)),
    path("doctor-list/", views.DoctorList.as_view()),
    path("doctor-details/<int:pk>/", views.DoctorDetails.as_view()),
    path("doctor-search/", doctorSearch, name="doctor-search"),
    path("create-department-doctor/", views.createDoctor, name="create-department-doctor"),
    path("get-department-doctors/", views.getDepartmentDoctors, name="get-department-doctors"),
    path("update-department-doctor/", views.updateDepartmentDoctor, name="update-department-doctor"),
    path("export-doctors-pdf/", views.generate_doctors_pdf, name="export-doctors-pdf"),
    path("export-doctors-excel/", views.generate_doctors_excel, name="export-doctors-excel"),
    path("export-doctors-csv/", views.generate_doctors_csv, name="export-doctors-csv"),
    path("delete-doctor/", views.deleteDoctor, name="delete-doctor")
]