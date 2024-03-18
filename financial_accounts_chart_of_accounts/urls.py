from django.urls import path,include
from . import views
from .filters import clientCategorySearch

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("clientcategories",views.ClientCategoryViewSet, basename="clientcategories")

urlpatterns = [
    path("", include(router.urls)),
    path("create-client-category/", views.createClientCategory, name="create-client-category"),
    path("update-client-category/", views.updateClientCategory, name="update-client-category"),
    path("fetch-client-categories/", views.getClientCategories, name="fetch-client-categories"),
    path("delete-client-category/", views.deleteClientCategory, name="delete-client-category"),
    path("client-category-list/", views.ClientCategoryList.as_view()),
    path("client-category-details/<str:pk>/", views.ClientCategoryDetails.as_view()),
    path("client-category-search/", clientCategorySearch, name="client-category_search"),
    path("export-client-categories-pdf/", views.generate_client_categories_pdf, name="export-client-categories-pdf"),
    path("export-client-categories-excel/", views.generate_client_categories_excel, name="export-client-categories-excel"),
    path("export-client-categories-csv/", views.generate_client_categories_csv, name="export-client-categories-csv"),

]