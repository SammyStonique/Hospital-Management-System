from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/',include('billing_management.urls')),
    path('api/v1/',include('bookings.urls')),
    path('api/v1/',include('customer_support.urls')),
    path('api/v1/',include('doctor_profile.urls')),
    path('api/v1/',include('inventory_management.urls')),
    path('api/v1/',include('lab_management.urls')),
    path('api/v1/',include('patients_registration.urls')),
    path('api/v1/',include('payroll.urls')),
    path('api/v1/',include('statistical_data.urls')),
    path('api/v1/',include('users.urls')),
    path('api/v1/',include('xtra.urls')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
