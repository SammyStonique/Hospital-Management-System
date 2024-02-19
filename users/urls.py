from django.urls import path,include

from . import views
from . import pass_generator

urlpatterns = [
    path('pass-gen/', pass_generator.password_generator),
    path('user-credentials/<int:user_id>/', views.send_user_credentials, name="user-credentials"),
]