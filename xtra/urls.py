from django.urls import path,include
from . import views
from .filters import departmentSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("departments",views.DepartmentViewSet, basename="departments")

urlpatterns = [
    path("", include(router.urls)),
    path("department-list/", views.DepartmentList.as_view()),
    path("department-details/<int:pk>/", views.DepartmentDetails.as_view()),
    path("department-search/", departmentSearch, name="department_search"),
    path("export-departments-pdf/", views.generate_departments_pdf, name="export-departments-pdf"),
    path("export-departments-excel/", views.generate_departments_excel, name="export-departments-excel"),
    path("export-departments-csv/", views.generate_departments_csv, name="export-departments-csv"),
]