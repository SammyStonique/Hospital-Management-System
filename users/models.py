from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from PIL import Image
from xtra.models import Department
from company.models import Company
import uuid


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email,phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,phone_number, password, **other_fields)
    
    def create_user(self, email,phone_number,password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other')) 
    PROFILES = (('', 'Select User Profile'),('Super Admin','Super Admin'),('Admin','Admin'),('Doctor','Doctor'),('Patient','Patient'),
                ('Accountant','Accountant'),('Human Resource','Human Resource'),('Nurse','Nurse'),('Lab Technician','Lab Technician'),
                ('Office Clerk','Office Clerk'),('Clinical Officer','Clinical Officer'),)

    user_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=250,blank=True)
    last_name = models.CharField(max_length=250,blank=True)
    identification_no = models.CharField(max_length=250,blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=250,choices=GENDER,default='',blank=True)
    phone_number = models.CharField(max_length=250)
    profile = models.CharField(max_length=250,choices=PROFILES,default='',blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    user_department = models.ForeignKey(Department, related_name='user_departments', on_delete=models.DO_NOTHING)
    user_department_name = models.CharField(max_length=250, null=True, blank=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= False)
    start_date = models.DateTimeField(auto_now_add=True)
    allowed_company = models.ForeignKey(Company, related_name='user_company', on_delete=models.CASCADE)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name','identification_no','birth_date','gender','profile','image','is_staff','is_active','user_department','user_department_name','allowed_company']

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        ordering = [('first_name')]
    
    def save(self,*args,**kwargs):
        super(User,self).save()

        img = Image.open(self.image.path)

        if img.height > 20 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def getDepartmentName(self):
        return self.user_department.name
        
class Manager(models.Model):
    STATUS = (('','Select Status'),('Active','Active'),('Inactive','Inactive'))

    manager_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    department = models.ForeignKey(Department, related_name='dep_manager', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='manager_company', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_manager", on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=250, null=True, blank=True)
    start_date = models.DateField()
    phone_number = models.CharField(max_length=250)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=250, choices=STATUS, default='')


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.department.name} Manager'
    
    class Meta:
        ordering = [('-start_date')]
