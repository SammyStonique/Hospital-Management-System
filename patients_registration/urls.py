from django.urls import path,include
from . import views
from . import patient_code_generator
from .filters import patientsSearch,contactPersonSearch,patientsHistorySearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("patients",views.PatientViewSet, basename="patients")
router.register("contact-persons",views.EmergencyContactPersonViewSet, basename="contact-persons")

from . import views

urlpatterns = [
    path("", include(router.urls)),
    path("create-patient/", views.createPatient, name="create-patient"),
    path('patient-code-gen/<str:hospital_id>/', patient_code_generator.patient_code_generator),
    path("update-patient/", views.updatePatient, name="update-patient"),
    path("get-patients/", views.getPatients, name="get-patients"),
    path("delete-patient/", views.deletePatient, name="delete-patient"),
    path("patient-list/", views.PatientList.as_view()),
    path("patient-details/<str:pk>/", views.PatientDetails.as_view()),
    path("patients-search/", patientsSearch, name="patients_search"),
    path("export-patients-pdf/", views.generate_patients_pdf, name="export-patients-pdf"),
    path("export-patients-excel/", views.generate_patients_excel, name="export-patients-excel"),
    path("export-patients-csv/", views.generate_patients_csv, name="export-patients-csv"),
    path("display-patients-import-excel/", views.display_patients_import_excel, name="display-import-patients-excel"),
    path("import-patients-excel/", views.import_patients_excel, name="import-patients-excel"),
    path("create-emergency-contact-person/", views.createEmergencyContactPerson, name="create-emergency-contact-person"),
    path("update-emergency-contact-person/", views.updateEmergencyContactPerson, name="update-emergency-contact-person"),
    path("get-emergency-contact-persons/", views.getEmergencyContactPersons, name="get-emergency-contact-persons"),
    path("delete-emergency-contact-person/", views.deleteEmergencyContactPerson, name="delete-emergency-contact-person"),
    path("emergency-contact-person-list/", views.EmergencyContactPersonList.as_view()),
    path("emergency-contact-person-details/<str:pk>/", views.EmergencyContactPersonDetails.as_view()),
    path("emergency-contact-person-search/", contactPersonSearch, name="patients_search"),
    path("export-emergency-contact-person-pdf/", views.generate_contact_persons_pdf, name="export-emergency-contact-person-pdf"),
    path("export-emergency-contact-person-excel/", views.generate_contact_persons_excel, name="export-emergency-contact-person-excel"),
    path("export-emergency-contact-person-csv/", views.generate_contact_persons_csv, name="export-emergency-contact-person-csv"),
    path("create-patient-history/", views.createPatientHistory, name="create-patient-history"),
    path("update-patient-history/", views.updatePatientHistory, name="update-patient-history"),
    path("get-patients-history/", views.getPatientHistories, name="get-patients-history"),
    path("delete-patient-history/", views.deletePatientHistory, name="delete-patient-history"),
    path("patient-history-list/", views.PatientHistoryList.as_view()),
    path("patient-history-details/<str:pk>/", views.PatientHistoryDetails.as_view()),
    path("patients-history-search/", patientsHistorySearch, name="patients_history_search"),
    path("export-patients-history-pdf/", views.generate_patients_history_pdf, name="export-patients-history-pdf"),
    path("export-patients-history-excel/", views.generate_patients_history_excel, name="export-patients-history-excel"),
    path("export-patients-history-csv/", views.generate_patients_history_csv, name="export-patients-history-csv"),
]