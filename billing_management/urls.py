from django.urls import path,include
from .filters import medicalFeesSearch

from . import views

urlpatterns = [
    path("medical-fee-list/", views.MedicalFeeList.as_view()),
    path("medical-fee-details/", views.MedicalFeeDetails.as_view()),
    path("create-medical-fee/", views.createMedicalFee, name="create-medical-fee"),
    path("get-medical-fees/", views.getMedicalFees, name="get-medical-fees"),
    path("update-medical-fee/", views.updateMedicalFee, name="update-medical-fee"),
    path("medical-fees-search/", medicalFeesSearch, name="medical-fees_search"),
    path("export-medical-fees-pdf/", views.generate_medical_fees_pdf, name="export-medical-fees-pdf"),
    path("export-medical-fees-excel/", views.generate_medical_fees_excel, name="export-medical-fees-excel"),
    path("export-medical-fees-csv/", views.generate_medical_fees_csv, name="export-medical-fees-csv"),
    path("delete-medical-fee/", views.deleteMedicalFee, name="delete-medical-fee"),
]
