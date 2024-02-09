from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField()
    manager = models.CharField()
    manager_start_date = models.DateField()

    def __str__(self):
        return f'{self.name} Department'

class Doctor(models.Model):
    payroll_number = models.CharField()
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    email = models.EmailField()
    department = models.CharField()
    specialization = models.CharField()
    phone_number = models.CharField()
    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'