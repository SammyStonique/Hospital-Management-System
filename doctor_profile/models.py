from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class Department(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} Department'
    
    class Meta:
        ordering = [('id')]
    
class Manager(models.Model):
    STATUS = (('','Select Status'),('Active','Active'),('Inactive','Inactive'))

    department = models.ForeignKey(Department, related_name='dep_manager', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    phone_number = models.CharField(max_length=250)
    end_date = models.DateField()
    status = models.CharField(max_length=250, choices=STATUS, default='')

    def __str__(self):
        return f'{self.department.name} Manager'

class Doctor(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,null=True,blank=True)
    payroll_number = models.CharField(max_length=250, blank=True)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    email = models.EmailField()
    # department = models.ForeignKey(Department, related_name='departments', on_delete=models.DO_NOTHING, blank=True)
    specialization = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=250)


    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'
    

    # @receiver(post_save, sender=UserModel)
    # def create_doctor(sender, instance, created, **kwargs):
    #     if created:
    #         Doctor.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name,
    #                               phone_number=instance.phone_number, email=instance.email)