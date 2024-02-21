from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'phone_number','first_name','profile')
    list_filter = ('email', 'phone_number','first_name', 'profile', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name','last_name','phone_number', 'profile',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','profile')}),
        ('Personal', {'fields': ('phone_number','birth_date','gender','identification_no','image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2','phone_number','image',
                       'gender', 'birth_date','identification_no', 'profile', 'is_active', 'is_staff')}
         ),
    )
admin.site.register(User,UserAdminConfig)