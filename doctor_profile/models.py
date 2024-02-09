from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=250)
    manager = models.CharField(max_length=250)
    manager_start_date = models.DateField()

    def __str__(self):
        return f'{self.name} Department'

class Doctor(models.Model):
    payroll_number = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    email = models.EmailField()
    department = models.ForeignKey(Department, related_name='departments', on_delete=models.DO_NOTHING)
    specialization = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'