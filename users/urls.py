from django.urls import path,include

from . import views
from . import pass_generator

urlpatterns = [
    path("user-list/", views.UserList.as_view()),
    path("user-details/<int:pk>/", views.UserDetails.as_view()),
    path('pass-gen/', pass_generator.password_generator),
    path('user-credentials/<int:user_id>/', views.send_user_credentials, name="user-credentials"),
    path('user-image/<int:user_id>/', views.get_user_image, name="user-image"),
]