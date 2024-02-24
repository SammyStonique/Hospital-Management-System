from django.db import models

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