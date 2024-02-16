from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("departments",views.DepartmentViewSet, basename="departments")

urlpatterns = [
    path("", include(router.urls)),
    path("doctor-list/", views.DoctorList.as_view()),
    path("doctor-details/<int:pk>/", views.DoctorDetails.as_view()),
    path("department-list/", views.DepartmentList.as_view()),
    path("department-details/<int:pk>/", views.DepartmentDetails.as_view()),
    path("manager-list/", views.ManagerList.as_view()),
    path("manager-details/<int:id>/", views.ManagerDetails.as_view()),
]