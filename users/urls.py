from django.urls import path,include

from . import views
from . import pass_generator
from .filters import staffSearch, managersSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("systemusers",views.UserViewSet, basename="systemusers")

urlpatterns = [
    path("", include(router.urls)),
    path("user-list/", views.UserList.as_view()),
    path("department-staff-list/", views.getDepartmentStaff, name="department-staff-list"),
    path("user-details/<int:pk>/", views.UserDetails.as_view()),
    path('pass-gen/', pass_generator.password_generator),
    path("reset-password/<str:user_id>/", views.reset_password, name="reset-password"),
    path('user-credentials/<str:user_id>/', views.send_user_credentials, name="user-credentials"),
    path("staff-search/", staffSearch, name="staff_search"),
    path("export-staff-pdf/", views.generate_staff_pdf, name="export-staff-pdf"),
    path("export-staff-excel/", views.generate_staff_excel, name="export-staff-excel"),
    path("export-staff-csv/", views.generate_staff_csv, name="export-staff-csv"),
    path("manager-list/", views.ManagerList.as_view()),
    path("manager-details/<int:pk>/", views.ManagerDetails.as_view()),
    path("create-department-manager/", views.createManager, name="create-department-manager"),
    path("get-department-managers/", views.getDepartmentManagers, name="get-department-managers"),
    path("update-department-manager/", views.updateDepartmentManager, name="update-department-manager"),
    path("replace-manager/", views.replaceManager, name="replace-manager"),
    path("managers-search/", managersSearch, name="managers_search"),
    path("export-managers-pdf/", views.generate_managers_pdf, name="export-managers-pdf"),
    path("export-managers-excel/", views.generate_managers_excel, name="export-managers-excel"),
    path("export-managers-csv/", views.generate_managers_csv, name="export-managers-csv"),

]