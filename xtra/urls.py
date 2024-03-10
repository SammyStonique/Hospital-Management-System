from django.urls import path,include
from . import views
from .filters import departmentSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("departments",views.DepartmentViewSet, basename="departments")

urlpatterns = [
    path("", include(router.urls)),
    path("create-department/", views.createDepartment, name="create-department"),
    path("update-department/", views.updateDepartment, name="update-department"),
    path("fetch-departments/", views.getDepartments, name="fetch-department"),
    path("delete-department/", views.deleteDepartment, name="delete-department"),
    path("department-list/", views.DepartmentList.as_view()),
    path("department-details/<str:pk>/", views.DepartmentDetails.as_view()),
    path("department-search/", departmentSearch, name="department_search"),
    path("export-departments-pdf/", views.generate_departments_pdf, name="export-departments-pdf"),
    path("export-departments-excel/", views.generate_departments_excel, name="export-departments-excel"),
    path("export-departments-csv/", views.generate_departments_csv, name="export-departments-csv"),
    path("display-departments-import-excel/", views.display_departments_import_excel, name="display-departments-import-excel"),
    path("import-departments-excel/", views.import_departments_excel, name="import-departments-excel"),
]