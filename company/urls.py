from django.urls import path,include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("companies",views.CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(router.urls)),
    path("company-list/", views.CompanyList.as_view()),
    path("company-details/<int:pk>/", views.CompanyDetails.as_view()),
]