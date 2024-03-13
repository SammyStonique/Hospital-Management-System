from django.urls import path,include
from . import views
from .filters import appointmentsSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("appointments",views.AppointmentViewSet, basename="appointments")

from . import views

urlpatterns = [
    path("", include(router.urls)),
    path("create-appointment/", views.createAppointment, name="create-appointment"),
    path("update-appointment/", views.updateAppointment, name="update-appointment"),
    path("get-appointments/", views.getAppointments, name="get-appointments"),
    path("delete-appointment/", views.deleteAppointment, name="delete-appointment"),
    path("appointment-list/", views.AppointmentList.as_view()),
    path("appointment-details/<str:pk>/", views.AppointmentDetails.as_view()),
    path("appointments-search/", appointmentsSearch, name="appointments_search"),
    path("export-appointments-pdf/", views.generate_appointments_pdf, name="export-appointments-pdf"),
    path("export-appointments-excel/", views.generate_appointments_excel, name="export-appointments-excel"),
    path("export-appointments-csv/", views.generate_appointments_csv, name="export-appointments-csv"),
]