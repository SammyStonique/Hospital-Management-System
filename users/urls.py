from django.urls import path,include

from . import views
from . import pass_generator
from .filters import staffSearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("systemusers",views.UserViewSet, basename="systemusers")

urlpatterns = [
    path("", include(router.urls)),
    path("user-list/", views.UserList.as_view()),
    path("user-details/<int:pk>/", views.UserDetails.as_view()),
    path('pass-gen/', pass_generator.password_generator),
    path('user-credentials/<int:user_id>/', views.send_user_credentials, name="user-credentials"),
    path('user-image/<int:user_id>/', views.get_user_image, name="user-image"),
    path("staff-search/", staffSearch, name="staff_search"),
    path("export-staff-pdf/", views.generate_staff_pdf, name="export-staff-pdf"),
    path("export-staff-excel/", views.generate_staff_excel, name="export-staff-excel"),
    path("export-staff-csv/", views.generate_staff_csv, name="export-staff-csv"),
    path("manager-list/", views.ManagerList.as_view()),
    path("manager-details/<int:pk>/", views.ManagerDetails.as_view()),
    path("get-manager/<int:dep_id>/", views.getManager, name="get-manager")
]